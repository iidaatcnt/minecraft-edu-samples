# Minecraft Education Edition MakeCode Python
# 整地ツール - 木の枝で10x10x10の範囲を整地

import math

# グローバル変数
clear_width = 10
clear_height = 10
clear_depth = 10
jump_power = 2
jump_forward = 3

def clear_terrain():
    """プレイヤーの前方10x10x10の範囲を整地する"""
    # プレイヤーの位置と向きを取得
    player_pos = player.position()

    # プレイヤーの向いている方向を取得
    # MakeCodeでは正確な回転角度が取得できないので、
    # プレイヤーの前方5ブロックの位置を中心とする
    center_pos = positions.add(player_pos, pos(0, 0, 5))

    # 整地範囲の始点と終点を計算
    # 中心から半径分広げた範囲
    half_width = clear_width // 2
    half_height = clear_height // 2
    half_depth = clear_depth // 2

    start_pos = positions.add(center_pos,
                             pos(-half_width, -half_height, -half_depth))
    end_pos = positions.add(center_pos,
                           pos(half_width, half_height, half_depth))

    # ブロックを空気に置換（整地）
    blocks.fill(AIR, start_pos, end_pos, FillOperation.REPLACE)

    # エフェクト音を鳴らす
    player.execute("playsound random.explode @s ~ ~ ~ 0.5 2.0")

    # プレイヤーを前方にテレポート（ジャンプ効果）
    new_pos = positions.add(player_pos, pos(0, jump_power, jump_forward))
    player.teleport(new_pos)

    # 完了メッセージ
    player.say("§a整地完了！ 10x10x10のブロックを除去しました")

def on_clear_command():
    """!clearコマンドで整地を実行"""
    clear_terrain()

def on_tool_command():
    """!cleartoolコマンドで木の枝を付与"""
    # プレイヤーに木の枝を1つ与える
    player.execute("give @s stick 1")
    player.say("§a整地ツール（木の枝）を付与しました！")
    player.say("§e木の枝を持った状態で '!clear' と入力すると整地します")

def on_clear_forward():
    """前方を連続整地（歩きながら整地）"""
    for i in range(5):
        clear_terrain()
        loops.pause(500)  # 0.5秒待機

def on_clear_area():
    """大規模整地（50x20x50の範囲）"""
    player_pos = player.position()
    start_pos = positions.add(player_pos, pos(-25, -5, -25))
    end_pos = positions.add(player_pos, pos(25, 15, 25))

    # 大範囲を整地
    blocks.fill(AIR, start_pos, end_pos, FillOperation.REPLACE)

    # エフェクト
    mobs.spawn(FIREWORKS_ROCKET, player_pos)
    player.say("§b大規模整地完了！ 50x20x50のブロックを除去しました")

def on_clear_tunnel():
    """トンネル掘削モード（3x3のトンネルを20ブロック掘る）"""
    player_pos = player.position()

    # 20ブロック先まで3x3のトンネルを掘る
    for distance in range(1, 21):
        tunnel_center = positions.add(player_pos, pos(0, 0, distance))

        # 3x3の範囲を空気に
        for x in range(-1, 2):
            for y in range(-1, 2):
                block_pos = positions.add(tunnel_center, pos(x, y, 0))
                blocks.place(AIR, block_pos)

        # 床にトーチを設置（5ブロックごと）
        if distance % 5 == 0:
            torch_pos = positions.add(tunnel_center, pos(0, -1, 0))
            blocks.place(TORCH, torch_pos)

    # プレイヤーをトンネルの入口にテレポート
    new_pos = positions.add(player_pos, pos(0, 0, 2))
    player.teleport(new_pos)
    player.say("§6トンネル掘削完了！ 3x3x20のトンネルを作成しました")

def on_clear_up():
    """上方向整地（天井を除去）"""
    player_pos = player.position()

    # プレイヤーの上10x10x10を整地
    start_pos = positions.add(player_pos, pos(-5, 2, -5))
    end_pos = positions.add(player_pos, pos(5, 12, 5))

    blocks.fill(AIR, start_pos, end_pos, FillOperation.REPLACE)
    player.say("§e上方整地完了！ 天井を除去しました")

def on_clear_down():
    """下方向整地（穴を掘る）"""
    player_pos = player.position()

    # プレイヤーの下10x10x10を整地
    start_pos = positions.add(player_pos, pos(-5, -12, -5))
    end_pos = positions.add(player_pos, pos(5, -2, 5))

    blocks.fill(AIR, start_pos, end_pos, FillOperation.REPLACE)

    # 安全のため、はしごを設置
    for y in range(-10, 0):
        ladder_pos = positions.add(player_pos, pos(0, y, -1))
        blocks.place(LADDER, ladder_pos)

    player.say("§c下方整地完了！ 穴を掘りました（はしご付き）")

# 初期化メッセージ
def on_start():
    """ゲーム開始時のメッセージ"""
    player.say("§b=== 整地システム起動 ===")
    player.say("§a利用可能なコマンド:")
    player.say("§e!cleartool - 木の枝を取得")
    player.say("§e!clear - 前方10x10x10を整地")
    player.say("§e!forward - 連続整地（5回）")
    player.say("§e!area - 大規模整地（50x20x50）")
    player.say("§e!tunnel - トンネル掘削（3x3x20）")
    player.say("§e!up - 上方向整地")
    player.say("§e!down - 下方向整地")

# コマンド登録
player.on_chat("cleartool", on_tool_command)
player.on_chat("clear", on_clear_command)
player.on_chat("forward", on_clear_forward)
player.on_chat("area", on_clear_area)
player.on_chat("tunnel", on_clear_tunnel)
player.on_chat("up", on_clear_up)
player.on_chat("down", on_clear_down)
player.on_chat("help", on_start)

# ゲーム開始時に自動実行
on_start()