player.onChat("setup", function () {
    player.say("Builder setup started")
    builder.teleportTo(player.position())
    player.say("Builder ready for wall construction")
    player.say("Position locked - ready to build!")
})

player.onChat("wall", function (num1, num2) {
    // パラメータの処理
    let radius = num1 || 30
    let height = num2 || 5

    // 範囲チェック
    if (radius < 10 || radius > 50) {
        player.say("Error: Radius must be between 10-50 blocks")
        return
    }

    if (height < 3 || height > 20) {
        player.say("Error: Height must be between 3-20 blocks")
        return
    }

    player.say("Building Wall Area - Radius: " + radius + ", Height: " + height)

    // エージェントの位置を中心点として固定
    let centerPos = builder.position()

    // 8方向の壁を建築（8角形近似）
    let directions = [
        {name: "North", xDir: 0, zDir: -1},
        {name: "Northeast", xDir: 1, zDir: -1},
        {name: "East", xDir: 1, zDir: 0},
        {name: "Southeast", xDir: 1, zDir: 1},
        {name: "South", xDir: 0, zDir: 1},
        {name: "Southwest", xDir: -1, zDir: 1},
        {name: "West", xDir: -1, zDir: 0},
        {name: "Northwest", xDir: -1, zDir: -1}
    ]

    buildWallDirections(centerPos, radius, height, directions, 0)
})

function buildWallDirections(centerPos: any, radius: number, height: number, directions: any[], dirIndex: number) {
    if (dirIndex >= directions.length) {
        player.say("Wall Area construction complete!")
        player.say("Octagonal wall built with radius: " + radius + " blocks")
        return
    }

    let direction = directions[dirIndex]
    player.say("Building Wall Section " + (dirIndex + 1) + "/8: " + direction.name)

    // 各方向の壁セグメントを建築
    buildWallSegment(centerPos, radius, height, direction.xDir, direction.zDir)

    loops.pause(1000)

    // 次の方向を建築
    buildWallDirections(centerPos, radius, height, directions, dirIndex + 1)
}

function buildWallSegment(centerPos: any, radius: number, height: number, xDir: number, zDir: number) {
    // 8角形の辺の長さを計算
    let isDiagonal = (xDir != 0 && zDir != 0)
    let segmentLength = isDiagonal ? Math.round(radius * 0.4) : Math.round(radius * 0.6)

    for (let i = -segmentLength; i <= segmentLength; i++) {
        // 壁の位置を計算
        let wallX, wallZ

        if (isDiagonal) {
            // 対角線方向：両方向に移動
            wallX = xDir * radius + (zDir * i * 0.3)
            wallZ = zDir * radius + (xDir * i * 0.3)
        } else {
            // 直交方向：垂直に移動
            wallX = xDir * radius + (zDir * i)
            wallZ = zDir * radius + (xDir * i)
        }

        // 高さ分のブロックを配置
        for (let y = 0; y < height; y++) {
            let wallPos = positions.add(centerPos, pos(Math.round(wallX), y, Math.round(wallZ)))
            blocks.place(COBBLESTONE, wallPos)
        }
    }
}