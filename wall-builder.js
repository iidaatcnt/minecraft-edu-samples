player.onChat("setup", function () {
    player.say("Builder setup started")
    builder.teleportTo(player.position())
    player.say("Builder ready for wall construction")
    player.say("Position locked at: " + builder.position().x + ", " + builder.position().y + ", " + builder.position().z)
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

    // 8セクションに分けて建築
    let sections = [
        {name: "North", startAngle: 0, endAngle: 45},
        {name: "Northeast", startAngle: 45, endAngle: 90},
        {name: "East", startAngle: 90, endAngle: 135},
        {name: "Southeast", startAngle: 135, endAngle: 180},
        {name: "South", startAngle: 180, endAngle: 225},
        {name: "Southwest", startAngle: 225, endAngle: 270},
        {name: "West", startAngle: 270, endAngle: 315},
        {name: "Northwest", startAngle: 315, endAngle: 360}
    ]

    buildWallSections(centerPos, radius, height, sections, 0)
})

function buildWallSections(centerPos: Position, radius: number, height: number, sections: any[], sectionIndex: number) {
    if (sectionIndex >= sections.length) {
        player.say("Wall Area construction complete!")
        player.say("Total circumference: " + Math.round(2 * Math.PI * radius) + " blocks")
        return
    }

    let section = sections[sectionIndex]
    player.say("Building Wall Section " + (sectionIndex + 1) + "/8: " + section.name)

    // セクションの角度範囲で円弧を建築
    buildWallSection(centerPos, radius, height, section.startAngle, section.endAngle)

    loops.pause(1000)

    // 次のセクションを建築
    buildWallSections(centerPos, radius, height, sections, sectionIndex + 1)
}

function buildWallSection(centerPos: Position, radius: number, height: number, startAngle: number, endAngle: number) {
    let angleStep = 2 // 2度刻み

    for (let angle = startAngle; angle < endAngle; angle += angleStep) {
        // 角度を弧度法に変換
        let radian = angle * Math.PI / 180

        // 円周上の座標を計算
        let x = Math.round(centerPos.x + radius * Math.cos(radian))
        let z = Math.round(centerPos.z + radius * Math.sin(radian))

        // 高さ分のブロックを配置
        for (let y = 0; y < height; y++) {
            let blockPos = pos(x, centerPos.y + y, z)
            blocks.place(COBBLESTONE, blockPos)
        }

        // 内側にも1ブロック厚く建築（厚さ2ブロック）
        let innerX = Math.round(centerPos.x + (radius - 1) * Math.cos(radian))
        let innerZ = Math.round(centerPos.z + (radius - 1) * Math.sin(radian))

        for (let y = 0; y < height; y++) {
            let innerBlockPos = pos(innerX, centerPos.y + y, innerZ)
            blocks.place(COBBLESTONE, innerBlockPos)
        }
    }
}