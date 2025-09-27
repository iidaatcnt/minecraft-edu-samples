player.onChat("cannon", function () {
    builder.teleportTo(pos(-1, 0, -10))
    builder.face(SOUTH)

    // キャノンの真下に3x10のブロック層を作成（水漏れ防止）
    for (let i = 0; i < 10; i++) {
        for (let j = 0; j < 3; j++) {
            builder.teleportTo(pos(-1 + j, 0, -10 + i))
            builder.place(COBBLESTONE)
        }
    }

    // キャノン建築位置に移動
    builder.teleportTo(pos(-1, 1, -10))
    builder.face(SOUTH)

    // 大砲の基礎構造を作成
    builder.mark()
    builder.move(FORWARD, 8)
    builder.move(LEFT, 2)
    builder.move(BACK, 8)
    builder.tracePath(STONE)
    builder.move(RIGHT, 1)
    builder.mark()
    builder.place(STONE_SLAB)
    builder.move(UP, 1)
    builder.place(TNT)
    builder.move(RIGHT, 1)
    builder.mark()
    builder.move(FORWARD, 2)
    builder.tracePath(STONE)
    builder.mark()
    builder.move(FORWARD, 6)
    builder.move(LEFT, 2)
    builder.move(BACK, 7)
    builder.tracePath(REDSTONE_WIRE)
    builder.shift(-1, 1, -2)
    builder.mark()
    builder.move(FORWARD, 1)
    builder.tracePath(REDSTONE_WIRE)
    builder.shift(4, -1, 0)
    builder.mark()
    builder.move(FORWARD, 2)
    builder.tracePath(blocks.repeater(NORTH, 4))
    builder.shift(1, 0, 1)
    builder.place(blocks.lever(BLOCK_TOP_POINTS_SOUTH_WHEN_OFF))
    builder.move(BACK, 1)
    builder.place(STONE)
    builder.move(DOWN, 1)
    builder.place(WATER)
    builder.move(BACK, 4)
    builder.mark()
    builder.move(BACK, 2)
    builder.tracePath(TNT)
})