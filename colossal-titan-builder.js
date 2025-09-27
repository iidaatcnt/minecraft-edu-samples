player.onChat("setup_colossal", function () {
    player.say("Builder setup started")
    builder.teleportTo(player.position())
    builder.move(FORWARD, 15)
    builder.move(DOWN, 1)
    player.say("Builder ready")
})

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

player.onChat("colossal", function () {
    player.say("Building Colossal Titan")
    basePos = builder.position()

    player.say("Step 1: Building legs")

    leftLegStart = positions.add(basePos, pos(-8, 0, -3))
    leftLegEnd = positions.add(basePos, pos(-2, 20, 3))
    blocks.fill(COBBLESTONE, leftLegStart, leftLegEnd, FillOperation.Replace)

    rightLegStart = positions.add(basePos, pos(2, 0, -3))
    rightLegEnd = positions.add(basePos, pos(8, 20, 3))
    blocks.fill(COBBLESTONE, rightLegStart, rightLegEnd, FillOperation.Replace)

    loops.pause(2000)

    player.say("Step 2: Building body")

    bodyStart = positions.add(basePos, pos(-7, 20, -4))
    bodyEnd = positions.add(basePos, pos(7, 45, 4))
    blocks.fill(COBBLESTONE, bodyStart, bodyEnd, FillOperation.Replace)

    loops.pause(2000)

    player.say("Step 3: Building arms")

    leftArmStart = positions.add(basePos, pos(-12, 35, -2))
    leftArmEnd = positions.add(basePos, pos(-8, 42, 2))
    blocks.fill(COBBLESTONE, leftArmStart, leftArmEnd, FillOperation.Replace)

    leftArmExtStart = positions.add(basePos, pos(-16, 30, -2))
    leftArmExtEnd = positions.add(basePos, pos(-12, 37, 2))
    blocks.fill(COBBLESTONE, leftArmExtStart, leftArmExtEnd, FillOperation.Replace)

    rightArmStart = positions.add(basePos, pos(8, 35, -2))
    rightArmEnd = positions.add(basePos, pos(12, 42, 2))
    blocks.fill(COBBLESTONE, rightArmStart, rightArmEnd, FillOperation.Replace)

    rightArmExtStart = positions.add(basePos, pos(12, 30, -2))
    rightArmExtEnd = positions.add(basePos, pos(16, 37, 2))
    blocks.fill(COBBLESTONE, rightArmExtStart, rightArmExtEnd, FillOperation.Replace)

    loops.pause(2000)

    player.say("Step 4: Building head and face")

    headStart = positions.add(basePos, pos(-5, 45, -5))
    headEnd = positions.add(basePos, pos(5, 60, 5))
    blocks.fill(COBBLESTONE, headStart, headEnd, FillOperation.Replace)

    leftEyeStart = positions.add(basePos, pos(-3, 52, 5))
    leftEyeEnd = positions.add(basePos, pos(-1, 54, 6))
    blocks.fill(COAL_BLOCK, leftEyeStart, leftEyeEnd, FillOperation.Replace)

    rightEyeStart = positions.add(basePos, pos(1, 52, 5))
    rightEyeEnd = positions.add(basePos, pos(3, 54, 6))
    blocks.fill(COAL_BLOCK, rightEyeStart, rightEyeEnd, FillOperation.Replace)

    noseStart = positions.add(basePos, pos(-1, 49, 5))
    noseEnd = positions.add(basePos, pos(1, 51, 7))
    blocks.fill(STONE, noseStart, noseEnd, FillOperation.Replace)

    mouthStart = positions.add(basePos, pos(-2, 47, 5))
    mouthEnd = positions.add(basePos, pos(2, 49, 6))
    blocks.fill(AIR, mouthStart, mouthEnd, FillOperation.Replace)

    mouthFrameStart = positions.add(basePos, pos(-3, 46, 5))
    mouthFrameEnd = positions.add(basePos, pos(3, 50, 5))
    blocks.fill(REDSTONE_BLOCK, mouthFrameStart, mouthFrameEnd, FillOperation.Replace)

    loops.pause(2000)

    player.say("Step 5: Adding steam")

    for (let i = 0; i < steamCount; i++) {
        steamX = Math.floor(Math.random() * 10) - 5
        steamZ = Math.floor(Math.random() * 10) - 5
        steamPos = positions.add(basePos, pos(steamX, 60 + i, steamZ))
        blocks.place(POLISHED_ANDESITE, steamPos)
    }

    for (let i = 0; i < bodySteam; i++) {
        steamX = Math.floor(Math.random() * 14) - 7
        steamZ = Math.floor(Math.random() * 8) - 4
        steamPos = positions.add(basePos, pos(steamX, 45 + i, steamZ))
        blocks.place(POLISHED_ANDESITE, steamPos)
    }

    for (let i = 0; i < armSteam; i++) {
        leftArmSteam = positions.add(basePos, pos(-14, 40 + i, 0))
        rightArmSteam = positions.add(basePos, pos(14, 40 + i, 0))
        blocks.place(POLISHED_ANDESITE, leftArmSteam)
        blocks.place(POLISHED_ANDESITE, rightArmSteam)
    }

    player.say("Colossal Titan complete")
    player.say("Height 60 blocks")
})

