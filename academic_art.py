# Minecraft Education Edition - アカデミック・ピクセルアート（改良版）
# 64×64ピクセルで精密に再現（詳細版）

def draw_einstein_64_detailed(x=0, y=0, z=0):
    """アインシュタイン - 64×64ピクセル詳細版"""
    player.say("§6アインシュタイン（詳細版64×64）を描画中...")

    # 背景 - 薄い青（空のような背景）
    player.execute("fill ~0 ~64 ~0 ~63 ~127 ~0 light_blue_wool")

    # ===== 特徴的なぼさぼさ白髪（重要！）=====
    # 上部の広がる髪
    player.execute("fill ~15 ~113 ~0 ~48 ~120 ~0 white_wool")
    player.execute("fill ~18 ~110 ~0 ~45 ~112 ~0 white_wool")

    # 髪の質感（ぼさぼさ感を出す）
    player.execute("fill ~12 ~115 ~0 ~17 ~118 ~0 white_wool")  # 左側の髪
    player.execute("fill ~46 ~115 ~0 ~51 ~118 ~0 white_wool")  # 右側の髪
    player.execute("fill ~14 ~118 ~0 ~18 ~121 ~0 light_gray_wool")  # 左上
    player.execute("fill ~45 ~118 ~0 ~49 ~121 ~0 light_gray_wool")  # 右上

    # ===== 顔の輪郭（肌色）=====
    # 楕円形の顔
    player.execute("fill ~22 ~98 ~0 ~41 ~110 ~0 pink_wool")
    player.execute("fill ~20 ~100 ~0 ~43 ~108 ~0 pink_wool")
    player.execute("fill ~24 ~95 ~0 ~39 ~98 ~0 pink_wool")  # 下顎

    # 額
    player.execute("fill ~24 ~110 ~0 ~39 ~113 ~0 pink_wool")

    # ===== 眉毛（白い太眉）=====
    player.execute("fill ~23 ~107 ~0 ~28 ~108 ~0 light_gray_wool")
    player.execute("fill ~35 ~107 ~0 ~40 ~108 ~0 light_gray_wool")

    # ===== 目（知的な目）=====
    # 左目
    player.execute("fill ~24 ~104 ~0 ~27 ~106 ~0 white_wool")
    player.execute("setblock ~25 ~105 ~0 brown_wool")  # 瞳
    player.execute("setblock ~26 ~105 ~0 black_wool")  # 瞳孔

    # 右目
    player.execute("fill ~36 ~104 ~0 ~39 ~106 ~0 white_wool")
    player.execute("setblock ~37 ~105 ~0 brown_wool")  # 瞳
    player.execute("setblock ~38 ~105 ~0 black_wool")  # 瞳孔

    # ===== 鼻（立体感）=====
    player.execute("fill ~30 ~100 ~0 ~33 ~104 ~0 pink_wool")
    player.execute("fill ~31 ~99 ~0 ~32 ~100 ~0 orange_wool")  # 鼻の影

    # ===== 特徴的な白い口髭（最重要！）=====
    # 口髭の形状を精密に
    player.execute("fill ~22 ~96 ~0 ~41 ~100 ~0 white_wool")
    player.execute("fill ~20 ~97 ~0 ~43 ~99 ~0 white_wool")
    player.execute("fill ~23 ~95 ~0 ~40 ~96 ~0 light_gray_wool")  # 髭の影

    # 髭の質感（波打つような）
    player.execute("fill ~19 ~98 ~0 ~22 ~98 ~0 light_gray_wool")
    player.execute("fill ~41 ~98 ~0 ~44 ~98 ~0 light_gray_wool")

    # ===== 口（髭の下に少し見える）=====
    player.execute("fill ~28 ~96 ~0 ~35 ~97 ~0 red_wool")

    # ===== もみあげ（白髪）=====
    player.execute("fill ~19 ~100 ~0 ~22 ~108 ~0 white_wool")
    player.execute("fill ~41 ~100 ~0 ~44 ~108 ~0 white_wool")

    # ===== 耳（ちょこっと見える）=====
    player.execute("fill ~19 ~103 ~0 ~20 ~106 ~0 pink_wool")
    player.execute("fill ~43 ~103 ~0 ~44 ~106 ~0 pink_wool")

    # ===== E=mc² の数式（はっきりと！）=====
    # 背景の黒板
    player.execute("fill ~18 ~82 ~0 ~45 ~90 ~0 black_wool")

    # E (白チョークで書いた文字)
    player.execute("fill ~20 ~84 ~0 ~20 ~88 ~0 white_wool")
    player.execute("fill ~20 ~84 ~0 ~23 ~84 ~0 white_wool")
    player.execute("fill ~20 ~86 ~0 ~22 ~86 ~0 white_wool")
    player.execute("fill ~20 ~88 ~0 ~23 ~88 ~0 white_wool")

    # = (イコール)
    player.execute("fill ~25 ~85 ~0 ~27 ~85 ~0 white_wool")
    player.execute("fill ~25 ~87 ~0 ~27 ~87 ~0 white_wool")

    # m (エム)
    player.execute("fill ~29 ~84 ~0 ~29 ~88 ~0 white_wool")
    player.execute("setblock ~30 ~88 ~0 white_wool")
    player.execute("fill ~31 ~84 ~0 ~31 ~88 ~0 white_wool")
    player.execute("setblock ~32 ~88 ~0 white_wool")
    player.execute("fill ~33 ~84 ~0 ~33 ~88 ~0 white_wool")

    # c (シー)
    player.execute("fill ~35 ~84 ~0 ~35 ~88 ~0 white_wool")
    player.execute("fill ~35 ~84 ~0 ~37 ~84 ~0 white_wool")
    player.execute("fill ~35 ~88 ~0 ~37 ~88 ~0 white_wool")

    # ² (二乗)
    player.execute("fill ~39 ~87 ~0 ~40 ~88 ~0 yellow_wool")
    player.execute("setblock ~39 ~86 ~0 yellow_wool")
    player.execute("setblock ~40 ~87 ~0 black_wool")

    # ===== 服（グレーのスーツ）=====
    player.execute("fill ~20 ~64 ~0 ~43 ~82 ~0 gray_wool")

    # 襟元（白いシャツ）
    player.execute("fill ~28 ~79 ~0 ~35 ~84 ~0 white_wool")

    # ネクタイ
    player.execute("fill ~30 ~75 ~0 ~33 ~82 ~0 brown_wool")

    player.say("§aアインシュタイン完成！")
    player.say("§e特徴: ぼさぼさ白髪、立派な口髭、E=mc²")

