# CheckerCraft - チェス盤作成プログラム
# チャットで "checkercraft" と入力して実行

def draw_chessboard():
    """8x8のチェス盤を作成"""
    player.say("チェス盤を作成します...")

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

            # マスを塗りつぶす（足元に作成）
            cmd = "fill ~" + str(x1) + " ~0 ~" + str(z1) + " ~" + str(x2) + " ~0 ~" + str(z2) + " " + block
            player.execute(cmd)

    player.say("完成！ 8x8のチェス盤ができました")

# チャットコマンドを登録
player.on_chat("checkercraft", draw_chessboard)
