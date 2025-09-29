import { world, system, Player, ItemStack, EntityItemComponent } from "@minecraft/server";

(() => {
    // 整地ツールの設定
    const CLEAR_ITEM = "minecraft:stick"; // 木の枝
    const CLEAR_WIDTH = 10;   // 横幅
    const CLEAR_HEIGHT = 10;  // 高さ
    const CLEAR_DEPTH = 10;   // 奥行き
    const JUMP_POWER = 1.5;   // ジャンプの強さ
    const JUMP_FORWARD = 2;   // 前方への移動距離

    // プレイヤーごとのクールダウン管理
    const playerCooldowns = new Map<string, number>();
    const COOLDOWN_TICKS = 10; // 0.5秒のクールダウン

    // 整地処理
    function clearTerrain(player: Player): void {
        const location = player.location;
        const rotation = player.getRotation();
        const dimension = player.dimension;

        // プレイヤーの視線方向を計算
        const yaw = rotation.y * (Math.PI / 180);
        const pitch = rotation.x * (Math.PI / 180);

        // 前方向のベクトルを計算
        const directionX = -Math.sin(yaw) * Math.cos(pitch);
        const directionY = -Math.sin(pitch);
        const directionZ = Math.cos(yaw) * Math.cos(pitch);

        // 整地範囲の中心点を計算（プレイヤーの前方）
        const centerOffset = CLEAR_DEPTH / 2;
        const centerX = Math.floor(location.x + directionX * centerOffset);
        const centerY = Math.floor(location.y + directionY * centerOffset);
        const centerZ = Math.floor(location.z + directionZ * centerOffset);

        // 10x10x10の範囲を空気に置換
        const halfWidth = Math.floor(CLEAR_WIDTH / 2);
        const halfHeight = Math.floor(CLEAR_HEIGHT / 2);
        const halfDepth = Math.floor(CLEAR_DEPTH / 2);

        try {
            // ブロックを空気に置換
            for (let x = -halfWidth; x <= halfWidth; x++) {
                for (let y = -halfHeight; y <= halfHeight; y++) {
                    for (let z = -halfDepth; z <= halfDepth; z++) {
                        const blockX = centerX + x;
                        const blockY = centerY + y;
                        const blockZ = centerZ + z;

                        // 範囲内のブロックを空気に置換
                        try {
                            const blockLocation = { x: blockX, y: blockY, z: blockZ };
                            const block = dimension.getBlock(blockLocation);
                            if (block) {
                                block.setType("minecraft:air");
                            }
                        } catch (error) {
                            // ブロックが範囲外の場合は無視
                        }
                    }
                }
            }

            // プレイヤーを前方にジャンプさせる
            player.applyKnockback(directionX, directionZ, JUMP_FORWARD, JUMP_POWER);

            // エフェクトとメッセージ
            player.playSound("random.explode", { volume: 0.5, pitch: 2.0 });
            player.sendMessage("§a整地完了！ 10x10x10のブロックを除去しました");

        } catch (error) {
            player.sendMessage(`§c整地中にエラーが発生しました: ${error}`);
        }
    }

    // アイテム使用イベントの監視
    world.afterEvents.itemUse.subscribe((event: any) => {
        const player = event.source as Player;
        const item = event.itemStack;

        // 木の枝を使用した場合
        if (item && item.typeId === CLEAR_ITEM) {
            const playerId = player.id;
            const currentTick = system.currentTick;

            // クールダウンチェック
            const lastUse = playerCooldowns.get(playerId) || 0;
            if (currentTick - lastUse < COOLDOWN_TICKS) {
                return;
            }
            playerCooldowns.set(playerId, currentTick);

            clearTerrain(player);
        }
    });

    // コマンド登録（オプション）
    world.beforeEvents.chatSend.subscribe((event: any) => {
        const player = event.sender as Player;
        const message = event.message.toLowerCase();

        if (message === "!cleartool") {
            event.cancel = true;

            // プレイヤーに木の枝を与える
            try {
                const inventory = player.getComponent("inventory") as EntityItemComponent;
                if (inventory && inventory.container) {
                    const stick = new ItemStack("minecraft:stick", 1);
                    inventory.container.addItem(stick);
                    player.sendMessage("§a整地ツール（木の枝）を付与しました！");
                    player.sendMessage("§e使い方: 木の枝を持って右クリック（使用）すると、前方10x10x10のブロックを除去します");
                }
            } catch (error) {
                player.sendMessage("§cアイテムの付与に失敗しました");
            }
        }
    });

    // 初期化メッセージ
    system.runTimeout(() => {
        world.sendMessage("§b整地システムが起動しました！");
        world.sendMessage("§e木の枝を持って右クリックで10x10x10の範囲を整地");
        world.sendMessage("§eチャットで '!cleartool' と入力すると木の枝を取得");
    }, 20);
})();