def draw_mona_lisa_64_detailed(x=0, y=0, z=0):
    """モナ・リザ - 64×64ピクセル詳細版"""
    player.say("§6モナ・リザ（詳細版64×64）を描画中...")

    # 背景（暗緑の風景画風）
    player.execute("fill ~0 ~64 ~70 ~63 ~127 ~70 green_wool")
    player.execute("fill ~0 ~100 ~70 ~63 ~127 ~70 cyan_wool")  # 空の部分

    # ===== 黒く長い髪 =====
    player.execute("fill ~18 ~102 ~70 ~45 ~118 ~70 black_wool")
    player.execute("fill ~16 ~105 ~70 ~47 ~115 ~70 black_wool")

    # 髪の分け目
    player.execute("fill ~31 ~110 ~70 ~32 ~118 ~70 black_wool")

    # ===== 顔（やわらかい輪郭）=====
    player.execute("fill ~24 ~96 ~70 ~39 ~110 ~70 pink_wool")
    player.execute("fill ~22 ~100 ~70 ~41 ~108 ~70 pink_wool")

    # 額
    player.execute("fill ~26 ~110 ~70 ~37 ~112 ~70 pink_wool")

    # ===== 眉毛（細い、繊細な）=====
    player.execute("fill ~25 ~108 ~70 ~28 ~108 ~70 brown_wool")
    player.execute("fill ~35 ~108 ~70 ~38 ~108 ~70 brown_wool")

    # ===== 目（神秘的な視線）=====
    # 左目
    player.execute("fill ~26 ~105 ~70 ~28 ~106 ~70 white_wool")
    player.execute("setblock ~27 ~105 ~70 brown_wool")

    # 右目
    player.execute("fill ~35 ~105 ~70 ~37 ~106 ~70 white_wool")
    player.execute("setblock ~36 ~105 ~70 brown_wool")

    # ===== 鼻（優雅に）=====
    player.execute("fill ~30 ~101 ~70 ~33 ~106 ~70 pink_wool")
    player.execute("setblock ~31 ~101 ~70 orange_wool")
    player.execute("setblock ~32 ~101 ~70 orange_wool")

    # ===== 謎めいた微笑み（最重要！）=====
    # 口の形状を精密に
    player.execute("fill ~28 ~100 ~70 ~35 ~101 ~70 red_wool")
    # 微笑みの端が上がっている
    player.execute("setblock ~27 ~101 ~70 red_wool")
    player.execute("setblock ~36 ~101 ~70 red_wool")

    # ===== 暗い服（ドレス）=====
    player.execute("fill ~20 ~64 ~70 ~43 ~96 ~70 black_wool")
    player.execute("fill ~18 ~70 ~70 ~45 ~90 ~70 black_wool")

    # 襟元（少し明るく）
    player.execute("fill ~26 ~93 ~70 ~37 ~96 ~70 gray_wool")

    # ===== 手（組んだ手）=====
    player.execute("fill ~22 ~70 ~70 ~41 ~78 ~70 pink_wool")
    player.execute("fill ~24 ~72 ~70 ~28 ~76 ~70 pink_wool")  # 左手
    player.execute("fill ~35 ~72 ~70 ~39 ~76 ~70 pink_wool")  # 右手

    player.say("§aモナ・リザ完成！")
    player.say("§e特徴: 謎めいた微笑み、長い黒髪")

