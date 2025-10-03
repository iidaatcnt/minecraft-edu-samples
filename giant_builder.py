# Minecraft Education Edition - 巨大キャラクタービルダー
# アニメ風の巨大キャラクターを建築するツール

import time

def build_colossal_titan():
    """超大型巨人 - 進撃の巨人風（60ブロック高）"""
    player.say("§c超大型巨人を建築開始...")

    # プレイヤーの位置を基準点に
    base_x = player.get_x()
    base_y = player.get_y()
    base_z = player.get_z()

    player.say("§eステップ1: 脚部建築中...")

    # 左脚
    player.execute(f"fill {base_x-8} {base_y} {base_z-3} {base_x-2} {base_y+20} {base_z+3} cobblestone")

    # 右脚
    player.execute(f"fill {base_x+2} {base_y} {base_z-3} {base_x+8} {base_y+20} {base_z+3} cobblestone")

    time.sleep(1)

    player.say("§eステップ2: 胴体建築中...")

    # 胴体
    player.execute(f"fill {base_x-7} {base_y+20} {base_z-4} {base_x+7} {base_y+45} {base_z+4} cobblestone")

    time.sleep(1)

    player.say("§eステップ3: 腕部建築中...")

    # 左腕（上腕）
    player.execute(f"fill {base_x-12} {base_y+35} {base_z-2} {base_x-8} {base_y+42} {base_z+2} cobblestone")
    # 左腕（前腕）
    player.execute(f"fill {base_x-16} {base_y+30} {base_z-2} {base_x-12} {base_y+37} {base_z+2} cobblestone")

    # 右腕（上腕）
    player.execute(f"fill {base_x+8} {base_y+35} {base_z-2} {base_x+12} {base_y+42} {base_z+2} cobblestone")
    # 右腕（前腕）
    player.execute(f"fill {base_x+12} {base_y+30} {base_z-2} {base_x+16} {base_y+37} {base_z+2} cobblestone")

    time.sleep(1)

    player.say("§eステップ4: 頭部・顔建築中...")

    # 頭部
    player.execute(f"fill {base_x-5} {base_y+45} {base_z-5} {base_x+5} {base_y+60} {base_z+5} cobblestone")

    # 左目
    player.execute(f"fill {base_x-3} {base_y+52} {base_z+5} {base_x-1} {base_y+54} {base_z+6} coal_block")

    # 右目
    player.execute(f"fill {base_x+1} {base_y+52} {base_z+5} {base_x+3} {base_y+54} {base_z+6} coal_block")

    # 鼻
    player.execute(f"fill {base_x-1} {base_y+49} {base_z+5} {base_x+1} {base_y+51} {base_z+7} stone")

    # 口（空洞）
    player.execute(f"fill {base_x-2} {base_y+47} {base_z+5} {base_x+2} {base_y+49} {base_z+6} air")

    # 口の枠（赤）
    player.execute(f"fill {base_x-3} {base_y+46} {base_z+5} {base_x+3} {base_y+50} {base_z+5} redstone_block")

    time.sleep(1)

    player.say("§eステップ5: 蒸気エフェクト追加中...")

    # 頭部からの蒸気
    for i in range(8):
        steam_x = base_x + (i % 3 - 1) * 2
        steam_z = base_z + (i % 2 - 1) * 2
        player.execute(f"setblock {steam_x} {base_y+60+i} {steam_z} white_wool")

    # 胴体からの蒸気
    for i in range(5):
        steam_x = base_x + (i % 5 - 2) * 2
        steam_z = base_z + (i % 3 - 1) * 2
        player.execute(f"setblock {steam_x} {base_y+45+i} {steam_z} white_wool")

    # 腕からの蒸気
    for i in range(3):
        player.execute(f"setblock {base_x-14} {base_y+40+i} {base_z} white_wool")
        player.execute(f"setblock {base_x+14} {base_y+40+i} {base_z} white_wool")

    player.say("§a超大型巨人完成！高さ60ブロック")
    player.say("§6『進撃の巨人』風の迫力ある巨人です！")

