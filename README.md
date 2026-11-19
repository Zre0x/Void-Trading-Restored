# Void Trading Restored

Void Trading Restored reverses Mojang's fix for MC-50614, introduced in snapshot
24w44a and released in Minecraft Java Edition 1.21.4. That fix closes the trading
window when a villager leaves interaction range, preventing legacy void trading.
The mod restores keeping an existing trade menu open across distance and chunk
unloading for both villagers and wandering traders, allowing the original
void-trading mechanisms to work again.

See [MC-50614](https://bugs.mojang.com/browse/MC-50614) and the
[official 24w44a changelog](https://www.minecraft.net/en-us/article/minecraft-snapshot-24w44a).

The shared mixin keeps an existing trade menu valid outside interaction range
and after `UNLOADED_TO_CHUNK`. Customer ownership and dimension checks remain
active. Trade uses, experience, restocking and entity AI use vanilla code.
The same `AbstractVillager` patch covers villagers and wandering traders.

## Downloads

Choose your Minecraft version and mod loader. All downloads are version 1.0.1.

| Minecraft | Fabric | NeoForge |
| --- | --- | --- |
| 1.21.4 | [Fabric](https://github.com/Zre0x/Void-Trading-Restored/raw/refs/heads/main/dist/1.21.4/void-trading-restored-fabric-1.21.4-1.0.1.jar) | [NeoForge](https://github.com/Zre0x/Void-Trading-Restored/raw/refs/heads/main/dist/1.21.4/void-trading-restored-neoforge-1.21.4-1.0.1.jar) |
| 1.21.5 | [Fabric](https://github.com/Zre0x/Void-Trading-Restored/raw/refs/heads/main/dist/1.21.5/void-trading-restored-fabric-1.21.5-1.0.1.jar) | [NeoForge](https://github.com/Zre0x/Void-Trading-Restored/raw/refs/heads/main/dist/1.21.5/void-trading-restored-neoforge-1.21.5-1.0.1.jar) |
| 1.21.6 | [Fabric](https://github.com/Zre0x/Void-Trading-Restored/raw/refs/heads/main/dist/1.21.6/void-trading-restored-fabric-1.21.6-1.0.1.jar) | [NeoForge](https://github.com/Zre0x/Void-Trading-Restored/raw/refs/heads/main/dist/1.21.6/void-trading-restored-neoforge-1.21.6-1.0.1.jar) |
| 1.21.7 | [Fabric](https://github.com/Zre0x/Void-Trading-Restored/raw/refs/heads/main/dist/1.21.7/void-trading-restored-fabric-1.21.7-1.0.1.jar) | [NeoForge](https://github.com/Zre0x/Void-Trading-Restored/raw/refs/heads/main/dist/1.21.7/void-trading-restored-neoforge-1.21.7-1.0.1.jar) |
| 1.21.8 | [Fabric](https://github.com/Zre0x/Void-Trading-Restored/raw/refs/heads/main/dist/1.21.8/void-trading-restored-fabric-1.21.8-1.0.1.jar) | [NeoForge](https://github.com/Zre0x/Void-Trading-Restored/raw/refs/heads/main/dist/1.21.8/void-trading-restored-neoforge-1.21.8-1.0.1.jar) |
| 1.21.9 | [Fabric](https://github.com/Zre0x/Void-Trading-Restored/raw/refs/heads/main/dist/1.21.9/void-trading-restored-fabric-1.21.9-1.0.1.jar) | [NeoForge](https://github.com/Zre0x/Void-Trading-Restored/raw/refs/heads/main/dist/1.21.9/void-trading-restored-neoforge-1.21.9-1.0.1.jar) |
| 1.21.10 | [Fabric](https://github.com/Zre0x/Void-Trading-Restored/raw/refs/heads/main/dist/1.21.10/void-trading-restored-fabric-1.21.10-1.0.1.jar) | [NeoForge](https://github.com/Zre0x/Void-Trading-Restored/raw/refs/heads/main/dist/1.21.10/void-trading-restored-neoforge-1.21.10-1.0.1.jar) |
| 1.21.11 | [Fabric](https://github.com/Zre0x/Void-Trading-Restored/raw/refs/heads/main/dist/1.21.11/void-trading-restored-fabric-1.21.11-1.0.1.jar) | [NeoForge](https://github.com/Zre0x/Void-Trading-Restored/raw/refs/heads/main/dist/1.21.11/void-trading-restored-neoforge-1.21.11-1.0.1.jar) |
| 26.1 | [Fabric](https://github.com/Zre0x/Void-Trading-Restored/raw/refs/heads/main/dist/26.1/void-trading-restored-fabric-26.1-1.0.1.jar) | [NeoForge](https://github.com/Zre0x/Void-Trading-Restored/raw/refs/heads/main/dist/26.1/void-trading-restored-neoforge-26.1-1.0.1.jar) |
| 26.1.1 | [Fabric](https://github.com/Zre0x/Void-Trading-Restored/raw/refs/heads/main/dist/26.1.1/void-trading-restored-fabric-26.1.1-1.0.1.jar) | [NeoForge](https://github.com/Zre0x/Void-Trading-Restored/raw/refs/heads/main/dist/26.1.1/void-trading-restored-neoforge-26.1.1-1.0.1.jar) |
| 26.1.2 | [Fabric](https://github.com/Zre0x/Void-Trading-Restored/raw/refs/heads/main/dist/26.1.2/void-trading-restored-fabric-26.1.2-1.0.1.jar) | [NeoForge](https://github.com/Zre0x/Void-Trading-Restored/raw/refs/heads/main/dist/26.1.2/void-trading-restored-neoforge-26.1.2-1.0.1.jar) |
| 26.2 | [Fabric](https://github.com/Zre0x/Void-Trading-Restored/raw/refs/heads/main/dist/26.2/void-trading-restored-fabric-26.2-1.0.1.jar) | [NeoForge](https://github.com/Zre0x/Void-Trading-Restored/raw/refs/heads/main/dist/26.2/void-trading-restored-neoforge-26.2-1.0.1.jar) |
| 26.3 | [Fabric](https://github.com/Zre0x/Void-Trading-Restored/raw/refs/heads/main/dist/26.3/void-trading-restored-fabric-26.3-1.0.1.jar) | [NeoForge](https://github.com/Zre0x/Void-Trading-Restored/raw/refs/heads/main/dist/26.3/void-trading-restored-neoforge-26.3-1.0.1.jar) |

## Build

Requires Python 3, Gradle 9.6 and internet access to official Maven repositories.
The script finds Gradle on PATH or in the user's cached Gradle 9.6 distribution.
Gradle can provision Java toolchains through the Foojay resolver.

Run all 26 targets from this directory.

```sh
python3 build_ports.py
```

Build one target.

```sh
python3 build_ports.py --minecraft 1.21.4 --loader neoforge
```

Use `--gradle /absolute/path/to/gradle` to select another Gradle executable.
Production JARs are copied to `dist/<minecraft-version>/` only after a successful
build. A failed target makes the script exit with an error after the other
targets have been attempted.

The code lives in `common/AbstractVillagerMixin.java`. The two loader projects
are regenerated sequentially from `versions.json`, with an exact Minecraft
dependency for each build. `common.gradle` generates the correct import for
the selected Minecraft version during compilation.

Targets are 1.21.4 through 1.21.11, 26.1, 26.1.1, 26.1.2, 26.2 and 26.3.
Fabric 1.21.x uses Loom's remapping plugin and official Mojang mappings.
Fabric 26.x and NeoForge use Mojang names directly.
Some NeoForge targets have only beta loader versions pinned by the official MDK.

## Verification status

All 26 Fabric and NeoForge targets were compiled. Built JARs are included in
`dist/<minecraft-version>/`. Their archive integrity, exact Minecraft metadata
and naming domains were checked.

The original Fabric 26.3 version was tested in game. Runtime loading and the
trade/unload/reload cycle on the remaining loader/version combinations have
not yet been verified.

Install the matching JAR in the server's `mods` directory. In singleplayer,
install it in the local game's `mods` directory. The mod adds no client content
or networking channels.

## License

MIT License

Copyright (c) 2026 Zre0x

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
