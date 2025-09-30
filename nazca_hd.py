# Minecraft Education Edition - 超高精細ナスカの地上絵
# 500x500ブロックで本物のハチドリを完全再現

def draw_hummingbird_hd():
    """超高精細ハチドリ - 500×500ブロックで細部まで完全再現"""
    player.say("§6超高精細ハチドリを描画開始（500×500）...")
    player.say("§e処理に時間がかかります。しばらくお待ちください...")

    # 巨大な砂漠を作成
    player.execute("fill ~-250 ~-1 ~-250 ~250 ~-1 ~250 sandstone")

    # ナスカの線の色（赤みがかった砂）
    LINE_COLOR = "red_sandstone"

    # === 長大なくちばし（全長約150ブロック）===
    # メインライン（上側）
    for i in range(0, 150, 3):
        player.execute(f"fill ~{-250+i} ~ ~-3 ~{-247+i} ~ ~0 {LINE_COLOR}")

    # くちばしの下側ライン
    for i in range(0, 150, 3):
        player.execute(f"fill ~{-250+i} ~ ~1 ~{-247+i} ~ ~3 {LINE_COLOR}")

    # くちばしの先端（細くなる）
    player.execute(f"fill ~-250 ~ ~-1 ~-245 ~ ~1 {LINE_COLOR}")

    # === 頭部（小さく丸い）===
    # 頭の輪郭（円形に近い）
    player.execute(f"fill ~-100 ~ ~-8 ~-95 ~ ~8 {LINE_COLOR}")
    player.execute(f"fill ~-95 ~ ~-10 ~-90 ~ ~10 {LINE_COLOR}")
    player.execute(f"fill ~-90 ~ ~-12 ~-85 ~ ~12 {LINE_COLOR}")
    player.execute(f"fill ~-85 ~ ~-10 ~-80 ~ ~10 {LINE_COLOR}")
    player.execute(f"fill ~-80 ~ ~-8 ~-75 ~ ~8 {LINE_COLOR}")

    # 頭部の詳細（目のような小さな円）
    player.execute(f"fill ~-88 ~ ~-3 ~-86 ~ ~3 {LINE_COLOR}")
    player.execute(f"fill ~-89 ~ ~-2 ~-87 ~ ~-1 white_concrete")
    player.execute(f"fill ~-89 ~ ~1 ~-87 ~ ~2 white_concrete")

    # === 首（細く優雅な曲線）===
    # 首の上側ライン（なだらかなカーブ）
    for i in range(0, 30, 2):
        y_offset = int(8 - i * 0.4)  # 徐々に細くなる
        player.execute(f"fill ~{-75+i} ~ ~{y_offset-1} ~{-73+i} ~ ~{y_offset} {LINE_COLOR}")

    # 首の下側ライン
    for i in range(0, 30, 2):
        y_offset = int(-8 + i * 0.4)
        player.execute(f"fill ~{-75+i} ~ ~{y_offset} ~{-73+i} ~ ~{y_offset+1} {LINE_COLOR}")

    # === 胴体（中央が膨らむ楕円形）===
    # 胴体上部の曲線
    for i in range(0, 80, 2):
        width = int(15 + 10 * math.sin(i * 3.14159 / 80))  # サイン曲線で膨らみを表現
        player.execute(f"fill ~{-45+i} ~ ~{width-2} ~{-43+i} ~ ~{width} {LINE_COLOR}")

    # 胴体下部の曲線
    for i in range(0, 80, 2):
        width = int(-15 - 10 * math.sin(i * 3.14159 / 80))
        player.execute(f"fill ~{-45+i} ~ ~{width} ~{-43+i} ~ ~{width+2} {LINE_COLOR}")

    # 胴体の中央線（オプション）
    player.execute(f"fill ~-40 ~ ~-1 ~30 ~ ~1 {LINE_COLOR}")

    # === 上側の翼（左斜め上）- 長く優雅に伸びる ===
    # 第1セグメント（付け根から）
    for i in range(0, 40, 2):
        player.execute(f"fill ~{-30-i} ~ ~{15+i} ~{-28-i} ~ ~{18+i} {LINE_COLOR}")

    # 第2セグメント（中間部）
    for i in range(40, 100, 2):
        player.execute(f"fill ~{-30-i} ~ ~{15+i} ~{-27-i} ~ ~{17+i} {LINE_COLOR}")

    # 第3セグメント（先端部、細くなる）
    for i in range(100, 180, 3):
        player.execute(f"fill ~{-30-i} ~ ~{15+i} ~{-29-i} ~ ~{16+i} {LINE_COLOR}")

    # 羽の筋（ディテール）
    for j in range(20, 160, 20):
        player.execute(f"fill ~{-30-j} ~ ~{14+j} ~{-28-j} ~ ~{15+j} {LINE_COLOR}")

    # === 上側の翼（右斜め上）===
    # 第1セグメント
    for i in range(0, 40, 2):
        player.execute(f"fill ~{35+i} ~ ~{15+int(i*0.8)} ~{37+i} ~ ~{18+int(i*0.8)} {LINE_COLOR}")

    # 第2セグメント
    for i in range(40, 100, 2):
        player.execute(f"fill ~{35+i} ~ ~{15+int(i*0.8)} ~{38+i} ~ ~{17+int(i*0.8)} {LINE_COLOR}")

    # 第3セグメント
    for i in range(100, 180, 3):
        player.execute(f"fill ~{35+i} ~ ~{15+int(i*0.8)} ~{36+i} ~ ~{16+int(i*0.8)} {LINE_COLOR}")

    # 羽の筋
    for j in range(20, 160, 20):
        player.execute(f"fill ~{35+j} ~ ~{14+int(j*0.8)} ~{37+j} ~ ~{15+int(j*0.8)} {LINE_COLOR}")

    # === 下側の翼（左斜め下）===
    # 第1セグメント
    for i in range(0, 40, 2):
        player.execute(f"fill ~{-30-i} ~ ~{-15-i} ~{-28-i} ~ ~{-18-i} {LINE_COLOR}")

    # 第2セグメント
    for i in range(40, 100, 2):
        player.execute(f"fill ~{-30-i} ~ ~{-15-i} ~{-27-i} ~ ~{-17-i} {LINE_COLOR}")

    # 第3セグメント
    for i in range(100, 180, 3):
        player.execute(f"fill ~{-30-i} ~ ~{-15-i} ~{-29-i} ~ ~{-16-i} {LINE_COLOR}")

    # 羽の筋
    for j in range(20, 160, 20):
        player.execute(f"fill ~{-30-j} ~ ~{-14-j} ~{-28-j} ~ ~{-15-j} {LINE_COLOR}")

    # === 下側の翼（右斜め下）===
    # 第1セグメント
    for i in range(0, 40, 2):
        player.execute(f"fill ~{35+i} ~ ~{-15-int(i*0.8)} ~{37+i} ~ ~{-18-int(i*0.8)} {LINE_COLOR}")

    # 第2セグメント
    for i in range(40, 100, 2):
        player.execute(f"fill ~{35+i} ~ ~{-15-int(i*0.8)} ~{38+i} ~ ~{-17-int(i*0.8)} {LINE_COLOR}")

    # 第3セグメント
    for i in range(100, 180, 3):
        player.execute(f"fill ~{35+i} ~ ~{-15-int(i*0.8)} ~{36+i} ~ ~{-16-int(i*0.8)} {LINE_COLOR}")

    # 羽の筋
    for j in range(20, 160, 20):
        player.execute(f"fill ~{35+j} ~ ~{-14-int(j*0.8)} ~{37+j} ~ ~{-15-int(j*0.8)} {LINE_COLOR}")

    # === 尾羽（特徴的な2本に分かれた長い尾）===
    # 上側の尾羽（曲線）
    for i in range(0, 120, 3):
        curve = int(5 * math.sin(i * 3.14159 / 60))  # 波打つ尾
        player.execute(f"fill ~{35+i} ~ ~{-3+curve} ~{37+i} ~ ~{-1+curve} {LINE_COLOR}")

    # 下側の尾羽（曲線）
    for i in range(0, 120, 3):
        curve = int(-5 * math.sin(i * 3.14159 / 60))
        player.execute(f"fill ~{35+i} ~ ~{1+curve} ~{37+i} ~ ~{3+curve} {LINE_COLOR}")

    # 尾羽の先端（扇状に広がる）
    player.execute(f"fill ~155 ~ ~-8 ~160 ~ ~-6 {LINE_COLOR}")
    player.execute(f"fill ~155 ~ ~6 ~160 ~ ~8 {LINE_COLOR}")
    player.execute(f"fill ~160 ~ ~-10 ~165 ~ ~-8 {LINE_COLOR}")
    player.execute(f"fill ~160 ~ ~8 ~165 ~ ~10 {LINE_COLOR}")

    # === 翼と胴体の接続部（重要なディテール）===
    # 上翼の付け根
    player.execute(f"fill ~-30 ~ ~15 ~-25 ~ ~20 {LINE_COLOR}")
    player.execute(f"fill ~35 ~ ~15 ~40 ~ ~20 {LINE_COLOR}")

    # 下翼の付け根
    player.execute(f"fill ~-30 ~ ~-20 ~-25 ~ ~-15 {LINE_COLOR}")
    player.execute(f"fill ~35 ~ ~-20 ~40 ~ ~-15 {LINE_COLOR}")

    # === 追加ディテール：羽毛のテクスチャ ===
    # 翼に細かい線を追加（羽毛を表現）
    for wing in [1, -1]:  # 上下の翼
        for side in [1, -1]:  # 左右の翼
            for i in range(30, 150, 15):
                x_base = side * (30 + i)
                y_base = wing * (15 + int(i * 0.8))
                player.execute(f"fill ~{x_base} ~ ~{y_base} ~{x_base+2} ~ ~{y_base+1} {LINE_COLOR}")

    player.say("§a超高精細ハチドリ完成！")
    player.say("§e500×500ブロック、細部まで完全再現！")
    player.say("§b高度Y=300以上から全体をご覧ください")

