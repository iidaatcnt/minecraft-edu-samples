# Minecraft Education Edition MakeCode Python
# fillコマンドを使った高速整地ツール

# グローバル変数
clear_size = 10  # 整地サイズ（10x10x10）

def on_clear():
    """fillコマンドで前方を整地"""
    # プレイヤーの現在位置を取得
    player_pos = player.position()
    x = player_pos.get_value(Axis.X)
    y = player_pos.get_value(Axis.Y)
    z = player_pos.get_value(Axis.Z)

    # 前方5ブロック先を中心に10x10x10の範囲を計算
    # fillコマンドで空気ブロックに置換
    player.execute(
        "fill ~-5 ~-5 ~5 ~5 ~5 ~15 air"
    )

    # ジャンプ効果（前方にテレポート）
    player.execute("tp @s ~ ~2 ~3")

    # 効果音
    player.execute("playsound random.explode @s ~ ~ ~ 0.5 2.0")

    # メッセージ
    player.say("§a整地完了！ 10x10x10のブロックを除去しました")

def on_big_clear():
    """大規模整地（30x30x30）"""
    # fillコマンドで大範囲を空気に
    player.execute(
        "fill ~-15 ~-5 ~-15 ~15 ~25 ~15 air"
    )

    # エフェクト
    player.execute("summon fireworks_rocket ~ ~ ~")
    player.say("§b大規模整地完了！ 30x30x30のブロックを除去しました")

def on_tunnel():
    """fillコマンドでトンネル掘削"""
    # 3x3のトンネルを30ブロック掘る
    player.execute(
        "fill ~-1 ~-1 ~1 ~1 ~1 ~30 air"
    )

    # トーチを5ブロックごとに設置
    for i in range(5, 31, 5):
        player.execute(f"setblock ~ ~-1 ~{i} torch")

    # プレイヤーをトンネル入口へ
    player.execute("tp @s ~ ~ ~2")
    player.say("§6トンネル完成！ 3x3x30のトンネルを掘りました")

def on_platform():
    """足場を作成（20x1x20）"""
    # 足元に石の床を作成
    player.execute(
        "fill ~-10 ~-1 ~-10 ~10 ~-1 ~10 stone"
    )
    player.say("§7足場作成完了！ 20x20の石の床を作りました")

def on_clear_up():
    """上方向の障害物を除去"""
    player.execute(
        "fill ~-5 ~2 ~-5 ~5 ~20 ~5 air"
    )
    player.say("§e上方クリア！ 障害物を除去しました")

def on_clear_down():
    """下に穴を掘る"""
    # 穴を掘る
    player.execute(
        "fill ~-3 ~-20 ~-3 ~3 ~-2 ~3 air"
    )

    # はしごを設置
    player.execute(
        "fill ~ ~-20 ~-1 ~ ~-2 ~-1 ladder"
    )
    player.say("§c穴掘り完了！ はしご付きの縦穴を作りました")

def on_wall():
    """周囲に壁を作成"""
    # 北の壁
    player.execute("fill ~-10 ~ ~-10 ~10 ~5 ~-10 stone")
    # 南の壁
    player.execute("fill ~-10 ~ ~10 ~10 ~5 ~10 stone")
    # 東の壁
    player.execute("fill ~10 ~ ~-10 ~10 ~5 ~10 stone")
    # 西の壁
    player.execute("fill ~-10 ~ ~-10 ~-10 ~5 ~10 stone")

    player.say("§8防壁完成！ 周囲に石の壁を作りました")

def on_sphere():
    """球体状に整地（近似）"""
    # 中心から段階的に小さくなる範囲を整地
    player.execute("fill ~-5 ~ ~-5 ~5 ~ ~5 air")      # y=0
    player.execute("fill ~-7 ~1 ~-7 ~7 ~1 ~7 air")    # y=1
    player.execute("fill ~-8 ~2 ~-8 ~8 ~2 ~8 air")    # y=2
    player.execute("fill ~-9 ~3 ~-9 ~9 ~3 ~9 air")    # y=3
    player.execute("fill ~-10 ~4 ~-10 ~10 ~4 ~10 air") # y=4
    player.execute("fill ~-10 ~5 ~-10 ~10 ~5 ~10 air") # y=5
    player.execute("fill ~-9 ~6 ~-9 ~9 ~6 ~9 air")    # y=6
    player.execute("fill ~-8 ~7 ~-8 ~8 ~7 ~8 air")    # y=7
    player.execute("fill ~-7 ~8 ~-7 ~7 ~8 ~7 air")    # y=8
    player.execute("fill ~-5 ~9 ~-5 ~5 ~9 ~5 air")    # y=9

    # 下半分も同様に
    player.execute("fill ~-7 ~-1 ~-7 ~7 ~-1 ~7 air")
    player.execute("fill ~-8 ~-2 ~-8 ~8 ~-2 ~8 air")
    player.execute("fill ~-9 ~-3 ~-9 ~9 ~-3 ~9 air")
    player.execute("fill ~-10 ~-4 ~-10 ~10 ~-4 ~10 air")
    player.execute("fill ~-10 ~-5 ~-10 ~10 ~-5 ~10 air")

    player.say("§d球体整地完了！ 約20x20x20の球形空間を作りました")

