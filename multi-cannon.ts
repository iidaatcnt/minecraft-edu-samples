// ============================================
// 複数TNTキャノン並列配置プログラム
// ============================================
// このプログラムは複数のTNTキャノンを横に並べて配置します
// 使い方: multiCannon <方向番号> <個数>
// 方向: 1=北, 2=南, 3=東, 4=西
// 個数: 1-5個まで

// ヘルパー関数: 単体の土台を作成する
function buildSinglePlatform(startX: number, startY: number, startZ: number, direction: string) {
    // 方向によって土台の向きを変える
    if (direction === "south" || direction === "north") {
        // 南北方向: 横3 x 縦10
        for (let lengthOffset = 0; lengthOffset < 10; lengthOffset++) {
            for (let widthOffset = 0; widthOffset < 3; widthOffset++) {
                let x = startX + widthOffset - 1
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
                let z = startZ + widthOffset - 1
                builder.teleportTo(pos(x, startY, z))
                builder.place(COBBLESTONE)
            }
        }
    }
}

// ヘルパー関数: 方向を設定する
function setDirection(direction: string) {
    switch(direction) {
        case "north":
            builder.face(NORTH)
            break
        case "south":
            builder.face(SOUTH)
            break
        case "east":
            builder.face(EAST)
            break
        case "west":
            builder.face(WEST)
            break
        default:
            builder.face(SOUTH)
    }
}

// ヘルパー関数: 単体のキャノン本体を建築
function buildSingleCannonBody(direction: string) {
    // 石の壁（U字型）
    builder.mark()
    builder.move(FORWARD, 8)
    builder.move(LEFT, 2)
    builder.move(BACK, 8)
    builder.tracePath(STONE)

    // TNT発射台
    builder.move(RIGHT, 1)
    builder.mark()
    builder.place(STONE_SLAB)
    builder.move(UP, 1)
    builder.place(TNT)

    // 砲身部分
    builder.move(RIGHT, 1)
    builder.mark()
    builder.move(FORWARD, 2)
    builder.tracePath(STONE)

    // レッドストーン回路
    builder.mark()
    builder.move(FORWARD, 6)
    builder.move(LEFT, 2)
    builder.move(BACK, 7)
    builder.tracePath(REDSTONE_WIRE)

    // 追加の配線
    builder.shift(-1, 1, -2)
    builder.mark()
    builder.move(FORWARD, 1)
    builder.tracePath(REDSTONE_WIRE)

    // リピーターとレバー
    builder.shift(4, -1, 0)
    builder.mark()
    builder.move(FORWARD, 2)

    // 方向に応じてリピーターの向きを変更
    if (direction === "north") {
        builder.tracePath(blocks.repeater(SOUTH, 4))
    } else if (direction === "south") {
        builder.tracePath(blocks.repeater(NORTH, 4))
    } else if (direction === "east") {
        builder.tracePath(blocks.repeater(WEST, 4))
    } else if (direction === "west") {
        builder.tracePath(blocks.repeater(EAST, 4))
    }

    builder.shift(1, 0, 1)
    builder.place(blocks.lever(BLOCK_TOP_POINTS_SOUTH_WHEN_OFF))

    // 安全装置（水と石）
    builder.move(BACK, 1)
    builder.place(STONE)
    builder.move(DOWN, 1)
    builder.place(WATER)

    // 追加のTNT
    builder.move(BACK, 4)
    builder.mark()
    builder.move(BACK, 2)
    builder.tracePath(TNT)
}

// ヘルパー関数: キャノン間の間隔を計算
function getCannonSpacing(direction: string) {
    // キャノンの幅は3ブロック、間隔は2ブロック空ける
    if (direction === "south" || direction === "north") {
        // 南北向きの場合、横に並べる（X方向に間隔）
        return { xSpacing: 5, zSpacing: 0 }  // 3(幅) + 2(間隔) = 5
    } else {
        // 東西向きの場合、縦に並べる（Z方向に間隔）
        return { xSpacing: 0, zSpacing: 5 }  // 3(幅) + 2(間隔) = 5
    }
}

// ヘルパー関数: 開始位置を計算
function calculateStartPosition(direction: string, cannonIndex: number, baseX: number, baseY: number, baseZ: number) {
    const spacing = getCannonSpacing(direction)

    // 各キャノンの基準位置を計算
    let x = baseX + (spacing.xSpacing * cannonIndex)
    let z = baseZ + (spacing.zSpacing * cannonIndex)

    // 方向に応じた建築開始位置
    switch(direction) {
        case "north":
            return { x: x, y: baseY + 1, z: z + 9 }
        case "south":
            return { x: x, y: baseY + 1, z: z }
        case "east":
            return { x: x, y: baseY + 1, z: z }
        case "west":
            return { x: x + 9, y: baseY + 1, z: z }
        default:
            return { x: x, y: baseY + 1, z: z }
    }
}