# さらに高精細版（1000×1000）
def draw_hummingbird_ultra():
    """究極精細ハチドリ - 1000×1000ブロックで曲線美を完全再現"""
    player.say("§6究極精細ハチドリを描画開始（1000×1000）...")
    player.say("§c警告：処理に数分かかる場合があります")

    # 超巨大な砂漠を作成
    player.execute("fill ~-500 ~-1 ~-500 ~500 ~-1 ~500 sandstone")

    LINE_COLOR = "red_sandstone"
    ACCENT_COLOR = "orange_terracotta"  # アクセント用

    # === 超精密くちばし（300ブロック、徐々に細くなる）===
    for i in range(0, 300, 2):
        # くちばしの太さを徐々に減らす
        thickness = max(1, int(6 - i * 0.015))
        player.execute(f"fill ~{-500+i} ~ ~{-thickness} ~{-498+i} ~ ~{thickness} {LINE_COLOR}")

        # くちばしの中心線（より細い線）
        if i % 10 == 0:
            player.execute(f"fill ~{-500+i} ~ ~-1 ~{-499+i} ~ ~1 {ACCENT_COLOR}")

    # === 超精密頭部（完全な円形）===
    # 円の方程式を使用して滑らかな曲線
    radius = 25
    center_x = -200
    center_y = 0

    for angle in range(0, 360, 5):
        rad = angle * 3.14159 / 180
        x = int(center_x + radius * math.cos(rad))
        y = int(center_y + radius * math.sin(rad))
        player.execute(f"fill ~{x-2} ~ ~{y-2} ~{x+2} ~ ~{y+2} {LINE_COLOR}")

    # 目の詳細（瞳孔まで）
    player.execute(f"fill ~{center_x-5} ~ ~{center_y-5} ~{center_x+5} ~ ~{center_y+5} {LINE_COLOR}")
    player.execute(f"fill ~{center_x-3} ~ ~{center_y-3} ~{center_x+3} ~ ~{center_y+3} white_concrete")
    player.execute(f"fill ~{center_x-1} ~ ~{center_y-1} ~{center_x+1} ~ ~{center_y+1} black_concrete")

    # === 超精密首（S字カーブ）===
    for i in range(0, 80, 1):
        # S字カーブの計算
        x = -175 + i
        y_top = int(20 * math.sin(i * 3.14159 / 40))
        y_bottom = int(-20 * math.sin(i * 3.14159 / 40))

        # 上側の線
        player.execute(f"fill ~{x} ~ ~{y_top-2} ~{x+1} ~ ~{y_top} {LINE_COLOR}")
        # 下側の線
        player.execute(f"fill ~{x} ~ ~{y_bottom} ~{x+1} ~ ~{y_bottom+2} {LINE_COLOR}")

    # === 超精密胴体（楕円形で内部構造あり）===
    # 楕円の方程式で滑らかな曲線
    a = 100  # 楕円の長軸
    b = 40   # 楕円の短軸
    center_x = -50

    for angle in range(0, 360, 2):
        rad = angle * 3.14159 / 180
        x = int(center_x + a * math.cos(rad))
        y = int(b * math.sin(rad))
        player.execute(f"fill ~{x-2} ~ ~{y-2} ~{x+2} ~ ~{y+2} {LINE_COLOR}")

    # 胴体の内部構造（肋骨のような線）
    for i in range(-80, 30, 15):
        player.execute(f"fill ~{i} ~ ~-30 ~{i+2} ~ ~30 {ACCENT_COLOR}")

    # === 超精密翼（曲線と羽の詳細）===
    # 各翼を複数のセグメントに分けて描画

    # 左上翼
    for segment in range(5):
        start_angle = segment * 15
        end_angle = (segment + 1) * 15

        for angle in range(start_angle, end_angle):
            rad = angle * 3.14159 / 180
            length = 100 + segment * 60  # セグメントごとに長くなる

            for l in range(0, length, 3):
                x = int(-50 - l * math.cos(rad + 0.7))
                y = int(30 + l * math.sin(rad + 0.7))
                player.execute(f"fill ~{x-1} ~ ~{y-1} ~{x+1} ~ ~{y+1} {LINE_COLOR}")

                # 羽の筋を追加
                if l % 20 == 0 and l > 0:
                    player.execute(f"fill ~{x-3} ~ ~{y} ~{x+3} ~ ~{y+1} {ACCENT_COLOR}")

    # 右上翼（対称的に）
    for segment in range(5):
        start_angle = segment * 15
        end_angle = (segment + 1) * 15

        for angle in range(start_angle, end_angle):
            rad = angle * 3.14159 / 180
            length = 100 + segment * 60

            for l in range(0, length, 3):
                x = int(50 + l * math.cos(rad + 0.5))
                y = int(30 + l * math.sin(rad + 0.5))
                player.execute(f"fill ~{x-1} ~ ~{y-1} ~{x+1} ~ ~{y+1} {LINE_COLOR}")

                if l % 20 == 0 and l > 0:
                    player.execute(f"fill ~{x-3} ~ ~{y} ~{x+3} ~ ~{y+1} {ACCENT_COLOR}")

    # 左下翼
    for segment in range(5):
        start_angle = segment * 15
        end_angle = (segment + 1) * 15

        for angle in range(start_angle, end_angle):
            rad = angle * 3.14159 / 180
            length = 100 + segment * 60

            for l in range(0, length, 3):
                x = int(-50 - l * math.cos(rad - 0.7))
                y = int(-30 - l * math.sin(rad - 0.7))
                player.execute(f"fill ~{x-1} ~ ~{y-1} ~{x+1} ~ ~{y+1} {LINE_COLOR}")

                if l % 20 == 0 and l > 0:
                    player.execute(f"fill ~{x-3} ~ ~{y-1} ~{x+3} ~ ~{y} {ACCENT_COLOR}")

    # 右下翼
    for segment in range(5):
        start_angle = segment * 15
        end_angle = (segment + 1) * 15

        for angle in range(start_angle, end_angle):
            rad = angle * 3.14159 / 180
            length = 100 + segment * 60

            for l in range(0, length, 3):
                x = int(50 + l * math.cos(rad - 0.5))
                y = int(-30 - l * math.sin(rad - 0.5))
                player.execute(f"fill ~{x-1} ~ ~{y-1} ~{x+1} ~ ~{y+1} {LINE_COLOR}")

                if l % 20 == 0 and l > 0:
                    player.execute(f"fill ~{x-3} ~ ~{y-1} ~{x+3} ~ ~{y} {ACCENT_COLOR}")

    # === 超精密尾羽（螺旋状の美しい尾）===
    # 上側の尾羽（螺旋カーブ）
    for i in range(0, 250, 2):
        # 螺旋の方程式
        spiral_radius = 10 + i * 0.05
        angle = i * 3.14159 / 50
        x = int(50 + i)
        y = int(spiral_radius * math.sin(angle))

        player.execute(f"fill ~{x-2} ~ ~{y-2} ~{x+2} ~ ~{y} {LINE_COLOR}")

        # 羽の装飾
        if i % 30 == 0:
            player.execute(f"fill ~{x-4} ~ ~{y-1} ~{x+4} ~ ~{y+1} {ACCENT_COLOR}")

    # 下側の尾羽（対称的な螺旋）
    for i in range(0, 250, 2):
        spiral_radius = 10 + i * 0.05
        angle = -i * 3.14159 / 50
        x = int(50 + i)
        y = int(spiral_radius * math.sin(angle))

        player.execute(f"fill ~{x-2} ~ ~{y} ~{x+2} ~ ~{y+2} {LINE_COLOR}")

        if i % 30 == 0:
            player.execute(f"fill ~{x-4} ~ ~{y-1} ~{x+4} ~ ~{y+1} {ACCENT_COLOR}")

    # === 最終仕上げ：接続部の滑らかさ ===
    # 各パーツの接続を滑らかにする
    connections = [
        (-200, 0, -175, 0),  # 頭と首
        (-95, 0, -50, 0),    # 首と胴体
        (50, 0, 100, 0),     # 胴体と尾
    ]

    for x1, y1, x2, y2 in connections:
        # ベジェ曲線で滑らかな接続
        for t in range(0, 100, 5):
            t_norm = t / 100.0
            x = int(x1 * (1 - t_norm) + x2 * t_norm)
            y = int(y1 * (1 - t_norm) + y2 * t_norm)
            player.execute(f"fill ~{x-3} ~ ~{y-3} ~{x+3} ~ ~{y+3} {LINE_COLOR}")

    player.say("§a究極精細ハチドリ完成！")
    player.say("§d1000×1000ブロック、完璧な曲線美！")
    player.say("§c高度Y=500以上を強く推奨")

# mathモジュールのインポート（必要）
import math

# コマンド登録
player.on_chat("bird_hd", draw_hummingbird_hd)
player.on_chat("bird_ultra", draw_hummingbird_ultra)

# ヘルプ
def on_help_hd():
    player.say("§b=== 超高精細ナスカアート ===")
    player.say("§e!bird_hd - 500×500 高精細ハチドリ")
    player.say("§c!bird_ultra - 1000×1000 究極精細ハチドリ")
    player.say("§a細部まで完全再現！曲線も滑らか！")

player.on_chat("nazca_hd", on_help_hd)

# 起動メッセージ
player.say("§d=== 超高精細ナスカアート起動！ ===")
player.say("§e'!nazca_hd' でヘルプ表示")