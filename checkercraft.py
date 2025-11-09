# CheckerCraft - チェス盤作成プログラム
# チャットで "checkercraft" と入力して実行

def draw_chessboard():
    """8x8のチェス盤を作成"""
    player.say("=== CheckerCraft 開始 ===")

    # エージェントをテレポート（位置を固定）
    agent.teleport_to_player()
    player.say("エージェントを配置しました")
    player.say("（作成中に動いても大丈夫です）")

    # ステップ1: 整地
    player.say("ステップ1: 整地中... (24x24x10ブロック)")
    player.execute("execute @e[type=agent] ~ ~ ~ fill ~0 ~1 ~0 ~23 ~10 ~23 air")

    # ステップ2: チェス盤作成
    player.say("ステップ2: チェス盤作成中...")

    # 8x8のチェス盤を描画（相対座標を使用）
    for row in range(8):
        for col in range(8):
            # 白と黒を交互に配置
            if (row + col) % 2 == 0:
                block = "white_concrete"
            else:
                block = "black_concrete"

            # 各マスは3x3ブロック
            # 相対座標で指定（プレイヤーの位置から）
            x1 = col * 3
            z1 = row * 3
            x2 = x1 + 2
            z2 = z1 + 2

            # マスを塗りつぶす（エージェントの位置を基準に作成）
            cmd = "execute @e[type=agent] ~ ~ ~ fill ~" + str(x1) + " ~0 ~" + str(z1) + " ~" + str(x2) + " ~0 ~" + str(z2) + " " + block
            player.execute(cmd)

    # ステップ3: 完成
    player.say("ステップ3: 完成！")
    player.say("8x8のチェス盤 (24x24ブロック) ができました")

# チャットコマンドを登録
player.on_chat("checkercraft", draw_chessboard)