def build_mecha():
    """巨大メカ - ガンダム風（50ブロック高）"""
    player.say("§b巨大メカを建築開始...")

    base_x = player.get_x()
    base_y = player.get_y()
    base_z = player.get_z()

    player.say("§eステップ1: 脚部フレーム建築中...")

    # 左脚（メカ風）
    player.execute(f"fill {base_x-6} {base_y} {base_z-2} {base_x-3} {base_y+25} {base_z+2} iron_block")
    player.execute(f"fill {base_x-5} {base_y+1} {base_z-1} {base_x-4} {base_y+24} {base_z+1} air")  # 内部を空洞に

    # 右脚（メカ風）
    player.execute(f"fill {base_x+3} {base_y} {base_z-2} {base_x+6} {base_y+25} {base_z+2} iron_block")
    player.execute(f"fill {base_x+4} {base_y+1} {base_z-1} {base_x+5} {base_y+24} {base_z+1} air")  # 内部を空洞に

    time.sleep(1)

    player.say("§eステップ2: 胴体コックピット建築中...")

    # 胴体（装甲）
    player.execute(f"fill {base_x-8} {base_y+25} {base_z-3} {base_x+8} {base_y+40} {base_z+3} iron_block")

    # コックピット（ガラス）
    player.execute(f"fill {base_x-2} {base_y+35} {base_z+3} {base_x+2} {base_y+38} {base_z+4} glass")

    # 胸部装甲（詳細）
    player.execute(f"fill {base_x-1} {base_y+30} {base_z+3} {base_x+1} {base_y+34} {base_z+4} diamond_block")

    time.sleep(1)

    player.say("§eステップ3: 腕部武装建築中...")

    # 左腕
    player.execute(f"fill {base_x-12} {base_y+30} {base_z-1} {base_x-9} {base_y+38} {base_z+1} iron_block")
    player.execute(f"fill {base_x-15} {base_y+25} {base_z-1} {base_x-12} {base_y+32} {base_z+1} iron_block")

    # 右腕（ビームライフル装備）
    player.execute(f"fill {base_x+9} {base_y+30} {base_z-1} {base_x+12} {base_y+38} {base_z+1} iron_block")
    player.execute(f"fill {base_x+12} {base_y+25} {base_z-1} {base_x+15} {base_y+32} {base_z+1} iron_block")

    # ビームライフル
    player.execute(f"fill {base_x+15} {base_y+28} {base_z-1} {base_x+20} {base_y+30} {base_z+1} gold_block")

    time.sleep(1)

    player.say("§eステップ4: 頭部センサー建築中...")

    # 頭部
    player.execute(f"fill {base_x-4} {base_y+40} {base_z-4} {base_x+4} {base_y+50} {base_z+4} iron_block")

    # メインカメラ（目）
    player.execute(f"fill {base_x-2} {base_y+45} {base_z+4} {base_x+2} {base_y+47} {base_z+5} redstone_block")

    # アンテナ
    player.execute(f"fill {base_x-1} {base_y+50} {base_z-1} {base_x+1} {base_y+55} {base_z+1} gold_block")

    # サブカメラ
    player.execute(f"setblock {base_x-3} {base_y+46} {base_z+4} lime_concrete")
    player.execute(f"setblock {base_x+3} {base_y+46} {base_z+4} lime_concrete")

    time.sleep(1)

    player.say("§eステップ5: 推進器エフェクト追加中...")

    # バックパック推進器
    player.execute(f"fill {base_x-3} {base_y+35} {base_z-4} {base_x+3} {base_y+40} {base_z-5} iron_block")

    # 推進炎エフェクト
    for i in range(4):
        player.execute(f"setblock {base_x-2} {base_y+30-i} {base_z-6} orange_wool")
        player.execute(f"setblock {base_x} {base_y+30-i} {base_z-6} yellow_wool")
        player.execute(f"setblock {base_x+2} {base_y+30-i} {base_z-6} red_wool")

    player.say("§a巨大メカ完成！高さ55ブロック")
    player.say("§6『ガンダム』風の迫力あるメカです！")

