# Minecraft Education Edition - ピクセルアートジェネレーター
# 巨大な女の子のイラストを描く（垂直・水平両対応）

def draw_girl_standing():
    """立っている女の子 - 垂直の壁に描く（約40×60ブロック）"""
    player.say("§d可愛い女の子を描きます...")

    # 背景（空色）
    player.execute("fill ~2 ~0 ~-20 ~2 ~60 ~20 light_blue_concrete")

    # 髪の毛（茶色）
    # 上部の髪
    player.execute("fill ~1 ~45 ~-8 ~1 ~55 ~8 brown_wool")
    player.execute("fill ~1 ~50 ~-10 ~1 ~55 ~10 brown_wool")

    # サイドの髪
    player.execute("fill ~1 ~35 ~-12 ~1 ~48 ~-8 brown_wool")
    player.execute("fill ~1 ~35 ~8 ~1 ~48 ~12 brown_wool")

    # 顔（肌色）
    player.execute("fill ~1 ~38 ~-7 ~1 ~48 ~7 peach_terracotta")

    # 目（黒と白）
    # 左目
    player.execute("fill ~1 ~42 ~-5 ~1 ~44 ~-3 white_concrete")
    player.execute("setblock ~1 ~43 ~-4 black_concrete")

    # 右目
    player.execute("fill ~1 ~42 ~3 ~1 ~44 ~5 white_concrete")
    player.execute("setblock ~1 ~43 ~4 black_concrete")

    # 口（ピンク）
    player.execute("fill ~1 ~39 ~-1 ~1 ~39 ~1 pink_concrete")

    # ほっぺ（赤）
    player.execute("setblock ~1 ~41 ~-6 red_concrete")
    player.execute("setblock ~1 ~41 ~6 red_concrete")

    # 体（服 - ピンクのワンピース）
    player.execute("fill ~1 ~20 ~-8 ~1 ~37 ~8 pink_wool")

    # リボン（赤）
    player.execute("fill ~1 ~36 ~-2 ~1 ~37 ~2 red_wool")

    # 腕（肌色）
    player.execute("fill ~1 ~25 ~-10 ~1 ~35 ~-9 peach_terracotta")
    player.execute("fill ~1 ~25 ~9 ~1 ~35 ~10 peach_terracotta")

    # 足（肌色）
    player.execute("fill ~1 ~10 ~-4 ~1 ~20 ~-2 peach_terracotta")
    player.execute("fill ~1 ~10 ~2 ~1 ~20 ~4 peach_terracotta")

    # 靴（赤）
    player.execute("fill ~1 ~8 ~-4 ~1 ~10 ~-2 red_concrete")
    player.execute("fill ~1 ~8 ~2 ~1 ~10 ~4 red_concrete")

    player.say("§a女の子完成！かわいい！")

def draw_cat_girl():
    """猫耳の女の子 - 地面に描く（約50×50ブロック）"""
    player.say("§d猫耳の女の子を地面に描きます...")

    # 背景（ピンク）
    player.execute("fill ~-25 ~-1 ~-25 ~25 ~-1 ~25 pink_concrete")

    # 髪の毛（黒）
    player.execute("fill ~-15 ~ ~-15 ~15 ~ ~15 black_wool")

    # 猫耳
    player.execute("fill ~-15 ~ ~10 ~-10 ~ ~18 black_wool")
    player.execute("fill ~10 ~ ~10 ~15 ~ ~18 black_wool")
    player.execute("fill ~-13 ~ ~12 ~-12 ~ ~16 pink_wool")
    player.execute("fill ~12 ~ ~12 ~13 ~ ~16 pink_wool")

    # 顔（肌色）
    player.execute("fill ~-10 ~ ~-10 ~10 ~ ~10 white_terracotta")

    # 目（大きな目）
    # 左目
    player.execute("fill ~-8 ~ ~2 ~-3 ~ ~6 white_concrete")
    player.execute("fill ~-7 ~ ~3 ~-4 ~ ~5 blue_concrete")
    player.execute("setblock ~-5 ~ ~4 black_concrete")

    # 右目
    player.execute("fill ~3 ~ ~2 ~8 ~ ~6 white_concrete")
    player.execute("fill ~4 ~ ~3 ~7 ~ ~5 blue_concrete")
    player.execute("setblock ~5 ~ ~4 black_concrete")

    # 口（にっこり）
    player.execute("fill ~-2 ~ ~-3 ~2 ~ ~-2 pink_concrete")
    player.execute("setblock ~-3 ~ ~-2 pink_concrete")
    player.execute("setblock ~3 ~ ~-2 pink_concrete")

    # ほっぺ（ピンク）
    player.execute("fill ~-10 ~ ~0 ~-8 ~ ~2 pink_wool")
    player.execute("fill ~8 ~ ~0 ~10 ~ ~2 pink_wool")

    # 髪飾り（リボン）
    player.execute("fill ~-5 ~ ~12 ~5 ~ ~14 red_wool")
    player.execute("fill ~-8 ~ ~13 ~-6 ~ ~15 red_wool")
    player.execute("fill ~6 ~ ~13 ~8 ~ ~15 red_wool")

    player.say("§a猫耳女の子完成！にゃー！")