def on_replace():
    """水を空気に置換"""
    # 周囲の水や溶岩を除去
    player.execute(
        "fill ~-10 ~-5 ~-10 ~10 ~10 ~10 air replace water"
    )
    player.execute(
        "fill ~-10 ~-5 ~-10 ~10 ~10 ~10 air replace lava"
    )
    player.say("§3液体除去完了！ 水と溶岩を空気に置換しました")

def on_glass():
    """ガラスの箱を作成"""
    # ガラスの箱（中は空洞）
    # 床
    player.execute("fill ~-5 ~-1 ~-5 ~5 ~-1 ~5 glass")
    # 天井
    player.execute("fill ~-5 ~10 ~-5 ~5 ~10 ~5 glass")
    # 壁（4面）
    player.execute("fill ~-5 ~0 ~-5 ~5 ~9 ~-5 glass")
    player.execute("fill ~-5 ~0 ~5 ~5 ~9 ~5 glass")
    player.execute("fill ~-5 ~0 ~-5 ~-5 ~9 ~5 glass")
    player.execute("fill ~5 ~0 ~-5 ~5 ~9 ~5 glass")

    player.say("§fガラスボックス完成！ 10x10x10のガラスの箱を作りました")

def on_pyramid():
    """ピラミッド型に整地"""
    # 下から上に向かって小さくなる整地
    player.execute("fill ~-10 ~ ~-10 ~10 ~ ~10 air")
    player.execute("fill ~-9 ~1 ~-9 ~9 ~1 ~9 air")
    player.execute("fill ~-8 ~2 ~-8 ~8 ~2 ~8 air")
    player.execute("fill ~-7 ~3 ~-7 ~7 ~3 ~7 air")
    player.execute("fill ~-6 ~4 ~-6 ~6 ~4 ~6 air")
    player.execute("fill ~-5 ~5 ~-5 ~5 ~5 ~5 air")
    player.execute("fill ~-4 ~6 ~-4 ~4 ~6 ~4 air")
    player.execute("fill ~-3 ~7 ~-3 ~3 ~7 ~3 air")
    player.execute("fill ~-2 ~8 ~-2 ~2 ~8 ~2 air")
    player.execute("fill ~-1 ~9 ~-1 ~1 ~9 ~1 air")

    player.say("§6ピラミッド整地完了！ ピラミッド型の空間を作りました")

def on_help():
    """ヘルプメッセージ"""
    player.say("§b=== Fillコマンド整地システム ===")
    player.say("§a基本コマンド:")
    player.say("§e!clear - 前方10x10x10を整地")
    player.say("§e!big - 大規模整地（30x30x30）")
    player.say("§e!tunnel - トンネル掘削（3x3x30）")
    player.say("§a建築コマンド:")
    player.say("§e!platform - 足場作成（20x20）")
    player.say("§e!wall - 防壁作成")
    player.say("§e!glass - ガラスボックス作成")
    player.say("§a特殊整地:")
    player.say("§e!up - 上方向クリア")
    player.say("§e!down - 下に穴を掘る")
    player.say("§e!sphere - 球体状に整地")
    player.say("§e!pyramid - ピラミッド型整地")
    player.say("§e!replace - 水と溶岩を除去")

# コマンド登録
player.on_chat("clear", on_clear)
player.on_chat("big", on_big_clear)
player.on_chat("tunnel", on_tunnel)
player.on_chat("platform", on_platform)
player.on_chat("up", on_clear_up)
player.on_chat("down", on_clear_down)
player.on_chat("wall", on_wall)
player.on_chat("sphere", on_sphere)
player.on_chat("replace", on_replace)
player.on_chat("glass", on_glass)
player.on_chat("pyramid", on_pyramid)
player.on_chat("help", on_help)

# 起動時メッセージ
player.say("§b整地システム起動！")
player.say("§a'!help' でコマンド一覧を表示")