def build_giant_robot():
    """巨大ロボット - エヴァンゲリオン風（45ブロック高）"""
    player.say("§5巨大ロボットを建築開始...")

    base_x = player.get_x()
    base_y = player.get_y()
    base_z = player.get_z()

    player.say("§eステップ1: 生体パーツ建築中...")

    # 脚部（生体風）
    player.execute(f"fill {base_x-5} {base_y} {base_z-2} {base_x-2} {base_y+22} {base_z+2} purple_concrete")
    player.execute(f"fill {base_x+2} {base_y} {base_z-2} {base_x+5} {base_y+22} {base_z+2} purple_concrete")

    # 関節部分
    player.execute(f"fill {base_x-4} {base_y+10} {base_z-1} {base_x-3} {base_y+12} {base_z+1} orange_concrete")
    player.execute(f"fill {base_x+3} {base_y+10} {base_z-1} {base_x+4} {base_y+12} {base_z+1} orange_concrete")

    time.sleep(1)

    player.say("§eステップ2: 装甲胴体建築中...")

    # 胴体（装甲と生体の混合）
    player.execute(f"fill {base_x-7} {base_y+22} {base_z-3} {base_x+7} {base_y+35} {base_z+3} purple_concrete")

    # エントリープラグ部分
    player.execute(f"fill {base_x-2} {base_y+30} {base_z-2} {base_x+2} {base_y+32} {base_z+2} orange_concrete")

    # 胸部コア
    player.execute(f"fill {base_x-1} {base_y+28} {base_z+3} {base_x+1} {base_y+30} {base_z+4} red_concrete")

    time.sleep(1)

    player.say("§eステップ3: 腕部武装建築中...")

    # 左腕
    player.execute(f"fill {base_x-11} {base_y+28} {base_z-1} {base_x-8} {base_y+33} {base_z+1} purple_concrete")
    player.execute(f"fill {base_x-14} {base_y+25} {base_z-1} {base_x-11} {base_y+30} {base_z+1} purple_concrete")

    # 右腕
    player.execute(f"fill {base_x+8} {base_y+28} {base_z-1} {base_x+11} {base_y+33} {base_z+1} purple_concrete")
    player.execute(f"fill {base_x+11} {base_y+25} {base_z-1} {base_x+14} {base_y+30} {base_z+1} purple_concrete")

    # プログレッシブナイフ（武器）
    player.execute(f"fill {base_x+14} {base_y+26} {base_z} {base_x+18} {base_y+28} {base_z} iron_block")

    time.sleep(1)

    player.say("§eステップ4: 頭部センサー建築中...")

    # 頭部
    player.execute(f"fill {base_x-3} {base_y+35} {base_z-3} {base_x+3} {base_y+45} {base_z+3} purple_concrete")

    # 目（4つ目）
    player.execute(f"setblock {base_x-2} {base_y+40} {base_z+3} lime_concrete")
    player.execute(f"setblock {base_x-1} {base_y+41} {base_z+3} lime_concrete")
    player.execute(f"setblock {base_x+1} {base_y+41} {base_z+3} lime_concrete")
    player.execute(f"setblock {base_x+2} {base_y+40} {base_z+3} lime_concrete")

    # 口部
    player.execute(f"fill {base_x-1} {base_y+38} {base_z+3} {base_x+1} {base_y+39} {base_z+4} black_concrete")

    # 角
    player.execute(f"setblock {base_x} {base_y+45} {base_z} orange_concrete")
    player.execute(f"setblock {base_x} {base_y+46} {base_z} orange_concrete")

    time.sleep(1)

    player.say("§eステップ5: ATフィールド展開中...")

    # ATフィールド（六角形のバリア）
    for angle in range(0, 360, 60):
        # 簡易的な六角形バリア
        x_offset = 12 if angle % 120 == 0 else 8
        z_offset = 12 if angle % 120 == 60 else 8

        field_x = base_x + x_offset
        field_z = base_z + z_offset

        player.execute(f"fill {field_x} {base_y+20} {field_z} {field_x} {base_y+40} {field_z} light_blue_stained_glass")

    player.say("§a巨大ロボット完成！高さ47ブロック")
    player.say("§6『エヴァンゲリオン』風の神秘的なロボです！")