def draw_princess():
    """プリンセス - 巨大（約80×100ブロック）"""
    player.say("§dプリンセスを描きます...")

    # 背景（城っぽく）
    player.execute("fill ~3 ~0 ~-40 ~3 ~100 ~40 white_concrete")

    # ティアラ（金）
    player.execute("fill ~2 ~85 ~-15 ~2 ~95 ~15 gold_block")
    player.execute("fill ~2 ~90 ~-10 ~2 ~92 ~10 diamond_block")

    # 髪（金髪）
    player.execute("fill ~2 ~60 ~-20 ~2 ~85 ~20 yellow_wool")
    player.execute("fill ~2 ~40 ~-25 ~2 ~70 ~25 yellow_wool")

    # 顔
    player.execute("fill ~2 ~65 ~-15 ~2 ~80 ~15 peach_terracotta")

    # 目
    player.execute("fill ~2 ~72 ~-10 ~2 ~75 ~-5 light_blue_concrete")
    player.execute("fill ~2 ~72 ~5 ~2 ~75 ~10 light_blue_concrete")
    player.execute("setblock ~2 ~73 ~-7 black_concrete")
    player.execute("setblock ~2 ~73 ~7 black_concrete")

    # ドレス（水色）
    player.execute("fill ~2 ~20 ~-20 ~2 ~65 ~20 light_blue_wool")
    player.execute("fill ~2 ~10 ~-30 ~2 ~30 ~30 light_blue_wool")

    # ドレスの飾り（ダイヤ）
    player.execute("fill ~2 ~45 ~-5 ~2 ~50 ~5 diamond_block")
    player.execute("fill ~2 ~35 ~-8 ~2 ~37 ~8 diamond_block")
    player.execute("fill ~2 ~25 ~-10 ~2 ~27 ~10 diamond_block")

    player.say("§aプリンセス完成！豪華です！")

