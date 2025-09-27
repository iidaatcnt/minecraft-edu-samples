// ============================================
// 方向対応TNTキャノン建築プログラム
// ============================================
// このプログラムは東西南北の4方向に対応したTNTキャノンを建築します
// 使い方: cannonDir <方向>
// 方向: north, south, east, west (または n, s, e, w)

// ヘルパー関数: 土台を作成する
// x座標, y座標, z座標を指定して3x10の土台を作成します
function buildPlatform(startX: number, startY: number, startZ: number, direction: string) {
    // 方向によって土台の向きを変える
    if (direction === "south" || direction === "north") {
        // 南北方向: 横3 x 縦10
        for (let lengthOffset = 0; lengthOffset < 10; lengthOffset++) {
            for (let widthOffset = 0; widthOffset < 3; widthOffset++) {
                let x = startX + widthOffset - 1  // 中心を基準に左右に配置
                let z = startZ + lengthOffset
                builder.teleportTo(pos(x, startY, z))
                builder.place(COBBLESTONE)
            }
        }
    } else {
        // 東西方向: 横10 x 縦3
        for (let lengthOffset = 0; lengthOffset < 10; lengthOffset++) {
            for (let widthOffset = 0; widthOffset < 3; widthOffset++) {
                let x = startX + lengthOffset
                let z = startZ + widthOffset - 1  // 中心を基準に上下に配置
                builder.teleportTo(pos(x, startY, z))
                builder.place(COBBLESTONE)
            }
        }
    }
}

// ヘルパー関数: 方向を設定する
function setBuilderDirection(direction: string) {
    // 方向の文字列を対応するMinecraftの定数に変換
    switch(direction) {
        case "north":
        case "n":
            builder.face(NORTH)
            break
        case "south":
        case "s":
            builder.face(SOUTH)
            break
        case "east":
        case "e":
            builder.face(EAST)
            break
        case "west":
        case "w":
            builder.face(WEST)
            break
        default:
            // デフォルトは南向き
            builder.face(SOUTH)
    }
}

// ヘルパー関数: キャノンの開始位置を計算する
function getCannonStartPosition(direction: string, baseX: number, baseY: number, baseZ: number) {
    // 方向によって開始位置を調整
    switch(direction) {
        case "north":
        case "n":
            // 北向きの場合、z座標を調整
            return { x: baseX, y: baseY + 1, z: baseZ + 9 }
        case "south":
        case "s":
            // 南向きの場合（デフォルト）
            return { x: baseX, y: baseY + 1, z: baseZ }
        case "east":
        case "e":
            // 東向きの場合
            return { x: baseX, y: baseY + 1, z: baseZ }
        case "west":
        case "w":
            // 西向きの場合、x座標を調整
            return { x: baseX + 9, y: baseY + 1, z: baseZ }
        default:
            return { x: baseX, y: baseY + 1, z: baseZ }
    }
}

