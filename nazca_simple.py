# Minecraft Education Edition - 超高精細ナスカの地上絵
# mathモジュールを一切使わない完全対応版

def draw_hummingbird_hd():
    """超高精細ハチドリ - 500×500ブロック（mathなし）"""
    player.say("§6超高精細ハチドリを描画開始（500×500）...")

    # 巨大な砂漠を作成
    player.execute("fill ~-250 ~-1 ~-250 ~250 ~-1 ~250 sandstone")

    # === 長大なくちばし（150ブロック）===
    for i in range(0, 150, 2):
        thickness = max(1, 6 - i // 25)
        player.execute(f"fill ~{-250+i} ~ ~{-thickness} ~{-248+i} ~ ~{thickness} red_sandstone")

    # === 頭部（円形）===
    center_x = -100
    radius = 15

    # 円を四角形の組み合わせで近似
    for i in range(-radius, radius + 1, 2):
        # 平方根を使わない円の近似
        if i * i <= radius * radius:
            y_offset = radius - abs(i) // 2
            player.execute(f"fill ~{center_x + i - 1} ~ ~{y_offset - 1} ~{center_x + i + 1} ~ ~{y_offset + 1} red_sandstone")
            player.execute(f"fill ~{center_x + i - 1} ~ ~{-y_offset - 1} ~{center_x + i + 1} ~ ~{-y_offset + 1} red_sandstone")

    # 目
    player.execute(f"fill ~{center_x - 3} ~ ~-3 ~{center_x + 3} ~ ~3 white_concrete")
    player.execute(f"fill ~{center_x - 1} ~ ~-1 ~{center_x + 1} ~ ~1 black_concrete")

    # === 首（段階的カーブ）===
    neck_x_points = [-85, -80, -75, -70, -65, -60, -55, -50, -45, -40]
    neck_y_upper = [12, 10, 8, 5, 2, 0, -2, -5, -8, -10]
    neck_y_lower = [-12, -10, -8, -5, -2, 0, 2, 5, 8, 10]

    for i in range(len(neck_x_points) - 1):
        x1, y1 = neck_x_points[i], neck_y_upper[i]
        x2, y2 = neck_x_points[i + 1], neck_y_upper[i + 1]

        # 上側の首
        for j in range(0, 10):
            x = x1 + (x2 - x1) * j // 10
            y = y1 + (y2 - y1) * j // 10
            player.execute(f"fill ~{x - 1} ~ ~{y - 1} ~{x + 1} ~ ~{y + 1} red_sandstone")

        # 下側の首
        y1_lower, y2_lower = neck_y_lower[i], neck_y_lower[i + 1]
        for j in range(0, 10):
            x = x1 + (x2 - x1) * j // 10
            y = y1_lower + (y2_lower - y1_lower) * j // 10
            player.execute(f"fill ~{x - 1} ~ ~{y - 1} ~{x + 1} ~ ~{y + 1} red_sandstone")

    # === 胴体（楕円近似）===
    body_center_x = -10
    for x in range(-50, 51, 3):
        # 楕円を三角形の組み合わせで近似
        y_max = max(0, 20 - abs(x) // 3)
        player.execute(f"fill ~{body_center_x + x - 1} ~ ~{y_max - 1} ~{body_center_x + x + 1} ~ ~{y_max + 1} red_sandstone")
        player.execute(f"fill ~{body_center_x + x - 1} ~ ~{-y_max - 1} ~{body_center_x + x + 1} ~ ~{-y_max + 1} red_sandstone")

    # === 翼（4方向）===
    # 左上翼
    wing_points_lu = [(-20, 20), (-40, 40), (-70, 70), (-110, 110), (-160, 160), (-220, 220)]
    for i in range(len(wing_points_lu) - 1):
        x1, y1 = wing_points_lu[i]
        x2, y2 = wing_points_lu[i + 1]
        thickness = max(2, 8 - i)

        for j in range(0, 20):
            x = x1 + (x2 - x1) * j // 20
            y = y1 + (y2 - y1) * j // 20
            player.execute(f"fill ~{x - thickness} ~ ~{y - thickness} ~{x + thickness} ~ ~{y + thickness} red_sandstone")

    # 右上翼
    wing_points_ru = [(30, 20), (60, 40), (100, 70), (150, 110), (210, 160)]
    for i in range(len(wing_points_ru) - 1):
        x1, y1 = wing_points_ru[i]
        x2, y2 = wing_points_ru[i + 1]
        thickness = max(2, 8 - i)

        for j in range(0, 20):
            x = x1 + (x2 - x1) * j // 20
            y = y1 + (y2 - y1) * j // 20
            player.execute(f"fill ~{x - thickness} ~ ~{y - thickness} ~{x + thickness} ~ ~{y + thickness} red_sandstone")

    # 左下翼
    wing_points_ld = [(-20, -20), (-40, -40), (-70, -70), (-110, -110), (-160, -160), (-220, -220)]
    for i in range(len(wing_points_ld) - 1):
        x1, y1 = wing_points_ld[i]
        x2, y2 = wing_points_ld[i + 1]
        thickness = max(2, 8 - i)

        for j in range(0, 20):
            x = x1 + (x2 - x1) * j // 20
            y = y1 + (y2 - y1) * j // 20
            player.execute(f"fill ~{x - thickness} ~ ~{y - thickness} ~{x + thickness} ~ ~{y + thickness} red_sandstone")

    # 右下翼
    wing_points_rd = [(30, -20), (60, -40), (100, -70), (150, -110), (210, -160)]
    for i in range(len(wing_points_rd) - 1):
        x1, y1 = wing_points_rd[i]
        x2, y2 = wing_points_rd[i + 1]
        thickness = max(2, 8 - i)

        for j in range(0, 20):
            x = x1 + (x2 - x1) * j // 20
            y = y1 + (y2 - y1) * j // 20
            player.execute(f"fill ~{x - thickness} ~ ~{y - thickness} ~{x + thickness} ~ ~{y + thickness} red_sandstone")

    # === 尾羽（波状）===
    for i in range(0, 120, 4):
        x = 40 + i
        # 簡単な波形（余弦なし）
        wave_cycle = i % 40
        if wave_cycle < 10:
            y_upper = i // 20
            y_lower = -(i // 20)
        elif wave_cycle < 20:
            y_upper = 5 - i // 20
            y_lower = -5 + i // 20
        elif wave_cycle < 30:
            y_upper = -(i // 20)
            y_lower = i // 20
        else:
            y_upper = -5 + i // 20
            y_lower = 5 - i // 20

        player.execute(f"fill ~{x - 2} ~ ~{y_upper - 1} ~{x + 2} ~ ~{y_upper + 1} red_sandstone")
        player.execute(f"fill ~{x - 2} ~ ~{y_lower - 1} ~{x + 2} ~ ~{y_lower + 1} red_sandstone")

    # 尾羽の先端装飾
    player.execute(f"fill ~155 ~ ~-8 ~165 ~ ~-5 orange_terracotta")
    player.execute(f"fill ~155 ~ ~5 ~165 ~ ~8 orange_terracotta")

    player.say("§a超高精細ハチドリ完成！")
    player.say("§e500×500ブロック、数学関数なしで完全再現！")

def draw_hummingbird_ultra():
    """究極精細ハチドリ - 1000×1000ブロック（mathなし）"""
    player.say("§6究極精細ハチドリを描画開始（1000×1000）...")

    # 超巨大な砂漠を作成
    player.execute("fill ~-500 ~-1 ~-500 ~500 ~-1 ~500 sandstone")

    # === 超精密くちばし（300ブロック）===
    for i in range(0, 300, 1):
        thickness = max(1, 10 - i // 30)
        player.execute(f"fill ~{-500+i} ~ ~{-thickness} ~{-498+i} ~ ~{thickness} red_sandstone")

        if i % 5 == 0:
            player.execute(f"fill ~{-500+i} ~ ~-1 ~{-499+i} ~ ~1 orange_terracotta")

    # === 超精密頭部（大きな円）===
    center_x = -200
    radius = 30

    # より精密な円（段階的近似）
    for i in range(-radius, radius + 1, 1):
        # より滑らかな円の近似
        y_offset = radius - abs(i) * 2 // 3
        if y_offset > 0:
            for j in range(-y_offset, y_offset + 1, 2):
                player.execute(f"fill ~{center_x + i - 1} ~ ~{j - 1} ~{center_x + i + 1} ~ ~{j + 1} red_sandstone")

    # 目の超詳細
    player.execute(f"fill ~{center_x - 8} ~ ~-8 ~{center_x + 8} ~ ~8 white_concrete")
    player.execute(f"fill ~{center_x - 5} ~ ~-5 ~{center_x + 5} ~ ~5 blue_concrete")
    player.execute(f"fill ~{center_x - 2} ~ ~-2 ~{center_x + 2} ~ ~2 black_concrete")
    player.execute(f"fill ~{center_x - 1} ~ ~1 ~{center_x + 1} ~ ~3 white_concrete")

    # === 詳細な翼（1000x1000版）===
    # 左上翼（より多くのセグメント）
    for segment in range(12):
        x_start = -50 - segment * 35
        y_start = 30 + segment * 30
        x_end = -50 - (segment + 1) * 35
        y_end = 30 + (segment + 1) * 30

        thickness = max(3, 15 - segment)

        for step in range(0, 40):
            x = x_start + (x_end - x_start) * step // 40
            y = y_start + (y_end - y_start) * step // 40
            player.execute(f"fill ~{x - thickness} ~ ~{y - thickness} ~{x + thickness} ~ ~{y + thickness} red_sandstone")

            # 羽の筋
            if step % 8 == 0:
                player.execute(f"fill ~{x - thickness - 2} ~ ~{y} ~{x + thickness + 2} ~ ~{y + 1} orange_terracotta")

    # 右上翼
    for segment in range(12):
        x_start = 50 + segment * 30
        y_start = 30 + segment * 25
        x_end = 50 + (segment + 1) * 30
        y_end = 30 + (segment + 1) * 25

        thickness = max(3, 15 - segment)

        for step in range(0, 40):
            x = x_start + (x_end - x_start) * step // 40
            y = y_start + (y_end - y_start) * step // 40
            player.execute(f"fill ~{x - thickness} ~ ~{y - thickness} ~{x + thickness} ~ ~{y + thickness} red_sandstone")

    # 左下翼
    for segment in range(12):
        x_start = -50 - segment * 35
        y_start = -30 - segment * 30
        x_end = -50 - (segment + 1) * 35
        y_end = -30 - (segment + 1) * 30

        thickness = max(3, 15 - segment)

        for step in range(0, 40):
            x = x_start + (x_end - x_start) * step // 40
            y = y_start + (y_end - y_start) * step // 40
            player.execute(f"fill ~{x - thickness} ~ ~{y - thickness} ~{x + thickness} ~ ~{y + thickness} red_sandstone")

    # 右下翼
    for segment in range(12):
        x_start = 50 + segment * 30
        y_start = -30 - segment * 25
        x_end = 50 + (segment + 1) * 30
        y_end = -30 - (segment + 1) * 25

        thickness = max(3, 15 - segment)

        for step in range(0, 40):
            x = x_start + (x_end - x_start) * step // 40
            y = y_start + (y_end - y_start) * step // 40
            player.execute(f"fill ~{x - thickness} ~ ~{y - thickness} ~{x + thickness} ~ ~{y + thickness} red_sandstone")

    # === 超詳細な尾羽（複雑な波形）===
    for i in range(0, 400, 2):
        x = 50 + i

        # 複雑な波形（三角関数なし）
        wave1 = (i % 60) - 30
        wave2 = (i % 40) - 20
        wave3 = (i % 80) - 40

        y_upper = (wave1 + wave2 // 2 + wave3 // 3) // 3
        y_lower = -(wave1 + wave2 // 2 + wave3 // 3) // 3

        player.execute(f"fill ~{x - 3} ~ ~{y_upper - 2} ~{x + 3} ~ ~{y_upper + 2} red_sandstone")
        player.execute(f"fill ~{x - 3} ~ ~{y_lower - 2} ~{x + 3} ~ ~{y_lower + 2} red_sandstone")

        if i % 20 == 0:
            player.execute(f"fill ~{x - 6} ~ ~{y_upper} ~{x + 6} ~ ~{y_upper + 1} orange_terracotta")
            player.execute(f"fill ~{x - 6} ~ ~{y_lower - 1} ~{x + 6} ~ ~{y_lower} orange_terracotta")

    player.say("§a究極精細ハチドリ完成！")
    player.say("§d1000×1000ブロック、完璧！")

# コマンド登録
player.on_chat("bird_hd", draw_hummingbird_hd)
player.on_chat("bird_ultra", draw_hummingbird_ultra)

def on_help():
    player.say("§b=== 超高精細ナスカアート ===")
    player.say("§e!bird_hd - 500×500 高精細ハチドリ")
    player.say("§c!bird_ultra - 1000×1000 究極精細ハチドリ")
    player.say("§a完全mathフリー版！")

player.on_chat("nazca_hd", on_help)

player.say("§d=== 超高精細ナスカアート起動！ ===")
player.say("§aMath関数完全不使用版！")