def draw_marilyn_64_detailed(x=0, y=0, z=0):
    """マリリン・モンロー - 64×64ピクセル詳細版（ポップアート風）"""
    player.say("§6マリリン・モンロー（詳細版64×64）を描画中...")

    # ポップアート風の明るい背景（黄色）
    player.execute("fill ~0 ~64 ~140 ~63 ~127 ~140 yellow_wool")

    # ===== プラチナブロンドの髪（波打つ髪）=====
    player.execute("fill ~16 ~100 ~140 ~47 ~120 ~140 white_wool")
    player.execute("fill ~12 ~105 ~140 ~51 ~118 ~140 white_wool")

    # 髪の質感（ウェーブ）
    player.execute("fill ~14 ~115 ~140 ~18 ~117 ~140 yellow_wool")
    player.execute("fill ~45 ~115 ~140 ~49 ~117 ~140 yellow_wool")

    # 前髪
    player.execute("fill ~20 ~112 ~140 ~43 ~115 ~140 white_wool")

    # ===== 顔（ピンクがかった肌）=====
    player.execute("fill ~20 ~90 ~140 ~43 ~110 ~140 pink_wool")
    player.execute("fill ~22 ~92 ~140 ~41 ~108 ~140 white_wool")  # ハイライト

    # ===== アイメイク（濃いメイク）=====
    # アイシャドウ（青紫）
    player.execute("fill ~23 ~106 ~140 ~28 ~108 ~140 purple_wool")
    player.execute("fill ~35 ~106 ~140 ~40 ~108 ~140 purple_wool")

    # アイライナー
    player.execute("fill ~23 ~105 ~140 ~28 ~105 ~140 black_wool")
    player.execute("fill ~35 ~105 ~140 ~40 ~105 ~140 black_wool")

    # ===== 目（大きな瞳）=====
    # 左目
    player.execute("fill ~24 ~102 ~140 ~27 ~104 ~140 white_wool")
    player.execute("setblock ~25 ~103 ~140 blue_wool")  # 青い瞳
    player.execute("setblock ~26 ~103 ~140 black_wool")

    # 右目
    player.execute("fill ~36 ~102 ~140 ~39 ~104 ~140 white_wool")
    player.execute("setblock ~37 ~103 ~140 blue_wool")
    player.execute("setblock ~38 ~103 ~140 black_wool")

    # まつ毛
    player.execute("fill ~23 ~104 ~140 ~28 ~104 ~140 black_wool")
    player.execute("fill ~35 ~104 ~140 ~40 ~104 ~140 black_wool")

    # ===== 鼻（小さく）=====
    player.execute("fill ~30 ~98 ~140 ~33 ~102 ~140 pink_wool")

    # ===== ホクロ（チャームポイント！）=====
    player.execute("setblock ~38 ~96 ~140 black_wool")
    player.execute("setblock ~39 ~96 ~140 black_wool")

    # ===== 赤い唇（セクシーな口）=====
    player.execute("fill ~26 ~94 ~140 ~37 ~97 ~140 red_wool")
    # 唇の立体感
    player.execute("fill ~28 ~95 ~140 ~35 ~96 ~140 pink_wool")

    # ===== 白いドレス =====
    player.execute("fill ~18 ~64 ~140 ~45 ~90 ~140 white_wool")
    player.execute("fill ~15 ~70 ~140 ~48 ~85 ~140 white_wool")

    # ドレスの影
    player.execute("fill ~30 ~75 ~140 ~33 ~85 ~140 light_gray_wool")

    player.say("§aマリリン・モンロー完成！")
    player.say("§e特徴: プラチナブロンド、ホクロ、赤い唇")

