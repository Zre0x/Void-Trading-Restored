#!/usr/bin/env python3
"""Generate and build exact-version ports using official loader repositories."""

import argparse
import json
import re
import shutil
import subprocess
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VERSIONS = [f"1.21.{patch}" for patch in range(4, 12)] + [
    "26.1", "26.1.1", "26.1.2", "26.2", "26.3"
]
LOADERS = ["fabric", "neoforge"]
MOD_VERSION = "1.0.1"


def fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": "VoidTrading-Build/1.0"})
    with urllib.request.urlopen(request, timeout=45) as response:
        return response.read()


def resolve(loader, minecraft):
    pins_path = ROOT / "versions.json"
    if pins_path.exists():
        pins = json.loads(pins_path.read_text())
        if minecraft in pins and loader in pins[minecraft]:
            return pins[minecraft][loader]
    if loader == "fabric":
        entries = json.loads(fetch(f"https://meta.fabricmc.net/v2/versions/loader/{minecraft}"))
        return next(entry["loader"]["version"] for entry in entries if entry["loader"]["stable"])
    properties = fetch(f"https://raw.githubusercontent.com/NeoForgeMDKs/MDK-{minecraft}-ModDevGradle/main/gradle.properties").decode()
    version = re.search(r"^neo_version=(.+)$", properties, re.MULTILINE)
    if not version:
        raise RuntimeError(f"NeoForge MDK has no version for {minecraft}")
    return version.group(1).strip()


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def generate(loader, minecraft, loader_version):
    modern = minecraft.startswith("26.")
    old_package = minecraft.startswith("1.21.") and int(minecraft.split(".")[-1]) < 11
    package = "net.minecraft.world.entity.npc" + ("" if old_package else ".villager")
    java = 25 if modern else 21
    directory = ROOT / loader
    config = {
        "required": True, "minVersion": "0.8", "package": "dev.voidtrading.mixin",
        "mixins": ["AbstractVillagerMixin"], "injectors": {"defaultRequire": 1}
    }
    if not modern and loader == "fabric":
        config["refmap"] = "voidtrading.refmap.json"
    write(directory / "src/main/resources/voidtrading.mixins.json", json.dumps(config, indent=2) + "\n")
    settings = """pluginManagement {
    repositories {
        maven { url = 'https://maven.fabricmc.net/' }
        maven { url = 'https://maven.neoforged.net/releases' }
        gradlePluginPortal()
    }
}
plugins {
    id 'org.gradle.toolchains.foojay-resolver-convention' version '1.0.0'
}
rootProject.name = 'void-trading-restored'
"""
    write(directory / "settings.gradle", settings)
    common = f"""
version = '{MOD_VERSION}'
group = 'dev.voidtrading'
base.archivesName = 'void-trading-restored-{loader}-{minecraft}'
java.toolchain.languageVersion = JavaLanguageVersion.of({java})
tasks.withType(JavaCompile).configureEach {{ options.encoding = 'UTF-8' }}
"""
    if loader == "fabric":
        plugin = "net.fabricmc.fabric-loom" + ("" if modern else "-remap")
        dependencies = f"minecraft 'com.mojang:minecraft:{minecraft}'\n"
        if not modern:
            dependencies += "mappings loom.officialMojangMappings()\n"
        dependencies += f"{'implementation' if modern else 'modImplementation'} 'net.fabricmc:fabric-loader:{loader_version}'"
        build = f"plugins {{ id '{plugin}' version '1.17.21' }}\n" + common
        build += "repositories { mavenCentral() }\ndependencies {\n" + dependencies + "\n}\n"
        if not modern:
            build += "loom { mixin { defaultRefmapName = 'voidtrading.refmap.json' } }\n"
        metadata = {"schemaVersion": 1, "id": "voidtrading", "version": MOD_VERSION,
                    "name": "Void Trading Restored", "environment": "*", "license": "MIT",
                    "mixins": ["voidtrading.mixins.json"],
                    "depends": {"fabricloader": f">={loader_version}", "minecraft": f"={minecraft}", "java": f">={java}"}}
        write(directory / "src/main/resources/fabric.mod.json", json.dumps(metadata, indent=2) + "\n")
    else:
        build = "plugins { id 'java'; id 'net.neoforged.moddev' version '2.0.148' }\n" + common
        build += f"neoForge {{ version = '{loader_version}' }}\n"
        header = '' if modern else 'modLoader="lowcodefml"\nloaderVersion="[1,)"\n'
        metadata = header + f'''license="MIT"
[[mixins]]
config="voidtrading.mixins.json"
[[mods]]
modId="voidtrading"
version="{MOD_VERSION}"
displayName="Void Trading Restored"
[[dependencies.voidtrading]]
modId="minecraft"
type="required"
versionRange="[{minecraft}]"
ordering="NONE"
side="BOTH"
'''
        write(directory / "src/main/resources/META-INF/neoforge.mods.toml", metadata)
    build += f"ext.villagerPackage = '{package}'\napply from: '../common.gradle'\n"
    write(directory / "build.gradle", build)
    write(directory / "gradle.properties", "org.gradle.jvmargs=-Xmx3G\norg.gradle.daemon=false\n")
    return directory


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--minecraft", choices=VERSIONS, action="append")
    parser.add_argument("--loader", choices=LOADERS, action="append")
    cached_gradle = next((Path.home() / ".gradle/wrapper/dists/gradle-9.6.0-bin").glob("*/gradle-9.6.0/bin/gradle"), None)
    default_gradle = shutil.which("gradle") or str(cached_gradle or "gradle")
    parser.add_argument("--gradle", default=default_gradle, help="Gradle 9.6 executable")
    parser.add_argument("--generate-only", action="store_true")
    arguments = parser.parse_args()
    failures = []
    for minecraft in arguments.minecraft or VERSIONS:
        for loader in arguments.loader or LOADERS:
            try:
                version = resolve(loader, minecraft)
                directory = generate(loader, minecraft, version)
                print(f"Prepared {minecraft} {loader} {version}", flush=True)
                if arguments.generate_only:
                    continue
                subprocess.run([arguments.gradle, "--no-daemon", "clean", "build"], cwd=directory, check=True)
                jars = list((directory / "build/libs").glob("*.jar"))
                jars = [jar for jar in jars if not any(tag in jar.name for tag in ("-sources", "-dev"))]
                if len(jars) != 1:
                    raise RuntimeError(f"Expected one production jar, found {jars}")
                output = ROOT / "dist" / minecraft
                output.mkdir(parents=True, exist_ok=True)
                shutil.copy2(jars[0], output / f"void-trading-restored-{loader}-{minecraft}-{MOD_VERSION}.jar")
            except (OSError, RuntimeError, ValueError, StopIteration, subprocess.CalledProcessError) as error:
                failures.append(f"{minecraft}/{loader}: {error}")
                print(f"FAILED {failures[-1]}", flush=True)
    if failures:
        raise SystemExit("\n".join(failures))


if __name__ == "__main__":
    main()