def build_titan_army():
    """巨人軍団 - 複数の巨人を配置"""
    player.say("§c巨人軍団を建築開始...")

    base_x = player.get_x()
    base_y = player.get_y()
    base_z = player.get_z()

    titan_positions = [
        (base_x, base_z),
        (base_x + 30, base_z + 15),
        (base_x - 30, base_z + 15),
        (base_x + 60, base_z),
        (base_x - 60, base_z)
    ]

    for i, (x, z) in enumerate(titan_positions):
        player.say(f"§e巨人 {i+1}/5 を建築中...")

        # 簡易版巨人
        # 脚
        player.execute(f"fill {x-6} {base_y} {z-2} {x-3} {base_y+15} {z+2} cobblestone")
        player.execute(f"fill {x+3} {base_y} {z-2} {x+6} {base_y+15} {z+2} cobblestone")

        # 胴体
        player.execute(f"fill {x-5} {base_y+15} {z-3} {x+5} {base_y+30} {z+3} cobblestone")

        # 腕
        player.execute(f"fill {x-9} {base_y+25} {z-1} {x-6} {base_y+30} {z+1} cobblestone")
        player.execute(f"fill {x+6} {base_y+25} {z-1} {x+9} {base_y+30} {z+1} cobblestone")

        # 頭
        player.execute(f"fill {x-3} {base_y+30} {z-3} {x+3} {base_y+40} {z+3} cobblestone")

        # 目
        player.execute(f"setblock {x-2} {base_y+35} {z+3} coal_block")
        player.execute(f"setblock {x+2} {base_y+35} {z+3} coal_block")

        # 口
        player.execute(f"fill {x-1} {base_y+32} {z+3} {x+1} {base_y+33} {z+4} redstone_block")

        time.sleep(0.5)

    player.say("§a巨人軍団完成！5体の巨人が配置されました")

def on_help():
    """ヘルプメッセージ"""
    player.say("§b=== 巨大キャラクタービルダー ===")
    player.say("§e!titan - 超大型巨人（進撃の巨人風、60ブロック）")
    player.say("§e!mecha - 巨大メカ（ガンダム風、55ブロック）")
    player.say("§e!eva - 巨大ロボット（エヴァ風、47ブロック）")
    player.say("§e!army - 巨人軍団（5体配置）")
    player.say("§a建築には数分かかります。広い平地で実行してください！")
    player.say("§6アニメファン必見の迫力ある巨大建築！")

# コマンド登録
player.on_chat("titan", build_colossal_titan)
player.on_chat("mecha", build_mecha)
player.on_chat("eva", build_giant_robot)
player.on_chat("army", build_titan_army)
player.on_chat("giant", on_help)

# 起動メッセージ
player.say("§d╔══════════════════════════════════╗")
player.say("§d║    巨大キャラクタービルダー      ║")
player.say("§d║      アニメ風巨大建築ツール      ║")
player.say("§d╚══════════════════════════════════╝")
player.say("")
player.say("§b--- コマンド一覧 ---")
player.say("§c!titan - 超大型巨人（進撃の巨人）")
player.say("§b!mecha - 巨大メカ（ガンダム）")
player.say("§5!eva - 巨大ロボット（エヴァンゲリオン）")
player.say("§c!army - 巨人軍団（5体配置）")
player.say("§f!giant - ヘルプ表示")
player.say("")
player.say("§6注意: 広い平地で実行してください！")
player.say("§e各建築は40-60ブロックの高さになります")