def draw_beethoven_64_detailed(x=0, y=0, z=0):
    """ベートーヴェン - 64×64ピクセル詳細版"""
    player.say("§6ベートーヴェン（詳細版64×64）を描画中...")

    # 背景（楽譜）
    player.execute("fill ~0 ~64 ~210 ~63 ~127 ~210 white_wool")

    # ===== 五線譜（背景）=====
    player.execute("fill ~0 ~115 ~210 ~63 ~115 ~210 black_wool")
    player.execute("fill ~0 ~110 ~210 ~63 ~110 ~210 black_wool")
    player.execute("fill ~0 ~105 ~210 ~63 ~105 ~210 black_wool")
    player.execute("fill ~0 ~100 ~210 ~63 ~100 ~210 black_wool")
    player.execute("fill ~0 ~95 ~210 ~63 ~95 ~210 black_wool")

    # 音符
    player.execute("fill ~8 ~105 ~210 ~10 ~110 ~210 black_wool")
    player.execute("fill ~9 ~110 ~210 ~11 ~110 ~210 black_wool")
    player.execute("fill ~50 ~100 ~210 ~52 ~105 ~210 black_wool")
    player.execute("fill ~51 ~105 ~210 ~53 ~105 ~210 black_wool")

    # ===== 乱れた髪（灰色の髪）=====
    player.execute("fill ~14 ~105 ~210 ~49 ~122 ~210 gray_wool")
    player.execute("fill ~12 ~108 ~210 ~51 ~120 ~210 gray_wool")

    # 髪のぼさぼさ感
    player.execute("fill ~10 ~115 ~210 ~15 ~118 ~210 light_gray_wool")
    player.execute("fill ~48 ~115 ~210 ~53 ~118 ~210 light_gray_wool")
    player.execute("fill ~16 ~120 ~210 ~47 ~123 ~210 gray_wool")

    # ===== 顔（強い表情）=====
    player.execute("fill ~22 ~88 ~210 ~41 ~105 ~210 pink_wool")
    player.execute("fill ~20 ~92 ~210 ~43 ~103 ~210 pink_wool")

    # ===== 太い眉毛（険しい表情）=====
    player.execute("fill ~23 ~102 ~210 ~28 ~103 ~210 black_wool")
    player.execute("fill ~35 ~102 ~210 ~40 ~103 ~210 black_wool")
    player.execute("fill ~24 ~103 ~210 ~27 ~104 ~210 black_wool")
    player.execute("fill ~36 ~103 ~210 ~39 ~104 ~210 black_wool")

    # ===== 鋭い目（厳しい視線）=====
    # 左目
    player.execute("fill ~25 ~98 ~210 ~27 ~100 ~210 white_wool")
    player.execute("setblock ~26 ~99 ~210 brown_wool")
    player.execute("setblock ~26 ~98 ~210 black_wool")

    # 右目
    player.execute("fill ~36 ~98 ~210 ~38 ~100 ~210 white_wool")
    player.execute("setblock ~37 ~99 ~210 brown_wool")
    player.execute("setblock ~37 ~98 ~210 black_wool")

    # ===== 鼻（力強い）=====
    player.execute("fill ~30 ~94 ~210 ~33 ~99 ~210 pink_wool")
    player.execute("fill ~31 ~93 ~210 ~32 ~94 ~210 orange_wool")

    # ===== 口（固く結んだ口）=====
    player.execute("fill ~28 ~90 ~210 ~35 ~91 ~210 brown_wool")

    # ===== もみあげ =====
    player.execute("fill ~20 ~95 ~210 ~23 ~103 ~210 gray_wool")
    player.execute("fill ~40 ~95 ~210 ~43 ~103 ~210 gray_wool")

    # ===== 黒い服（フォーマル）=====
    player.execute("fill ~18 ~64 ~210 ~45 ~88 ~210 black_wool")

    # 白いシャツの襟
    player.execute("fill ~28 ~85 ~210 ~35 ~88 ~210 white_wool")

    # 黒いネクタイ
    player.execute("fill ~30 ~80 ~210 ~33 ~87 ~210 black_wool")

    player.say("§aベートーヴェン完成！")
    player.say("§e特徴: 乱れた灰色の髪、険しい表情、五線譜")