// メインコマンド: 複数キャノンを並列配置
player.onChat("multiCannon", function (directionNum: number, count: number) {
    // 方向の変換
    let direction: string = "south"

    if (directionNum === 1) {
        direction = "north"
    } else if (directionNum === 2) {
        direction = "south"
    } else if (directionNum === 3) {
        direction = "east"
    } else if (directionNum === 4) {
        direction = "west"
    } else {
        player.say("使い方: multiCannon <方向> <個数>")
        player.say("方向: 1=北, 2=南, 3=東, 4=西")
        player.say("個数: 1-5個まで")
        return
    }

    // 個数のチェック
    if (!count || count < 1) {
        count = 1
    } else if (count > 5) {
        player.say("エラー: 最大5個まで建築可能です")
        return
    }

    player.say("TNTキャノンを " + count + "個、" + direction + " 向きで並列配置します")

    // 基準座標
    const baseX = -1
    const baseY = 0
    const baseZ = -10

    // 各キャノンを建築
    for (let i = 0; i < count; i++) {
        player.say("キャノン " + (i + 1) + "/" + count + " を建築中...")

        // 土台の位置を計算
        const spacing = getCannonSpacing(direction)
        const platformX = baseX + (spacing.xSpacing * i)
        const platformZ = baseZ + (spacing.zSpacing * i)

        // 土台を作成
        buildSinglePlatform(platformX, baseY, platformZ, direction)

        // キャノン本体の位置を計算
        const cannonPos = calculateStartPosition(direction, i, baseX, baseY, baseZ)

        // キャノン本体を建築
        builder.teleportTo(pos(cannonPos.x, cannonPos.y, cannonPos.z))
        setDirection(direction)
        buildSingleCannonBody(direction)
    }

    player.say("全 " + count + " 個のTNTキャノンの建築が完了しました！")
    player.say("各レバーを引いて発射してください")
})

// 一斉発射用: レッドストーン制御線で接続
player.onChat("cannonLine", function (directionNum: number, count: number) {
    // 通常の並列配置を実行
    player.onChat("multiCannon", function() {})  // multiCannonを呼び出し

    // 方向の変換
    let direction: string = "south"

    if (directionNum === 1) {
        direction = "north"
    } else if (directionNum === 2) {
        direction = "south"
    } else if (directionNum === 3) {
        direction = "east"
    } else if (directionNum === 4) {
        direction = "west"
    } else {
        return
    }

    // 個数のチェック
    if (!count || count < 1) count = 1
    if (count > 5) count = 5

    player.say("レッドストーン制御線を追加中...")

    // 基準座標
    const baseX = -1
    const baseY = 0
    const baseZ = -10

    // レッドストーン制御線を配置
    const spacing = getCannonSpacing(direction)

    // 制御線の開始位置（最初のキャノンの後ろ）
    let controlX = baseX
    let controlY = baseY + 1
    let controlZ = baseZ - 2  // キャノンの後ろ側

    if (direction === "north") {
        controlZ = baseZ + 11
    } else if (direction === "east") {
        controlX = baseX - 2
        controlZ = baseZ
    } else if (direction === "west") {
        controlX = baseX + 11
        controlZ = baseZ
    }

    // 各キャノンを接続
    for (let i = 0; i < count; i++) {
        let wireX = controlX + (spacing.xSpacing * i)
        let wireZ = controlZ + (spacing.zSpacing * i)

        // レッドストーンワイヤーで接続
        builder.teleportTo(pos(wireX, controlY, wireZ))

        if (i < count - 1) {
            // 次のキャノンまで配線
            if (spacing.xSpacing > 0) {
                for (let j = 0; j < spacing.xSpacing; j++) {
                    builder.place(REDSTONE_WIRE)
                    builder.move(RIGHT, 1)
                }
            } else {
                for (let j = 0; j < spacing.zSpacing; j++) {
                    builder.place(REDSTONE_WIRE)
                    builder.move(FORWARD, 1)
                }
            }
        }
    }

    // マスターレバーを設置
    builder.teleportTo(pos(controlX - 2, controlY, controlZ))
    builder.place(STONE)
    builder.move(UP, 1)
    builder.place(blocks.lever(BLOCK_TOP_POINTS_SOUTH_WHEN_OFF))

    player.say("一斉発射用制御線の配置が完了しました！")
    player.say("マスターレバーで全キャノンを同時発射できます")
})

// シンプル版: 3個固定で南向き
player.onChat("triCannon", function () {
    player.say("3連装TNTキャノンを建築します（南向き）")

    const baseX = -1
    const baseY = 0
    const baseZ = -10
    const count = 3
    const direction = "south"

    for (let i = 0; i < count; i++) {
        player.say("キャノン " + (i + 1) + "/3 を建築中...")

        // 各キャノンを5ブロック間隔で配置
        const platformX = baseX + (5 * i)

        // 土台を作成
        buildSinglePlatform(platformX, baseY, baseZ, direction)

        // キャノン本体を建築
        builder.teleportTo(pos(platformX, baseY + 1, baseZ))
        setDirection(direction)
        buildSingleCannonBody(direction)
    }

    player.say("3連装TNTキャノンの建築が完了しました！")
})