// 数学定数の定義
const PI = 3.14159265359

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

    // 6方向の壁を建築（6角形）
    let directions = [
        {name: "North", xDir: 0, zDir: -1},
        {name: "Northeast", xDir: 1, zDir: -1},
        {name: "Southeast", xDir: 1, zDir: 1},
        {name: "South", xDir: 0, zDir: 1},
        {name: "Southwest", xDir: -1, zDir: 1},
        {name: "Northwest", xDir: -1, zDir: -1}
    ]

    buildWallDirections(centerPos, radius, height, directions, 0)
})

function buildWallDirections(centerPos: any, radius: number, height: number, directions: any[], dirIndex: number) {
    if (dirIndex >= directions.length) {
        player.say("Wall Area construction complete!")
        player.say("Hexagonal wall built with radius: " + radius + " blocks")
        return
    }

    let direction = directions[dirIndex]
    player.say("Building Wall Section " + (dirIndex + 1) + "/6: " + direction.name)

    // 各方向の壁セグメントを建築
    buildWallSegment(centerPos, radius, height, direction.xDir, direction.zDir)

    loops.pause(1000)

    // 次の方向を建築
    buildWallDirections(centerPos, radius, height, directions, dirIndex + 1)
}

function buildWallSegment(centerPos: any, radius: number, height: number, xDir: number, zDir: number) {
    // 6角形の各辺を正確に計算
    // 現在の方向のインデックスを求める
    let directions = [
        {xDir: 0, zDir: -1},   // North
        {xDir: 1, zDir: -1},   // Northeast
        {xDir: 1, zDir: 1},    // Southeast
        {xDir: 0, zDir: 1},    // South
        {xDir: -1, zDir: 1},   // Southwest
        {xDir: -1, zDir: -1}   // Northwest
    ]

    let currentIndex = -1
    for (let i = 0; i < directions.length; i++) {
        if (directions[i].xDir === xDir && directions[i].zDir === zDir) {
            currentIndex = i
            break
        }
    }

    if (currentIndex === -1) return

    // 正六角形の頂点を計算（60度間隔で6つの頂点）
    let currentAngle = currentIndex * 60 * PI / 180  // 度をラジアンに変換
    let nextAngle = ((currentIndex + 1) % 6) * 60 * PI / 180

    // 正六角形の頂点座標を計算
    let startX = Math.round(radius * Math.sin(currentAngle))
    let startZ = Math.round(radius * -Math.cos(currentAngle))  // Minecraftでは-Z方向が北
    let endX = Math.round(radius * Math.sin(nextAngle))
    let endZ = Math.round(radius * -Math.cos(nextAngle))

    // 辺の長さを計算
    let deltaX = endX - startX
    let deltaZ = endZ - startZ
    let segmentLength = Math.max(Math.abs(deltaX), Math.abs(deltaZ))

    // 辺を描画
    for (let i = 0; i <= segmentLength; i++) {
        let t = segmentLength > 0 ? i / segmentLength : 0
        let wallX = startX + deltaX * t
        let wallZ = startZ + deltaZ * t

        // 高さ分のブロックを配置
        for (let y = 0; y < height; y++) {
            let wallPos = positions.add(centerPos, pos(Math.round(wallX), y, Math.round(wallZ)))
            blocks.place(COBBLESTONE, wallPos)
        }
    }
}