def draw_van_gogh_64_detailed(x=0, y=0, z=0):
    """ゴッホ自画像 - 64×64ピクセル詳細版"""
    player.say("§6ゴッホ自画像（詳細版64×64）を描画中...")

    # 背景（渦巻く青）
    player.execute("fill ~0 ~64 ~280 ~63 ~127 ~280 blue_wool")

    # 渦巻き効果
    player.execute("fill ~5 ~100 ~280 ~25 ~120 ~280 cyan_wool")
    player.execute("fill ~38 ~100 ~280 ~58 ~120 ~280 light_blue_wool")
    player.execute("fill ~15 ~110 ~280 ~48 ~125 ~280 blue_wool")

    # ===== 赤茶色の髪 =====
    player.execute("fill ~20 ~102 ~280 ~43 ~118 ~280 orange_wool")
    player.execute("fill ~16 ~105 ~280 ~47 ~115 ~280 orange_wool")

    # 髪の質感
    player.execute("fill ~18 ~110 ~280 ~22 ~115 ~280 red_wool")
    player.execute("fill ~41 ~110 ~280 ~45 ~115 ~280 red_wool")

    # ===== 顔（苦悩の表情）=====
    player.execute("fill ~23 ~88 ~280 ~40 ~102 ~280 pink_wool")
    player.execute("fill ~21 ~92 ~280 ~42 ~100 ~280 pink_wool")

    # ===== 眉毛（濃い）=====
    player.execute("fill ~24 ~100 ~280 ~28 ~101 ~280 orange_wool")
    player.execute("fill ~35 ~100 ~280 ~39 ~101 ~280 orange_wool")

    # ===== 目（深い悲しみ）=====
    # 左目
    player.execute("fill ~25 ~96 ~280 ~27 ~98 ~280 white_wool")
    player.execute("setblock ~26 ~97 ~280 green_wool")  # 緑の瞳
    player.execute("setblock ~26 ~96 ~280 black_wool")

    # 右目
    player.execute("fill ~36 ~96 ~280 ~38 ~98 ~280 white_wool")
    player.execute("setblock ~37 ~97 ~280 green_wool")
    player.execute("setblock ~37 ~96 ~280 black_wool")

    # ===== 鼻 =====
    player.execute("fill ~30 ~92 ~280 ~33 ~97 ~280 pink_wool")
    player.execute("setblock ~31 ~92 ~280 orange_wool")

    # ===== 赤ひげ =====
    player.execute("fill ~22 ~85 ~280 ~41 ~92 ~280 orange_wool")
    player.execute("fill ~20 ~87 ~280 ~43 ~90 ~280 orange_wool")

    # ひげの質感
    player.execute("fill ~24 ~86 ~280 ~39 ~88 ~280 red_wool")

    # ===== 包帯の耳（重要！）=====
    # 右耳に白い包帯
    player.execute("fill ~40 ~94 ~280 ~45 ~100 ~280 white_wool")
    player.execute("fill ~41 ~95 ~280 ~44 ~99 ~280 white_wool")

    # 包帯の影
    player.execute("fill ~42 ~96 ~280 ~43 ~98 ~280 light_gray_wool")

    # ===== 左耳（正常な耳）=====
    player.execute("fill ~19 ~95 ~280 ~21 ~98 ~280 pink_wool")

    # ===== 口 =====
    player.execute("fill ~28 ~89 ~280 ~35 ~90 ~280 red_wool")

    # ===== 緑の服 =====
    player.execute("fill ~20 ~64 ~280 ~43 ~88 ~280 green_wool")
    player.execute("fill ~18 ~70 ~280 ~45 ~85 ~280 green_wool")

    # 襟元（暗緑）
    player.execute("fill ~26 ~84 ~280 ~37 ~88 ~280 lime_wool")

    player.say("§aゴッホ自画像完成！")
    player.say("§e特徴: 赤茶色の髪とひげ、包帯の耳、渦巻く背景")