player.onChat("army", function (num1) {
    // 引数の処理（デフォルト値5、最大30）
    let count = num1 || 5

    // 最大値チェック
    if (count > 30) {
        player.say("Error: Maximum titan count is 30")
        player.say("Too many titans can crash the game!")
        return
    }

    if (count < 1) {
        player.say("Error: Minimum titan count is 1")
        return
    }

    player.say("Building Titan Army (" + count + " titans)")

    // setup_colossalで設定した高さを使用
    armyBasePos = builder.position()

    for (let i = 0; i < count; i++) {
        player.say("Building titan " + (i + 1))

        xOffset = (i - Math.floor(count / 2)) * spacing
        zOffset = (i % 2 == 0) ? 0 : staggerOffset

        titanPos = positions.add(armyBasePos, pos(xOffset, 0, zOffset))

        buildSimpleTitan(titanPos)

        loops.pause(1000)
    }

    player.say("Titan Army complete (" + count + " titans built)")
})

function buildSimpleTitan(titanBase: Position) {
    legs1 = positions.add(titanBase, pos(-8, 0, -3))
    legs2 = positions.add(titanBase, pos(-2, 20, 3))
    blocks.fill(COBBLESTONE, legs1, legs2, FillOperation.Replace)

    legs3 = positions.add(titanBase, pos(2, 0, -3))
    legs4 = positions.add(titanBase, pos(8, 20, 3))
    blocks.fill(COBBLESTONE, legs3, legs4, FillOperation.Replace)

    body1 = positions.add(titanBase, pos(-7, 20, -4))
    body2 = positions.add(titanBase, pos(7, 45, 4))
    blocks.fill(COBBLESTONE, body1, body2, FillOperation.Replace)

    arm1 = positions.add(titanBase, pos(-12, 35, -2))
    arm2 = positions.add(titanBase, pos(-8, 42, 2))
    blocks.fill(COBBLESTONE, arm1, arm2, FillOperation.Replace)

    arm3 = positions.add(titanBase, pos(-16, 30, -2))
    arm4 = positions.add(titanBase, pos(-12, 37, 2))
    blocks.fill(COBBLESTONE, arm3, arm4, FillOperation.Replace)

    arm5 = positions.add(titanBase, pos(8, 35, -2))
    arm6 = positions.add(titanBase, pos(12, 42, 2))
    blocks.fill(COBBLESTONE, arm5, arm6, FillOperation.Replace)

    arm7 = positions.add(titanBase, pos(12, 30, -2))
    arm8 = positions.add(titanBase, pos(16, 37, 2))
    blocks.fill(COBBLESTONE, arm7, arm8, FillOperation.Replace)

    head1 = positions.add(titanBase, pos(-5, 45, -5))
    head2 = positions.add(titanBase, pos(5, 60, 5))
    blocks.fill(COBBLESTONE, head1, head2, FillOperation.Replace)

    eye1 = positions.add(titanBase, pos(-3, 52, 5))
    eye2 = positions.add(titanBase, pos(-1, 54, 6))
    blocks.fill(COAL_BLOCK, eye1, eye2, FillOperation.Replace)

    eye3 = positions.add(titanBase, pos(1, 52, 5))
    eye4 = positions.add(titanBase, pos(3, 54, 6))
    blocks.fill(COAL_BLOCK, eye3, eye4, FillOperation.Replace)

    nose1 = positions.add(titanBase, pos(-1, 49, 5))
    nose2 = positions.add(titanBase, pos(1, 51, 7))
    blocks.fill(STONE, nose1, nose2, FillOperation.Replace)

    mouth1 = positions.add(titanBase, pos(-2, 47, 5))
    mouth2 = positions.add(titanBase, pos(2, 49, 6))
    blocks.fill(AIR, mouth1, mouth2, FillOperation.Replace)

    mouthFrame1 = positions.add(titanBase, pos(-3, 46, 5))
    mouthFrame2 = positions.add(titanBase, pos(3, 50, 5))
    blocks.fill(REDSTONE_BLOCK, mouthFrame1, mouthFrame2, FillOperation.Replace)

    for (let i = 0; i < quickSteam; i++) {
        steam1 = positions.add(titanBase, pos(0, 60 + i, 0))
        steam2 = positions.add(titanBase, pos(-10, 40 + i, 0))
        steam3 = positions.add(titanBase, pos(10, 40 + i, 0))
        blocks.place(POLISHED_ANDESITE, steam1)
        blocks.place(POLISHED_ANDESITE, steam2)
        blocks.place(POLISHED_ANDESITE, steam3)
    }
}