// ヘルパー関数: キャノン本体を建築する（方向対応版）
function buildCannonBody(direction: string) {
    // ===== 石の壁（U字型）を作る =====
    builder.mark()              // 現在位置をマーク
    builder.move(FORWARD, 8)    // 前に8ブロック移動
    builder.move(LEFT, 2)       // 左に2ブロック移動
    builder.move(BACK, 8)       // 後ろに8ブロック移動（U字の形）
    builder.tracePath(STONE)    // 移動した経路に石を配置

    // ===== TNT発射台を作る =====
    builder.move(RIGHT, 1)      // 右に1ブロック移動
    builder.mark()
    builder.place(STONE_SLAB)   // 石のハーフブロック設置
    builder.move(UP, 1)         // 上に1ブロック移動
    builder.place(TNT)          // TNTを設置

    // ===== 砲身部分を作る =====
    builder.move(RIGHT, 1)      // 右に1ブロック移動
    builder.mark()
    builder.move(FORWARD, 2)    // 前に2ブロック移動
    builder.tracePath(STONE)    // 石の道を作る

    // ===== レッドストーン回路を配置 =====
    builder.mark()
    builder.move(FORWARD, 6)    // 前に6ブロック移動
    builder.move(LEFT, 2)       // 左に2ブロック移動
    builder.move(BACK, 7)       // 後ろに7ブロック移動
    builder.tracePath(REDSTONE_WIRE)  // レッドストーンワイヤーを配置

    // 追加の配線
    builder.shift(-1, 1, -2)    // 位置を微調整
    builder.mark()
    builder.move(FORWARD, 1)
    builder.tracePath(REDSTONE_WIRE)

    // ===== リピーターとレバーを設置 =====
    builder.shift(4, -1, 0)     // 位置を調整
    builder.mark()
    builder.move(FORWARD, 2)

    // 方向に応じてリピーターの向きを変更
    if (direction === "north") {
        builder.tracePath(blocks.repeater(SOUTH, 4))  // 北向きキャノンの場合は南向きリピーター
    } else if (direction === "south") {
        builder.tracePath(blocks.repeater(NORTH, 4))  // 南向きキャノンの場合は北向きリピーター
    } else if (direction === "east") {
        builder.tracePath(blocks.repeater(WEST, 4))   // 東向きキャノンの場合は西向きリピーター
    } else if (direction === "west") {
        builder.tracePath(blocks.repeater(EAST, 4))   // 西向きキャノンの場合は東向きリピーター
    }

    builder.shift(1, 0, 1)
    builder.place(blocks.lever(BLOCK_TOP_POINTS_SOUTH_WHEN_OFF))  // レバーを設置

    // ===== 安全装置（水と石）を配置 =====
    builder.move(BACK, 1)
    builder.place(STONE)        // 石を設置
    builder.move(DOWN, 1)
    builder.place(WATER)        // 水を設置（爆発ダメージ軽減）

    // ===== 追加のTNTを配置 =====
    builder.move(BACK, 4)
    builder.mark()
    builder.move(BACK, 2)
    builder.tracePath(TNT)      // 追加のTNTを配置
}

// メインコマンド: 方向を指定してキャノンを建築
// Minecraftでは引数を数値で受け取るため、対応表を作成
player.onChat("cannon", function (directionNum: number) {
    // 数値を方向文字列に変換するマッピング
    // 1=north, 2=south, 3=east, 4=west
    let direction: string = "south"  // デフォルト

    if (directionNum === 1) {
        direction = "north"
    } else if (directionNum === 2) {
        direction = "south"
    } else if (directionNum === 3) {
        direction = "east"
    } else if (directionNum === 4) {
        direction = "west"
    } else {
        player.say("使い方: cannon <数字>")
        player.say("1=北, 2=南, 3=東, 4=西")
        return
    }


    // 建築開始のメッセージ
    player.say("TNTキャノンを " + direction + " 向きで建築します")

    // ===== ステップ1: 初期位置の設定 =====
    const baseX = -1
    const baseY = 0
    const baseZ = -10
    builder.teleportTo(pos(baseX, baseY, baseZ))

    // ===== ステップ2: 土台（3x10）を作成 =====
    player.say("土台を作成中...")
    buildPlatform(baseX, baseY, baseZ, direction)

    // ===== ステップ3: キャノン建築位置に移動 =====
    const cannonPos = getCannonStartPosition(direction, baseX, baseY, baseZ)
    builder.teleportTo(pos(cannonPos.x, cannonPos.y, cannonPos.z))
    setBuilderDirection(direction)

    // ===== ステップ4: キャノン本体を建築 =====
    player.say("キャノン本体を建築中...")
    buildCannonBody(direction)

    // 完成メッセージ
    player.say("TNTキャノンの建築が完了しました！")
    player.say("レバーを引いて発射してください")
})

// シンプルバージョン（南向き固定）
player.onChat("cannonSimple", function () {
    player.say("シンプルなTNTキャノンを建築します（南向き）")

    // 初期位置に移動
    builder.teleportTo(pos(-1, 0, -10))
    builder.face(SOUTH)

    // 土台を作成
    player.say("土台を作成中...")
    for (let i = 0; i < 10; i++) {
        for (let j = 0; j < 3; j++) {
            builder.teleportTo(pos(-1 + j, 0, -10 + i))
            builder.place(COBBLESTONE)
        }
    }

    // キャノン建築位置に移動
    builder.teleportTo(pos(-1, 1, -10))
    builder.face(SOUTH)

    // キャノン本体を建築
    player.say("キャノン本体を建築中...")
    buildCannonBody("south")

    player.say("TNTキャノンの建築が完了しました！")
})