def draw_da_vinci_64_detailed(x=0, y=0, z=0):
    """ダ・ヴィンチ - 64×64ピクセル詳細版"""
    player.say("§6ダ・ヴィンチ（詳細版64×64）を描画中...")

    # ルネサンス風の背景（暖色）
    player.execute("fill ~0 ~64 ~350 ~63 ~127 ~350 orange_wool")
    player.execute("fill ~0 ~90 ~350 ~63 ~127 ~350 yellow_wool")

    # ===== 長い白髪 =====
    player.execute("fill ~18 ~100 ~350 ~45 ~120 ~350 white_wool")
    player.execute("fill ~10 ~95 ~350 ~53 ~118 ~350 white_wool")

    # 髪の質感（ウェーブ）
    player.execute("fill ~12 ~105 ~350 ~18 ~115 ~350 light_gray_wool")
    player.execute("fill ~45 ~105 ~350 ~51 ~115 ~350 light_gray_wool")

    # ===== 顔（年老いた賢者）=====
    player.execute("fill ~20 ~88 ~350 ~43 ~105 ~350 pink_wool")
    player.execute("fill ~22 ~90 ~350 ~41 ~103 ~350 pink_wool")

    # しわ
    player.execute("fill ~24 ~100 ~350 ~39 ~100 ~350 orange_wool")
    player.execute("fill ~25 ~95 ~350 ~38 ~95 ~350 orange_wool")

    # ===== 白い眉毛 =====
    player.execute("fill ~23 ~102 ~350 ~28 ~103 ~350 white_wool")
    player.execute("fill ~35 ~102 ~350 ~40 ~103 ~350 white_wool")

    # ===== 目（知恵に満ちた）=====
    # 左目
    player.execute("fill ~25 ~98 ~350 ~27 ~100 ~350 white_wool")
    player.execute("setblock ~26 ~99 ~350 brown_wool")

    # 右目
    player.execute("fill ~36 ~98 ~350 ~38 ~100 ~350 white_wool")
    player.execute("setblock ~37 ~99 ~350 brown_wool")

    # ===== 鼻（立派な鼻）=====
    player.execute("fill ~30 ~93 ~350 ~33 ~99 ~350 pink_wool")
    player.execute("setblock ~31 ~93 ~350 orange_wool")

    # ===== 長い白いひげ（印象的！）=====
    player.execute("fill ~18 ~70 ~350 ~45 ~90 ~350 white_wool")
    player.execute("fill ~20 ~72 ~350 ~43 ~88 ~350 white_wool")

    # ひげの質感
    player.execute("fill ~24 ~75 ~350 ~39 ~85 ~350 light_gray_wool")

    # 口はひげに隠れている
    player.execute("fill ~28 ~91 ~350 ~35 ~92 ~350 pink_wool")

    # ===== もみあげ =====
    player.execute("fill ~19 ~95 ~350 ~22 ~103 ~350 white_wool")
    player.execute("fill ~41 ~95 ~350 ~44 ~103 ~350 white_wool")

    # ===== ベレー帽（芸術家の象徴）=====
    player.execute("fill ~20 ~110 ~350 ~43 ~118 ~350 red_wool")
    player.execute("fill ~22 ~115 ~350 ~41 ~120 ~350 red_wool")

    # 帽子の影
    player.execute("fill ~24 ~112 ~350 ~39 ~114 ~350 brown_wool")

    # ===== ルネサンス風の服 =====
    player.execute("fill ~18 ~64 ~350 ~45 ~72 ~350 brown_wool")
    player.execute("fill ~20 ~64 ~350 ~43 ~70 ~350 orange_wool")

    # 襟
    player.execute("fill ~26 ~88 ~350 ~37 ~90 ~350 brown_wool")

    player.say("§aダ・ヴィンチ完成！")
    player.say("§e特徴: 長い白髪とひげ、赤いベレー帽、賢者の風格")