let rightArmSteam: Position = null
let leftArmSteam: Position = null
let steamPos: Position = null
let mouthFrameEnd: Position = null
let mouthFrameStart: Position = null
let mouthEnd: Position = null
let mouthStart: Position = null
let noseEnd: Position = null
let noseStart: Position = null
let rightEyeEnd: Position = null
let rightEyeStart: Position = null
let leftEyeEnd: Position = null
let leftEyeStart: Position = null
let headEnd: Position = null
let headStart: Position = null
let rightArmExtEnd: Position = null
let rightArmExtStart: Position = null
let rightArmEnd: Position = null
let rightArmStart: Position = null
let leftArmExtEnd: Position = null
let leftArmExtStart: Position = null
let leftArmEnd: Position = null
let leftArmStart: Position = null
let bodyEnd: Position = null
let bodyStart: Position = null
let rightLegEnd: Position = null
let rightLegStart: Position = null
let leftLegEnd: Position = null
let leftLegStart: Position = null
let basePos: Position = null
let titanPos: Position = null
let armyBasePos: Position = null
let steam3: Position = null
let steam2: Position = null
let steam1: Position = null
let mouthFrame2: Position = null
let mouthFrame1: Position = null
let mouth2: Position = null
let mouth1: Position = null
let nose2: Position = null
let nose1: Position = null
let eye4: Position = null
let eye3: Position = null
let eye2: Position = null
let eye1: Position = null
let head2: Position = null
let head1: Position = null
let arm8: Position = null
let arm7: Position = null
let arm6: Position = null
let arm5: Position = null
let arm4: Position = null
let arm3: Position = null
let arm2: Position = null
let arm1: Position = null
let body2: Position = null
let body1: Position = null
let legs4: Position = null
let legs3: Position = null
let legs2: Position = null
let legs1: Position = null
let steamX = 0
let steamZ = 0
let zOffset = 0
let xOffset = 0
let steamCount = 8
let bodySteam = 5
let armSteam = 3
// titanCount is now passed as parameter to army command
let spacing = 25
let staggerOffset = 12
let quickSteam = 3