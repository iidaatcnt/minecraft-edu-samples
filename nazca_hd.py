# Minecraft Education Edition - 超高精細ナスカの地上絵
# 500x500ブロックで本物のハチドリを完全再現（mathモジュール不使用）

def draw_hummingbird_hd():
    """超高精細ハチドリ - 500×500ブロックで細部まで完全再現"""
    player.say("§6超高精細ハチドリを描画開始（500×500）...")
    player.say("§e処理に時間がかかります。しばらくお待ちください...")

    # 巨大な砂漠を作成
    player.execute("fill ~-250 ~-1 ~-250 ~250 ~-1 ~250 sandstone")

    # ナスカの線の色
    LINE_COLOR = "red_sandstone"
    ACCENT_COLOR = "orange_terracotta"

    # === 長大なくちばし（全長約150ブロック、徐々に細くなる）===
    # メインライン（上側）
    for i in range(0, 150, 2):
        # くちばしの太さを徐々に減らす（線形変化）
        thickness = max(1, 6 - i // 25)
        player.execute(f"fill ~{-250+i} ~ ~{-thickness} ~{-248+i} ~ ~{thickness} {LINE_COLOR}")

    # くちばしの先端（最も細い部分）
    player.execute(f"fill ~-250 ~ ~-1 ~-245 ~ ~1 {LINE_COLOR}")

    # === 頭部（大きな円形、段階的に描画）===
    # 円を近似的に描画（8角形を基本に）
    center_x = -100
    center_y = 0
    radius = 15

    # 上半分の円弧
    for i in range(-radius, radius + 1, 2):
        # 円の方程式を近似（y = sqrt(r^2 - x^2)）
        y_offset = int((radius * radius - i * i) ** 0.5)
        player.execute(f"fill ~{center_x + i - 1} ~ ~{center_y + y_offset - 1} ~{center_x + i + 1} ~ ~{center_y + y_offset + 1} {LINE_COLOR}")
        player.execute(f"fill ~{center_x + i - 1} ~ ~{center_y - y_offset - 1} ~{center_x + i + 1} ~ ~{center_y - y_offset + 1} {LINE_COLOR}")

    # 左右の円弧
    for i in range(-radius, radius + 1, 2):
        x_offset = int((radius * radius - i * i) ** 0.5)
        player.execute(f"fill ~{center_x + x_offset - 1} ~ ~{center_y + i - 1} ~{center_x + x_offset + 1} ~ ~{center_y + i + 1} {LINE_COLOR}")
        player.execute(f"fill ~{center_x - x_offset - 1} ~ ~{center_y + i - 1} ~{center_x - x_offset + 1} ~ ~{center_y + i + 1} {LINE_COLOR}")

    # 目の詳細
    player.execute(f"fill ~{center_x - 3} ~ ~{center_y - 3} ~{center_x + 3} ~ ~{center_y + 3} white_concrete")
    player.execute(f"fill ~{center_x - 1} ~ ~{center_y - 1} ~{center_x + 1} ~ ~{center_y + 1} black_concrete")

    # === 首（滑らかなS字カーブを近似）===
    # S字カーブを区分線形で近似
    neck_points = [
        (-85, 12), (-80, 10), (-75, 8), (-70, 5), (-65, 2),
        (-60, 0), (-55, -2), (-50, -5), (-45, -8), (-40, -10)
    ]

    # 上側の首ライン
    for i in range(len(neck_points) - 1):
        x1, y1 = neck_points[i]
        x2, y2 = neck_points[i + 1]
        # 2点間を線で結ぶ
        for j in range(0, 10):
            x = x1 + (x2 - x1) * j // 10
            y = y1 + (y2 - y1) * j // 10
            player.execute(f"fill ~{x - 1} ~ ~{y - 1} ~{x + 1} ~ ~{y + 1} {LINE_COLOR}")

    # 下側の首ライン（対称）
    for i in range(len(neck_points) - 1):
        x1, y1 = neck_points[i]
        x2, y2 = neck_points[i + 1]
        for j in range(0, 10):
            x = x1 + (x2 - x1) * j // 10
            y = -y1 - (y2 - y1) * j // 10  # Y座標を反転
            player.execute(f"fill ~{x - 1} ~ ~{y - 1} ~{x + 1} ~ ~{y + 1} {LINE_COLOR}")

    # === 胴体（楕円形を近似）===
    # 楕円を区分的に描画
    body_center_x = -10
    a = 50  # 長軸
    b = 20  # 短軸

    # 楕円の上下部分
    for x in range(-a, a + 1, 3):
        # 楕円の方程式を近似
        y_squared = b * b * (1 - (x * x) // (a * a))
        if y_squared >= 0:
            y = int(y_squared ** 0.5)
            player.execute(f"fill ~{body_center_x + x - 1} ~ ~{y - 1} ~{body_center_x + x + 1} ~ ~{y + 1} {LINE_COLOR}")
            player.execute(f"fill ~{body_center_x + x - 1} ~ ~{-y - 1} ~{body_center_x + x + 1} ~ ~{-y + 1} {LINE_COLOR}")

    # 胴体の中央線
    player.execute(f"fill ~{body_center_x - a} ~ ~-1 ~{body_center_x + a} ~ ~1 {LINE_COLOR}")

    # === 翼（多角形で近似した長い翼）===

    # 左上翼（多段階の線で構成）
    wing_points_lu = [
        (-20, 20), (-35, 35), (-55, 55), (-80, 80), (-110, 110), (-150, 150), (-200, 200)
    ]

    for i in range(len(wing_points_lu) - 1):
        x1, y1 = wing_points_lu[i]
        x2, y2 = wing_points_lu[i + 1]

        # 翼の太さを段階的に変更
        thickness = max(2, 8 - i * 2)

        for j in range(0, 20):
            x = x1 + (x2 - x1) * j // 20
            y = y1 + (y2 - y1) * j // 20
            player.execute(f"fill ~{x - thickness} ~ ~{y - thickness} ~{x + thickness} ~ ~{y + thickness} {LINE_COLOR}")

    # 右上翼
    wing_points_ru = [
        (30, 20), (50, 40), (75, 65), (105, 95), (140, 130), (180, 170), (220, 210)
    ]

    for i in range(len(wing_points_ru) - 1):
        x1, y1 = wing_points_ru[i]
        x2, y2 = wing_points_ru[i + 1]

        thickness = max(2, 8 - i * 2)

        for j in range(0, 20):
            x = x1 + (x2 - x1) * j // 20
            y = y1 + (y2 - y1) * j // 20
            player.execute(f"fill ~{x - thickness} ~ ~{y - thickness} ~{x + thickness} ~ ~{y + thickness} {LINE_COLOR}")

    # 左下翼
    wing_points_ld = [
        (-20, -20), (-35, -35), (-55, -55), (-80, -80), (-110, -110), (-150, -150), (-200, -200)
    ]

    for i in range(len(wing_points_ld) - 1):
        x1, y1 = wing_points_ld[i]
        x2, y2 = wing_points_ld[i + 1]

        thickness = max(2, 8 - i * 2)

        for j in range(0, 20):
            x = x1 + (x2 - x1) * j // 20
            y = y1 + (y2 - y1) * j // 20
            player.execute(f"fill ~{x - thickness} ~ ~{y - thickness} ~{x + thickness} ~ ~{y + thickness} {LINE_COLOR}")

    # 右下翼
    wing_points_rd = [
        (30, -20), (50, -40), (75, -65), (105, -95), (140, -130), (180, -170), (220, -210)
    ]

    for i in range(len(wing_points_rd) - 1):
        x1, y1 = wing_points_rd[i]
        x2, y2 = wing_points_rd[i + 1]

        thickness = max(2, 8 - i * 2)

        for j in range(0, 20):
            x = x1 + (x2 - x1) * j // 20
            y = y1 + (y2 - y1) * j // 20
            player.execute(f"fill ~{x - thickness} ~ ~{y - thickness} ~{x + thickness} ~ ~{y + thickness} {LINE_COLOR}")

    # === 羽の筋（詳細）===
    # 各翼に細かい筋を追加
    for wing_set in [wing_points_lu, wing_points_ru, wing_points_ld, wing_points_rd]:
        for i in range(len(wing_set)):
            x, y = wing_set[i]
            if i % 2 == 0:  # 2つおきに筋を描画
                # 翼に垂直な短い線
                if y > 0:  # 上翼
                    player.execute(f"fill ~{x - 5} ~ ~{y} ~{x + 5} ~ ~{y + 2} {ACCENT_COLOR}")
                else:  # 下翼
                    player.execute(f"fill ~{x - 5} ~ ~{y - 2} ~{x + 5} ~ ~{y} {ACCENT_COLOR}")

    # === 尾羽（2本に分かれた波打つ尾）===
    # 上側の尾羽（波状カーブを近似）
    tail_upper = []
    for i in range(0, 120, 4):
        x = 40 + i
        # 簡単な波形を作る（周期的な上下）
        wave_cycle = i % 40
        if wave_cycle < 10:
            y = i // 20
        elif wave_cycle < 20:
            y = 5 - i // 20
        elif wave_cycle < 30:
            y = -(i // 20)
        else:
            y = -5 + i // 20
        tail_upper.append((x, y))

    # 上側尾羽を描画
    for i in range(len(tail_upper) - 1):
        x1, y1 = tail_upper[i]
        x2, y2 = tail_upper[i + 1]
        for j in range(0, 8):
            x = x1 + (x2 - x1) * j // 8
            y = y1 + (y2 - y1) * j // 8
            player.execute(f"fill ~{x - 2} ~ ~{y - 1} ~{x + 2} ~ ~{y + 1} {LINE_COLOR}")

    # 下側の尾羽（対称的な波）
    tail_lower = []
    for i in range(0, 120, 4):
        x = 40 + i
        wave_cycle = i % 40
        if wave_cycle < 10:
            y = -(i // 20)
        elif wave_cycle < 20:
            y = -5 + i // 20
        elif wave_cycle < 30:
            y = i // 20
        else:
            y = 5 - i // 20
        tail_lower.append((x, y))

    # 下側尾羽を描画
    for i in range(len(tail_lower) - 1):
        x1, y1 = tail_lower[i]
        x2, y2 = tail_lower[i + 1]
        for j in range(0, 8):
            x = x1 + (x2 - x1) * j // 8
            y = y1 + (y2 - y1) * j // 8
            player.execute(f"fill ~{x - 2} ~ ~{y - 1} ~{x + 2} ~ ~{y + 1} {LINE_COLOR}")

    # 尾羽の先端装飾
    player.execute(f"fill ~155 ~ ~-10 ~165 ~ ~-5 {ACCENT_COLOR}")
    player.execute(f"fill ~155 ~ ~5 ~165 ~ ~10 {ACCENT_COLOR}")

    # === 翼と胴体の接続部===
    # 各翼の付け根を太くして接続を強調
    player.execute(f"fill ~-25 ~ ~15 ~-15 ~ ~25 {LINE_COLOR}")  # 左上翼の付け根
    player.execute(f"fill ~25 ~ ~15 ~35 ~ ~25 {LINE_COLOR}")    # 右上翼の付け根
    player.execute(f"fill ~-25 ~ ~-25 ~-15 ~ ~-15 {LINE_COLOR}") # 左下翼の付け根
    player.execute(f"fill ~25 ~ ~-25 ~35 ~ ~-15 {LINE_COLOR}")   # 右下翼の付け根

    player.say("§a超高精細ハチドリ完成！")
    player.say("§e500×500ブロック、細部まで完全再現！")
    player.say("§b高度Y=300以上から全体をご覧ください")

def draw_hummingbird_ultra():
    """究極精細ハチドリ - 1000×1000ブロック版"""
    player.say("§6究極精細ハチドリを描画開始（1000×1000）...")
    player.say("§c警告：処理に数分かかる場合があります")

    # 超巨大な砂漠を作成
    player.execute("fill ~-500 ~-1 ~-500 ~500 ~-1 ~500 sandstone")

    LINE_COLOR = "red_sandstone"
    ACCENT_COLOR = "orange_terracotta"

    # === 超精密くちばし（300ブロック）===
    for i in range(0, 300, 1):
        # より細かい厚さ変化
        thickness = max(1, 10 - i // 30)
        player.execute(f"fill ~{-500+i} ~ ~{-thickness} ~{-498+i} ~ ~{thickness} {LINE_COLOR}")

        # 中心線を細く
        if i % 5 == 0:
            player.execute(f"fill ~{-500+i} ~ ~-1 ~{-499+i} ~ ~1 {ACCENT_COLOR}")

    # === 超精密頭部（より大きな円）===
    center_x = -200
    center_y = 0
    radius = 30

    # より細かい円の近似
    for i in range(-radius, radius + 1, 1):
        y_offset = int((radius * radius - i * i) ** 0.5)
        if y_offset >= 0:
            # 上下の円弧
            player.execute(f"fill ~{center_x + i - 2} ~ ~{center_y + y_offset - 2} ~{center_x + i + 2} ~ ~{center_y + y_offset + 2} {LINE_COLOR}")
            player.execute(f"fill ~{center_x + i - 2} ~ ~{center_y - y_offset - 2} ~{center_x + i + 2} ~ ~{center_y - y_offset + 2} {LINE_COLOR}")

    for i in range(-radius, radius + 1, 1):
        x_offset = int((radius * radius - i * i) ** 0.5)
        if x_offset >= 0:
            # 左右の円弧
            player.execute(f"fill ~{center_x + x_offset - 2} ~ ~{center_y + i - 2} ~{center_x + x_offset + 2} ~ ~{center_y + i + 2} {LINE_COLOR}")
            player.execute(f"fill ~{center_x - x_offset - 2} ~ ~{center_y + i - 2} ~{center_x - x_offset + 2} ~ ~{center_y + i + 2} {LINE_COLOR}")

    # 目の超詳細
    player.execute(f"fill ~{center_x - 8} ~ ~{center_y - 8} ~{center_x + 8} ~ ~{center_y + 8} white_concrete")
    player.execute(f"fill ~{center_x - 5} ~ ~{center_y - 5} ~{center_x + 5} ~ ~{center_y + 5} blue_concrete")
    player.execute(f"fill ~{center_x - 2} ~ ~{center_y - 2} ~{center_x + 2} ~ ~{center_y + 2} black_concrete")
    player.execute(f"fill ~{center_x - 1} ~ ~{center_y + 1} ~{center_x + 1} ~ ~{center_y + 3} white_concrete")

    # === 詳細な翼（1000x1000版）===
    # より多くのセグメントで滑らかな翼

    # 左上翼（10段階）
    wing_segments_lu = []
    for i in range(10):
        x = -50 - i * 40
        y = 30 + i * 35
        wing_segments_lu.append((x, y))

    # 各セグメント間を細かく描画
    for i in range(len(wing_segments_lu) - 1):
        x1, y1 = wing_segments_lu[i]
        x2, y2 = wing_segments_lu[i + 1]

        thickness = max(3, 12 - i)

        for j in range(0, 50):  # より細かく分割
            x = x1 + (x2 - x1) * j // 50
            y = y1 + (y2 - y1) * j // 50
            player.execute(f"fill ~{x - thickness} ~ ~{y - thickness} ~{x + thickness} ~ ~{y + thickness} {LINE_COLOR}")

            # 羽の筋をより細かく
            if j % 10 == 0:
                player.execute(f"fill ~{x - thickness - 3} ~ ~{y} ~{x + thickness + 3} ~ ~{y + 1} {ACCENT_COLOR}")

    # 同様に他の翼も描画（右上、左下、右下）
    # 右上翼
    wing_segments_ru = []
    for i in range(10):
        x = 50 + i * 35
        y = 30 + i * 32
        wing_segments_ru.append((x, y))

    for i in range(len(wing_segments_ru) - 1):
        x1, y1 = wing_segments_ru[i]
        x2, y2 = wing_segments_ru[i + 1]
        thickness = max(3, 12 - i)
        for j in range(0, 50):
            x = x1 + (x2 - x1) * j // 50
            y = y1 + (y2 - y1) * j // 50
            player.execute(f"fill ~{x - thickness} ~ ~{y - thickness} ~{x + thickness} ~ ~{y + thickness} {LINE_COLOR}")

    # 左下翼
    wing_segments_ld = []
    for i in range(10):
        x = -50 - i * 40
        y = -30 - i * 35
        wing_segments_ld.append((x, y))

    for i in range(len(wing_segments_ld) - 1):
        x1, y1 = wing_segments_ld[i]
        x2, y2 = wing_segments_ld[i + 1]
        thickness = max(3, 12 - i)
        for j in range(0, 50):
            x = x1 + (x2 - x1) * j // 50
            y = y1 + (y2 - y1) * j // 50
            player.execute(f"fill ~{x - thickness} ~ ~{y - thickness} ~{x + thickness} ~ ~{y + thickness} {LINE_COLOR}")

    # 右下翼
    wing_segments_rd = []
    for i in range(10):
        x = 50 + i * 35
        y = -30 - i * 32
        wing_segments_rd.append((x, y))

    for i in range(len(wing_segments_rd) - 1):
        x1, y1 = wing_segments_rd[i]
        x2, y2 = wing_segments_rd[i + 1]
        thickness = max(3, 12 - i)
        for j in range(0, 50):
            x = x1 + (x2 - x1) * j // 50
            y = y1 + (y2 - y1) * j // 50
            player.execute(f"fill ~{x - thickness} ~ ~{y - thickness} ~{x + thickness} ~ ~{y + thickness} {LINE_COLOR}")

    # === 超詳細な尾羽（複雑な波形）===
    # より複雑な波形を作成
    for i in range(0, 400, 2):
        x = 50 + i

        # 複雑な波形（複数の周期を組み合わせ）
        wave1 = (i % 60) - 30  # 基本波
        wave2 = (i % 40) - 20  # 高周波
        wave3 = (i % 80) - 40  # 低周波

        y_upper = (wave1 + wave2 // 2 + wave3 // 3) // 3
        y_lower = -(wave1 + wave2 // 2 + wave3 // 3) // 3

        # 上側尾羽
        player.execute(f"fill ~{x - 3} ~ ~{y_upper - 2} ~{x + 3} ~ ~{y_upper + 2} {LINE_COLOR}")
        # 下側尾羽
        player.execute(f"fill ~{x - 3} ~ ~{y_lower - 2} ~{x + 3} ~ ~{y_lower + 2} {LINE_COLOR}")

        # 装飾的な羽毛
        if i % 20 == 0:
            player.execute(f"fill ~{x - 6} ~ ~{y_upper} ~{x + 6} ~ ~{y_upper + 1} {ACCENT_COLOR}")
            player.execute(f"fill ~{x - 6} ~ ~{y_lower - 1} ~{x + 6} ~ ~{y_lower} {ACCENT_COLOR}")

    player.say("§a究極精細ハチドリ完成！")
    player.say("§d1000×1000ブロック、完璧な曲線美！")
    player.say("§c高度Y=500以上を強く推奨")

# コマンド登録
player.on_chat("bird_hd", draw_hummingbird_hd)
player.on_chat("bird_ultra", draw_hummingbird_ultra)

# ヘルプ
def on_help_hd():
    player.say("§b=== 超高精細ナスカアート ===")
    player.say("§e!bird_hd - 500×500 高精細ハチドリ")
    player.say("§c!bird_ultra - 1000×1000 究極精細ハチドリ")
    player.say("§a細部まで完全再現！曲線も滑らか！")
    player.say("§7※mathモジュール不使用で高精度描画")

player.on_chat("nazca_hd", on_help_hd)

# 起動メッセージ
player.say("§d=== 超高精細ナスカアート起動！ ===")
player.say("§a数学関数を使わずに曲線を完全再現！")
player.say("§e'!nazca_hd' でヘルプ表示")