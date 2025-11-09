# CheckerCraft - チェス盤作成プログラム
# チャットで "checkercraft" と入力して実行

def draw_chessboard(num1=0, num2=0, num3=0):
    """チェス盤を作成"""
    player.say("=== CheckerCraft 開始 ===")

    # サイズの決定とバリデーション
    if num1 == 0:
        size = 8
        player.say("デフォルトサイズ: 8x8")
    else:
        size = num1
        if size < 5 or size > 50:
            player.say("=== エラー ===")
            player.say("サイズは5から50の範囲で指定してください")
            player.say("")
            player.say("=== 使い方 ===")
            player.say("checkercraft [サイズ]")
            player.say("  サイズ: 5-50 (省略時は8)")
            player.say("")
            player.say("例:")
            player.say("  checkercraft     → 8x8")
            player.say("  checkercraft 10  → 10x10")
            player.say("  checkercraft 50  → 50x50")
            return
        else:
            player.say("サイズ: " + str(size) + "x" + str(size))

    # エージェントをテレポート（位置を固定）
    agent.teleport_to_player()
    player.say("エージェントを配置しました")
    player.say("（作成中に動いても大丈夫です）")

    # 計算: チェス盤の実サイズ
    total_blocks = size * 3
    player.say("実サイズ: " + str(total_blocks) + "x" + str(total_blocks) + "ブロック")

    # ステップ1: 整地（チャンク分割）
    player.say("ステップ1: 整地中...")

    # チャンクサイズ（30×30×10 = 9,000ブロック、上限の約1/3で安全）
    chunk_size = 30

    # チャンク数を計算
    chunks_x = int((total_blocks + chunk_size - 1) / chunk_size)
    chunks_z = int((total_blocks + chunk_size - 1) / chunk_size)
    total_chunks = chunks_x * chunks_z
    current_chunk = 0

    # チャンクごとに整地
    for cx in range(chunks_x):
        for cz in range(chunks_z):
            current_chunk = current_chunk + 1

            # チャンクの開始位置
            start_x = cx * chunk_size
            start_z = cz * chunk_size

            # チャンクの終了位置（範囲外にならないように調整）
            end_x = start_x + chunk_size - 1
            end_z = start_z + chunk_size - 1
            if end_x >= total_blocks:
                end_x = total_blocks - 1
            if end_z >= total_blocks:
                end_z = total_blocks - 1

            # 進捗表示
            player.say("整地中... " + str(current_chunk) + "/" + str(total_chunks))

            # fillコマンド実行
            cmd = "execute @e[type=agent] ~ ~ ~ fill ~" + str(start_x) + " ~1 ~" + str(start_z) + " ~" + str(end_x) + " ~10 ~" + str(end_z) + " air"
            player.execute(cmd)

    # ステップ2: チェス盤作成
    player.say("ステップ2: チェス盤作成中...")

    # 総マス数
    total_squares = size * size
    current_square = 0
    progress_step = int(total_squares / 4)  # 25%ごとに表示

    # チェス盤を描画（相対座標を使用）
    for row in range(size):
        for col in range(size):
            current_square = current_square + 1

            # 進捗表示（25%ごと）
            if progress_step > 0 and current_square % progress_step == 0:
                progress = int((current_square * 100) / total_squares)
                player.say("作成中... " + str(progress) + "%")

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
    player.say(str(size) + "x" + str(size) + "のチェス盤 (" + str(total_blocks) + "x" + str(total_blocks) + "ブロック) ができました")

# チャットコマンドを登録
player.on_chat("checkercraft", draw_chessboard)
