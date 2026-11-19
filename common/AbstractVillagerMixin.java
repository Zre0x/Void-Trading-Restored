package dev.voidtrading.mixin;

import net.minecraft.world.entity.Entity;
import @VILLAGER_PACKAGE@.AbstractVillager;
import net.minecraft.world.entity.player.Player;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfoReturnable;

@Mixin(AbstractVillager.class)
abstract class AbstractVillagerMixin {
    @Inject(method = "stillValid", at = @At("HEAD"), cancellable = true)
    private void voidtrading$allowUnloadedMerchant(Player player, CallbackInfoReturnable<Boolean> callback) {
        AbstractVillager merchant = (AbstractVillager) (Object) this;
        boolean unloaded = merchant.getRemovalReason() == Entity.RemovalReason.UNLOADED_TO_CHUNK;
        callback.setReturnValue(merchant.getTradingPlayer() == player
                && merchant.level() == player.level()
                && (merchant.isAlive() || unloaded));
    }
}
