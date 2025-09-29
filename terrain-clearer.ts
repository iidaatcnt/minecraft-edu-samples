import { world, system } from "@minecraft/server";

// すべてのコードを単一の関数内で実行
function initializeTerrainClearer() {
    // 整地ツールの設定
    const CLEAR_ITEM = "minecraft:stick";
    const CLEAR_WIDTH = 10;
    const CLEAR_HEIGHT = 10;
    const CLEAR_DEPTH = 10;
    const JUMP_POWER = 1.5;
    const JUMP_FORWARD = 2;
    const COOLDOWN_TICKS = 10;

    // プレイヤーごとのクールダウン管理
    const playerCooldowns = new Map();

    // アイテム使用イベントの監視
    world.afterEvents.itemUse.subscribe((event) => {
        const player = event.source;
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

            // 整地処理実行
            const location = player.location;
            const rotation = player.getRotation();
            const dimension = player.dimension;

            // プレイヤーの視線方向を計算
            const yaw = rotation.y * (3.14159 / 180);
            const pitch = rotation.x * (3.14159 / 180);

            // 前方向のベクトルを計算
            const directionX = -Math.sin(yaw) * Math.cos(pitch);
            const directionY = -Math.sin(pitch);
            const directionZ = Math.cos(yaw) * Math.cos(pitch);

            // 整地範囲の中心点を計算
            const centerOffset = CLEAR_DEPTH / 2;
            const centerX = Math.floor(location.x + directionX * centerOffset);
            const centerY = Math.floor(location.y + directionY * centerOffset);
            const centerZ = Math.floor(location.z + directionZ * centerOffset);

            // 範囲を計算
            const halfWidth = Math.floor(CLEAR_WIDTH / 2);
            const halfHeight = Math.floor(CLEAR_HEIGHT / 2);
            const halfDepth = Math.floor(CLEAR_DEPTH / 2);

            try {
                // ブロックを空気に置換
                for (let x = -halfWidth; x <= halfWidth; x++) {
                    for (let y = -halfHeight; y <= halfHeight; y++) {
                        for (let z = -halfDepth; z <= halfDepth; z++) {
                            try {
                                const block = dimension.getBlock({
                                    x: centerX + x,
                                    y: centerY + y,
                                    z: centerZ + z
                                });
                                if (block) {
                                    block.setType("minecraft:air");
                                }
                            } catch (e) {
                                // ブロックが範囲外の場合は無視
                            }
                        }
                    }
                }

                // プレイヤーを前方にジャンプ
                player.applyKnockback(directionX, directionZ, JUMP_FORWARD, JUMP_POWER);

                // エフェクトとメッセージ
                player.playSound("random.explode", { volume: 0.5, pitch: 2.0 });
                player.sendMessage("§a整地完了！ 10x10x10のブロックを除去しました");

            } catch (error) {
                player.sendMessage("§c整地中にエラーが発生しました");
            }
        }
    });

    // チャットコマンド
    world.beforeEvents.chatSend.subscribe((event) => {
        const player = event.sender;
        const message = event.message.toLowerCase();

        if (message === "!cleartool") {
            event.cancel = true;

            // 木の枝を与える
            try {
                const inventory = player.getComponent("inventory");
                if (inventory && inventory.container) {
                    const ItemStack = world.ItemStack || system.ItemStack;
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
}

// 関数を即座に実行
initializeTerrainClearer();