def draw_anime_face():
    """アニメ風の顔（超巨大）- 約100×100ブロック"""
    player.say("§dアニメ風の巨大な顔を描きます...")

    # 輪郭
    player.execute("fill ~5 ~10 ~-40 ~5 ~90 ~40 white_concrete")

    # 髪（ピンク）
    player.execute("fill ~4 ~70 ~-45 ~4 ~95 ~45 pink_wool")
    player.execute("fill ~4 ~60 ~-50 ~4 ~85 ~-40 pink_wool")
    player.execute("fill ~4 ~60 ~40 ~4 ~85 ~50 pink_wool")

    # 前髪
    player.execute("fill ~3 ~75 ~-30 ~3 ~85 ~30 pink_wool")

    # 目（超大きい）
    # 左目
    player.execute("fill ~3 ~50 ~-30 ~3 ~65 ~-10 white_concrete")
    player.execute("fill ~2 ~52 ~-28 ~2 ~63 ~-12 purple_concrete")
    player.execute("fill ~1 ~54 ~-26 ~1 ~61 ~-14 black_concrete")
    player.execute("fill ~1 ~58 ~-20 ~1 ~60 ~-18 white_concrete")

    # 右目
    player.execute("fill ~3 ~50 ~10 ~3 ~65 ~30 white_concrete")
    player.execute("fill ~2 ~52 ~12 ~2 ~63 ~28 purple_concrete")
    player.execute("fill ~1 ~54 ~14 ~1 ~61 ~26 black_concrete")
    player.execute("fill ~1 ~58 ~18 ~1 ~60 ~20 white_concrete")

    # まつげ
    player.execute("fill ~2 ~65 ~-30 ~2 ~67 ~-10 black_wool")
    player.execute("fill ~2 ~65 ~10 ~2 ~67 ~30 black_wool")

    # 口（小さくてかわいい）
    player.execute("fill ~2 ~35 ~-5 ~2 ~37 ~5 pink_concrete")

    # ほっぺ（赤面）
    player.execute("fill ~2 ~45 ~-35 ~2 ~48 ~-32 red_concrete")
    player.execute("fill ~2 ~45 ~32 ~2 ~48 ~35 red_concrete")

    # ハートマーク装飾
    player.execute("fill ~1 ~55 ~0 ~1 ~57 ~2 red_concrete")
    player.execute("fill ~1 ~55 ~-2 ~1 ~57 ~0 red_concrete")
    player.execute("fill ~1 ~53 ~-1 ~1 ~55 ~1 red_concrete")

    player.say("§a超巨大アニメ顔完成！かわいい！")

def draw_chibi():
    """ちびキャラ - 2頭身（約30×40ブロック）"""
    player.say("§dちびキャラを描きます...")

    # 頭（でかい）
    player.execute("fill ~1 ~25 ~-10 ~1 ~40 ~10 peach_terracotta")

    # 髪
    player.execute("fill ~1 ~35 ~-12 ~1 ~42 ~12 orange_wool")

    # 目（でかい）
    player.execute("fill ~1 ~30 ~-7 ~1 ~33 ~-3 black_concrete")
    player.execute("fill ~1 ~30 ~3 ~1 ~33 ~7 black_concrete")
    player.execute("setblock ~1 ~32 ~-5 white_concrete")
    player.execute("setblock ~1 ~32 ~5 white_concrete")

    # 口
    player.execute("fill ~1 ~27 ~-1 ~1 ~27 ~1 pink_concrete")

    # 体（小さい）
    player.execute("fill ~1 ~15 ~-5 ~1 ~25 ~5 light_blue_wool")

    # 手
    player.execute("fill ~1 ~18 ~-7 ~1 ~22 ~-6 peach_terracotta")
    player.execute("fill ~1 ~18 ~6 ~1 ~22 ~7 peach_terracotta")

    # 足
    player.execute("fill ~1 ~10 ~-3 ~1 ~15 ~-1 white_concrete")
    player.execute("fill ~1 ~10 ~1 ~1 ~15 ~3 white_concrete")

    player.say("§aちびキャラ完成！2頭身かわいい！")

def on_art_help():
    """ピクセルアートのヘルプ"""
    player.say("§d=== ピクセルアート ===")
    player.say("§e!girl - 立っている女の子（40×60）")
    player.say("§e!catgirl - 猫耳女の子（50×50）")
    player.say("§e!princess - プリンセス（80×100）")
    player.say("§e!anime - アニメ顔（100×100）")
    player.say("§e!chibi - ちびキャラ（30×40）")

# コマンド登録
player.on_chat("girl", draw_girl_standing)
player.on_chat("catgirl", draw_cat_girl)
player.on_chat("princess", draw_princess)
player.on_chat("anime", draw_anime_face)
player.on_chat("chibi", draw_chibi)
player.on_chat("art", on_art_help)

# メッセージ
player.say("§d=== ピクセルアート起動！ ===")
player.say("§a'!art' でヘルプ表示")