def draw_all_gallery_detailed(x=0, y=0, z=0):
    """全作品を一度に描画（詳細版）"""
    player.say("§d=== 名作ギャラリー作成開始（詳細版）===")
    player.say("§e各作品の特徴を精密に再現します...")

    draw_einstein_64_detailed()
    draw_mona_lisa_64_detailed()
    draw_marilyn_64_detailed()
    draw_beethoven_64_detailed()
    draw_van_gogh_64_detailed()
    draw_da_vinci_64_detailed()

    player.say("§a=== 全6作品完成！ ===")
    player.say("§e各作品は70ブロック間隔で配置されています")
    player.say("§b高さY=96付近から見ると最適です！")
    player.say("§6今度こそ誰が誰だかわかるはず！")

def on_help_detailed(x=0, y=0, z=0):
    """ヘルプメッセージ（詳細版）"""
    player.say("§b=== アカデミック・ピクセルアート（詳細版）===")
    player.say("§d特徴を精密に再現した64×64版！")
    player.say("§e!ein - アインシュタイン（ぼさぼさ白髪・口髭・E=mc²）")
    player.say("§e!mona - モナ・リザ（謎の微笑み・黒髪）")
    player.say("§e!marilyn - マリリン・モンロー（プラチナブロンド・ホクロ）")
    player.say("§e!beethoven - ベートーヴェン（乱れた灰色髪・五線譜）")
    player.say("§e!vangogh - ゴッホ（赤ひげ・包帯の耳）")
    player.say("§e!davinci - ダ・ヴィンチ（白髪白ひげ・ベレー帽）")
    player.say("§c!gallery - 全作品を一度に作成")
    player.say("§a生徒も納得の精密ピクセルアート！")

# コマンド登録（短縮版も追加）
player.on_chat("ein", draw_einstein_64_detailed)
player.on_chat("einstein", draw_einstein_64_detailed)
player.on_chat("mona", draw_mona_lisa_64_detailed)
player.on_chat("monalisa", draw_mona_lisa_64_detailed)
player.on_chat("marilyn", draw_marilyn_64_detailed)
player.on_chat("beethoven", draw_beethoven_64_detailed)
player.on_chat("vangogh", draw_van_gogh_64_detailed)
player.on_chat("davinci", draw_da_vinci_64_detailed)
player.on_chat("gallery", draw_all_gallery_detailed)
player.on_chat("help", on_help_detailed)
player.on_chat("academic", on_help_detailed)

# 起動メッセージ
player.say("§d╔══════════════════════════════════╗")
player.say("§d║  名作ピクセルアートギャラリー    ║")
player.say("§d║     詳細版 64×64ピクセル        ║")
player.say("§d╚══════════════════════════════════╝")
player.say("")
player.say("§b--- コマンド一覧 ---")
player.say("§a!ein - アインシュタイン（白髪・口髭）")
player.say("§a!mona - モナ・リザ（謎の微笑み）")
player.say("§a!marilyn - マリリン・モンロー（ホクロ）")
player.say("§a!beethoven - ベートーヴェン（険しい表情）")
player.say("§a!vangogh - ゴッホ（包帯の耳）")
player.say("§a!davinci - ダ・ヴィンチ（白ひげ）")
player.say("§c!gallery - 全作品を一度に作成")
player.say("§f!help - ヘルプ表示")
player.say("")
player.say("§6座標: X=0-63, Y=64-127, Z=70ブロック間隔")
player.say("§e特徴を精密に再現！生徒も納得！")