# Minecraft Education Edition - ナスカの地上絵ジェネレーター
# 超巨大200x200サイズで空から見ないとわからない地上絵を描く

def draw_hummingbird():
    """ハチドリ - ナスカの地上絵で最も有名な図柄（200×200ブロック）"""
    player.say("§6本物のナスカのハチドリを描きます（200×200）...")

    # 地面を平らにする（ナスカ砂漠を再現）
    player.execute("fill ~-100 ~-1 ~-100 ~100 ~-1 ~100 sandstone")

    # ナスカの線画スタイル（線の太さ3-4ブロック）

    # 長いくちばし（左に向かって伸びる）
    player.execute("fill ~-100 ~ ~-2 ~-40 ~ ~2 red_sandstone")
    player.execute("fill ~-100 ~ ~-1 ~-45 ~ ~1 red_sandstone")

    # 頭部（小さめ）
    player.execute("fill ~-40 ~ ~-5 ~-30 ~ ~5 red_sandstone")
    player.execute("fill ~-35 ~ ~-6 ~-28 ~ ~6 red_sandstone")

    # 首から胴体へのライン（細い首）
    player.execute("fill ~-30 ~ ~-3 ~-20 ~ ~3 red_sandstone")

    # 胴体（中央の膨らみ）
    player.execute("fill ~-20 ~ ~-8 ~10 ~ ~8 red_sandstone")
    player.execute("fill ~-15 ~ ~-10 ~5 ~ ~10 red_sandstone")

    # 後部（尾に向かって細くなる）
    player.execute("fill ~10 ~ ~-5 ~30 ~ ~5 red_sandstone")
    player.execute("fill ~25 ~ ~-3 ~40 ~ ~3 red_sandstone")

    # 上の翼（左斜め上に伸びる長い線）
    player.execute("fill ~-10 ~ ~8 ~-5 ~ ~12 red_sandstone")
    player.execute("fill ~-15 ~ ~12 ~-10 ~ ~30 red_sandstone")
    player.execute("fill ~-20 ~ ~30 ~-15 ~ ~50 red_sandstone")
    player.execute("fill ~-25 ~ ~50 ~-20 ~ ~70 red_sandstone")
    player.execute("fill ~-30 ~ ~70 ~-25 ~ ~85 red_sandstone")
    player.execute("fill ~-35 ~ ~85 ~-30 ~ ~95 red_sandstone")

    # 上の翼（右斜め上に伸びる長い線）
    player.execute("fill ~5 ~ ~8 ~10 ~ ~12 red_sandstone")
    player.execute("fill ~10 ~ ~12 ~20 ~ ~25 red_sandstone")
    player.execute("fill ~20 ~ ~25 ~30 ~ ~40 red_sandstone")
    player.execute("fill ~30 ~ ~40 ~40 ~ ~55 red_sandstone")
    player.execute("fill ~40 ~ ~55 ~50 ~ ~70 red_sandstone")
    player.execute("fill ~50 ~ ~70 ~60 ~ ~80 red_sandstone")

    # 下の翼（左斜め下に伸びる長い線）
    player.execute("fill ~-10 ~ ~-12 ~-5 ~ ~-8 red_sandstone")
    player.execute("fill ~-15 ~ ~-30 ~-10 ~ ~-12 red_sandstone")
    player.execute("fill ~-20 ~ ~-50 ~-15 ~ ~-30 red_sandstone")
    player.execute("fill ~-25 ~ ~-70 ~-20 ~ ~-50 red_sandstone")
    player.execute("fill ~-30 ~ ~-85 ~-25 ~ ~-70 red_sandstone")
    player.execute("fill ~-35 ~ ~-95 ~-30 ~ ~-85 red_sandstone")

    # 下の翼（右斜め下に伸びる長い線）
    player.execute("fill ~5 ~ ~-12 ~10 ~ ~-8 red_sandstone")
    player.execute("fill ~10 ~ ~-25 ~20 ~ ~-12 red_sandstone")
    player.execute("fill ~20 ~ ~-40 ~30 ~ ~-25 red_sandstone")
    player.execute("fill ~30 ~ ~-55 ~40 ~ ~-40 red_sandstone")
    player.execute("fill ~40 ~ ~-70 ~50 ~ ~-55 red_sandstone")
    player.execute("fill ~50 ~ ~-80 ~60 ~ ~-70 red_sandstone")

    # 尾羽（2本に分かれた長い尾）
    player.execute("fill ~40 ~ ~-2 ~50 ~ ~2 red_sandstone")
    player.execute("fill ~50 ~ ~-4 ~65 ~ ~0 red_sandstone")
    player.execute("fill ~65 ~ ~-8 ~80 ~ ~-4 red_sandstone")
    player.execute("fill ~80 ~ ~-12 ~95 ~ ~-8 red_sandstone")

    player.execute("fill ~50 ~ ~0 ~65 ~ ~4 red_sandstone")
    player.execute("fill ~65 ~ ~4 ~80 ~ ~8 red_sandstone")
    player.execute("fill ~80 ~ ~8 ~95 ~ ~12 red_sandstone")

    player.say("§a本物のナスカのハチドリ完成！一筆書きの美しさを再現！")

def draw_monkey():
    """サル - 渦巻き尻尾が特徴的（200×200ブロック）"""
    player.say("§6超巨大なサルを描きます（200×200）...")

    # 地面を平らにする
    player.execute("fill ~-100 ~-1 ~-100 ~100 ~-1 ~100 sandstone")

    # 頭（大きな丸い頭）
    player.execute("fill ~-20 ~ ~70 ~20 ~ ~90 coal_block")
    player.execute("fill ~-15 ~ ~75 ~15 ~ ~85 coal_block")

    # 顔の詳細（目と口）
    player.execute("fill ~-10 ~ ~78 ~-5 ~ ~82 white_concrete")
    player.execute("fill ~5 ~ ~78 ~10 ~ ~82 white_concrete")

    # 胴体（太い）
    player.execute("fill ~-30 ~ ~30 ~30 ~ ~70 coal_block")
    player.execute("fill ~-25 ~ ~35 ~25 ~ ~65 coal_block")

    # 前足（長い）
    player.execute("fill ~31 ~ ~40 ~70 ~ ~45 coal_block")
    player.execute("fill ~65 ~ ~30 ~70 ~ ~50 coal_block")
    player.execute("fill ~-70 ~ ~40 ~-31 ~ ~45 coal_block")
    player.execute("fill ~-70 ~ ~30 ~-65 ~ ~50 coal_block")

    # 後ろ足（太く頑丈）
    player.execute("fill ~15 ~ ~25 ~25 ~ ~-20 coal_block")
    player.execute("fill ~20 ~ ~-20 ~25 ~ ~-30 coal_block")
    player.execute("fill ~-25 ~ ~25 ~-15 ~ ~-20 coal_block")
    player.execute("fill ~-25 ~ ~-20 ~-20 ~ ~-30 coal_block")

    # 渦巻き尻尾（ナスカの特徴的な螺旋）
    # 外側の大きな渦
    player.execute("fill ~-10 ~ ~-31 ~10 ~ ~-35 coal_block")
    player.execute("fill ~10 ~ ~-35 ~15 ~ ~-60 coal_block")
    player.execute("fill ~-15 ~ ~-60 ~15 ~ ~-65 coal_block")
    player.execute("fill ~-15 ~ ~-65 ~-10 ~ ~-85 coal_block")
    player.execute("fill ~-10 ~ ~-85 ~20 ~ ~-90 coal_block")
    player.execute("fill ~20 ~ ~-90 ~25 ~ ~-40 coal_block")

    # 内側の渦（螺旋の中心）
    player.execute("fill ~-5 ~ ~-45 ~5 ~ ~-75 coal_block")
    player.execute("fill ~0 ~ ~-60 ~12 ~ ~-65 coal_block")
    player.execute("fill ~5 ~ ~-50 ~10 ~ ~-70 coal_block")

    player.say("§a超巨大サル完成！渦巻き尻尾が見事です！")

def draw_spider():
    """クモ - シンプルだけど超巨大（200×200ブロック）"""
    player.say("§6超巨大なクモを描きます（200×200）...")

    # 地面を平らにする
    player.execute("fill ~-100 ~-1 ~-100 ~100 ~-1 ~100 sand")

    # 胴体（大きな楕円）
    player.execute("fill ~-20 ~ ~-30 ~20 ~ ~30 black_wool")
    player.execute("fill ~-15 ~ ~-35 ~15 ~ ~35 black_wool")

    # 頭（前方の丸）
    player.execute("fill ~-12 ~ ~31 ~12 ~ ~45 black_wool")
    player.execute("fill ~-8 ~ ~40 ~8 ~ ~50 black_wool")

    # 8本の足（クモの特徴）
    # 右側の4本
    player.execute("fill ~21 ~ ~20 ~60 ~ ~25 black_wool")
    player.execute("fill ~55 ~ ~20 ~60 ~ ~-20 black_wool")

    player.execute("fill ~21 ~ ~5 ~60 ~ ~10 black_wool")
    player.execute("fill ~55 ~ ~5 ~60 ~ ~-35 black_wool")

    player.execute("fill ~21 ~ ~-10 ~60 ~ ~-5 black_wool")
    player.execute("fill ~55 ~ ~-10 ~60 ~ ~-50 black_wool")

    player.execute("fill ~21 ~ ~-25 ~60 ~ ~-20 black_wool")
    player.execute("fill ~55 ~ ~-25 ~60 ~ ~-65 black_wool")

    # 左側の4本（対称）
    player.execute("fill ~-60 ~ ~20 ~-21 ~ ~25 black_wool")
    player.execute("fill ~-60 ~ ~20 ~-55 ~ ~-20 black_wool")

    player.execute("fill ~-60 ~ ~5 ~-21 ~ ~10 black_wool")
    player.execute("fill ~-60 ~ ~5 ~-55 ~ ~-35 black_wool")

    player.execute("fill ~-60 ~ ~-10 ~-21 ~ ~-5 black_wool")
    player.execute("fill ~-60 ~ ~-10 ~-55 ~ ~-50 black_wool")

    player.execute("fill ~-60 ~ ~-25 ~-21 ~ ~-20 black_wool")
    player.execute("fill ~-60 ~ ~-25 ~-55 ~ ~-65 black_wool")

    # 足の関節部分
    player.execute("fill ~58 ~ ~-18 ~65 ~ ~-22 black_wool")
    player.execute("fill ~58 ~ ~-48 ~65 ~ ~-52 black_wool")
    player.execute("fill ~-65 ~ ~-18 ~-58 ~ ~-22 black_wool")
    player.execute("fill ~-65 ~ ~-48 ~-58 ~ ~-52 black_wool")

    player.say("§a超巨大クモ完成！8本足が印象的！")

def draw_tree():
    """生命の樹 - 神秘的な図柄（200×200ブロック）"""
    player.say("§6生命の樹を描きます（200×200）...")

    # 地面を平らにする（緑の大地）
    player.execute("fill ~-100 ~-1 ~-100 ~100 ~-1 ~100 grass_block")

    # 幹（太い）
    player.execute("fill ~-8 ~ ~-80 ~8 ~ ~20 oak_log")
    player.execute("fill ~-6 ~ ~-70 ~6 ~ ~30 oak_log")

    # 根っこ（広がる根）
    player.execute("fill ~-5 ~ ~-90 ~5 ~ ~-80 oak_log")
    player.execute("fill ~-30 ~ ~-85 ~-8 ~ ~-80 oak_log")
    player.execute("fill ~8 ~ ~-85 ~30 ~ ~-80 oak_log")
    player.execute("fill ~-40 ~ ~-88 ~-30 ~ ~-85 oak_log")
    player.execute("fill ~30 ~ ~-88 ~40 ~ ~-85 oak_log")
    player.execute("fill ~-50 ~ ~-92 ~-40 ~ ~-88 oak_log")
    player.execute("fill ~40 ~ ~-92 ~50 ~ ~-88 oak_log")

    # 枝（左右対称で広がる）
    # レベル1（下の枝）
    player.execute("fill ~-40 ~ ~20 ~-9 ~ ~25 oak_leaves")
    player.execute("fill ~9 ~ ~20 ~40 ~ ~25 oak_leaves")
    player.execute("fill ~-50 ~ ~22 ~-40 ~ ~27 oak_leaves")
    player.execute("fill ~40 ~ ~22 ~50 ~ ~27 oak_leaves")

    # レベル2（中間の枝）
    player.execute("fill ~-60 ~ ~40 ~-20 ~ ~45 oak_leaves")
    player.execute("fill ~20 ~ ~40 ~60 ~ ~45 oak_leaves")
    player.execute("fill ~-30 ~ ~45 ~-10 ~ ~50 oak_leaves")
    player.execute("fill ~10 ~ ~45 ~30 ~ ~50 oak_leaves")

    # レベル3（上の枝）
    player.execute("fill ~-70 ~ ~60 ~-40 ~ ~65 oak_leaves")
    player.execute("fill ~40 ~ ~60 ~70 ~ ~65 oak_leaves")
    player.execute("fill ~-40 ~ ~65 ~40 ~ ~70 oak_leaves")

    # レベル4（頂上）
    player.execute("fill ~-30 ~ ~70 ~30 ~ ~80 oak_leaves")
    player.execute("fill ~-20 ~ ~80 ~20 ~ ~90 oak_leaves")
    player.execute("fill ~-10 ~ ~90 ~10 ~ ~95 oak_leaves")

    # 実（金のリンゴ - 生命の象徴）
    player.execute("fill ~-25 ~ ~50 ~-22 ~ ~53 gold_block")
    player.execute("fill ~22 ~ ~50 ~25 ~ ~53 gold_block")
    player.execute("fill ~-2 ~ ~75 ~2 ~ ~78 gold_block")
    player.execute("fill ~-15 ~ ~68 ~-12 ~ ~71 gold_block")
    player.execute("fill ~12 ~ ~68 ~15 ~ ~71 gold_block")

    player.say("§a生命の樹完成！神秘的で壮大です！")

def draw_condor():
    """コンドル - 巨大な翼を広げた鳥（200×200ブロック）"""
    player.say("§6巨大なコンドルを描きます（200×200）...")

    # 地面を平らにする
    player.execute("fill ~-100 ~-1 ~-100 ~100 ~-1 ~100 red_sandstone")

    # 胴体
    player.execute("fill ~-15 ~ ~-20 ~15 ~ ~20 black_concrete")

    # 頭と首
    player.execute("fill ~-8 ~ ~21 ~8 ~ ~35 black_concrete")
    player.execute("fill ~-5 ~ ~36 ~5 ~ ~45 black_concrete")

    # くちばし
    player.execute("fill ~-2 ~ ~46 ~2 ~ ~55 gray_concrete")

    # 左翼（巨大に広げた）
    player.execute("fill ~-16 ~ ~-10 ~-30 ~ ~10 black_concrete")
    player.execute("fill ~-31 ~ ~-15 ~-50 ~ ~15 black_concrete")
    player.execute("fill ~-51 ~ ~-20 ~-70 ~ ~20 black_concrete")
    player.execute("fill ~-71 ~ ~-25 ~-90 ~ ~25 black_concrete")

    # 左翼の羽根の詳細
    player.execute("fill ~-91 ~ ~-20 ~-95 ~ ~-10 black_concrete")
    player.execute("fill ~-91 ~ ~-5 ~-95 ~ ~5 black_concrete")
    player.execute("fill ~-91 ~ ~10 ~-95 ~ ~20 black_concrete")

    # 右翼（対称）
    player.execute("fill ~16 ~ ~-10 ~30 ~ ~10 black_concrete")
    player.execute("fill ~31 ~ ~-15 ~50 ~ ~15 black_concrete")
    player.execute("fill ~51 ~ ~-20 ~70 ~ ~20 black_concrete")
    player.execute("fill ~71 ~ ~-25 ~90 ~ ~25 black_concrete")

    # 右翼の羽根の詳細
    player.execute("fill ~91 ~ ~-20 ~95 ~ ~-10 black_concrete")
    player.execute("fill ~91 ~ ~-5 ~95 ~ ~5 black_concrete")
    player.execute("fill ~91 ~ ~10 ~95 ~ ~20 black_concrete")

    # 尾羽
    player.execute("fill ~-10 ~ ~-21 ~10 ~ ~-30 black_concrete")
    player.execute("fill ~-15 ~ ~-31 ~15 ~ ~-40 black_concrete")
    player.execute("fill ~-10 ~ ~-41 ~-5 ~ ~-50 black_concrete")
    player.execute("fill ~5 ~ ~-41 ~10 ~ ~-50 black_concrete")

    player.say("§aコンドル完成！翼幅190ブロックの壮大さ！")

def draw_spiral():
    """巨大な渦巻き - ナスカの謎の図形（200×200ブロック）"""
    player.say("§6巨大な渦巻きを描きます（200×200）...")

    # 地面を平らにする
    player.execute("fill ~-100 ~-1 ~-100 ~100 ~-1 ~100 white_concrete")

    # 外側から内側に向かって渦を描く
    # 最外周
    player.execute("fill ~-90 ~ ~-90 ~90 ~ ~-85 black_concrete")
    player.execute("fill ~85 ~ ~-90 ~90 ~ ~90 black_concrete")
    player.execute("fill ~-90 ~ ~85 ~90 ~ ~90 black_concrete")
    player.execute("fill ~-90 ~ ~-90 ~-85 ~ ~90 black_concrete")

    # 2周目
    player.execute("fill ~-80 ~ ~-80 ~80 ~ ~-75 blue_concrete")
    player.execute("fill ~75 ~ ~-80 ~80 ~ ~80 blue_concrete")
    player.execute("fill ~-80 ~ ~75 ~80 ~ ~80 blue_concrete")
    player.execute("fill ~-80 ~ ~-80 ~-75 ~ ~80 blue_concrete")

    # 3周目
    player.execute("fill ~-70 ~ ~-70 ~70 ~ ~-65 purple_concrete")
    player.execute("fill ~65 ~ ~-70 ~70 ~ ~70 purple_concrete")
    player.execute("fill ~-70 ~ ~65 ~70 ~ ~70 purple_concrete")
    player.execute("fill ~-70 ~ ~-70 ~-65 ~ ~70 purple_concrete")

    # 4周目
    player.execute("fill ~-60 ~ ~-60 ~60 ~ ~-55 red_concrete")
    player.execute("fill ~55 ~ ~-60 ~60 ~ ~60 red_concrete")
    player.execute("fill ~-60 ~ ~55 ~60 ~ ~60 red_concrete")
    player.execute("fill ~-60 ~ ~-60 ~-55 ~ ~60 red_concrete")

    # 5周目
    player.execute("fill ~-50 ~ ~-50 ~50 ~ ~-45 orange_concrete")
    player.execute("fill ~45 ~ ~-50 ~50 ~ ~50 orange_concrete")
    player.execute("fill ~-50 ~ ~45 ~50 ~ ~50 orange_concrete")
    player.execute("fill ~-50 ~ ~-50 ~-45 ~ ~50 orange_concrete")

    # 6周目
    player.execute("fill ~-40 ~ ~-40 ~40 ~ ~-35 yellow_concrete")
    player.execute("fill ~35 ~ ~-40 ~40 ~ ~40 yellow_concrete")
    player.execute("fill ~-40 ~ ~35 ~40 ~ ~40 yellow_concrete")
    player.execute("fill ~-40 ~ ~-40 ~-35 ~ ~40 yellow_concrete")

    # 7周目
    player.execute("fill ~-30 ~ ~-30 ~30 ~ ~-25 lime_concrete")
    player.execute("fill ~25 ~ ~-30 ~30 ~ ~30 lime_concrete")
    player.execute("fill ~-30 ~ ~25 ~30 ~ ~30 lime_concrete")
    player.execute("fill ~-30 ~ ~-30 ~-25 ~ ~30 lime_concrete")

    # 中心
    player.execute("fill ~-20 ~ ~-20 ~20 ~ ~20 gold_block")

    player.say("§aカラフルな巨大渦巻き完成！催眠術みたい！")

def draw_creeper():
    """クリーパー - マイクラの代表的モンスター（200×200ブロック）"""
    player.say("§2巨大なクリーパーを描きます（200×200）...")

    # 地面を平らにする（暗い大地）
    player.execute("fill ~-100 ~-1 ~-100 ~100 ~-1 ~100 black_concrete")

    # クリーパーの体（緑色）
    # 頭部（正方形）
    player.execute("fill ~-30 ~ ~40 ~30 ~ ~80 green_concrete")
    player.execute("fill ~-25 ~ ~35 ~25 ~ ~85 green_concrete")

    # 顔のパーツ（黒い穴）
    # 目
    player.execute("fill ~-20 ~ ~65 ~-10 ~ ~75 black_concrete")
    player.execute("fill ~10 ~ ~65 ~20 ~ ~75 black_concrete")

    # 鼻
    player.execute("fill ~-5 ~ ~55 ~5 ~ ~65 black_concrete")

    # 口（逆さ'T'字）
    player.execute("fill ~-15 ~ ~45 ~15 ~ ~50 black_concrete")
    player.execute("fill ~-5 ~ ~40 ~5 ~ ~55 black_concrete")

    # 胴体（長方形）
    player.execute("fill ~-25 ~ ~-20 ~25 ~ ~40 green_concrete")
    player.execute("fill ~-20 ~ ~-25 ~20 ~ ~45 green_concrete")

    # 4本の足
    player.execute("fill ~-20 ~ ~-60 ~-10 ~ ~-20 green_concrete")
    player.execute("fill ~10 ~ ~-60 ~20 ~ ~-20 green_concrete")
    player.execute("fill ~-15 ~ ~-65 ~-5 ~ ~-25 green_concrete")
    player.execute("fill ~5 ~ ~-65 ~15 ~ ~-25 green_concrete")

    # クリーパーの模様（黒い斑点）
    for i in range(-80, 81, 20):
        for j in range(-80, 81, 20):
            if (i + j) % 40 == 0:
                player.execute(f"fill ~{i-3} ~ ~{j-3} ~{i+3} ~ ~{j+3} black_concrete")

    player.say("§a巨大クリーパー完成！爆発しそう...！")

def draw_zombie():
    """ゾンビ - 腕を前に出したポーズ（200×200ブロック）"""
    player.say("§6巨大なゾンビを描きます（200×200）...")

    # 地面を平らにする（荒れた大地）
    player.execute("fill ~-100 ~-1 ~-100 ~100 ~-1 ~100 dirt")

    # ゾンビの体（肌色〜緑がかった色）
    # 頭部
    player.execute("fill ~-25 ~ ~50 ~25 ~ ~90 lime_terracotta")
    player.execute("fill ~-20 ~ ~45 ~20 ~ ~95 lime_terracotta")

    # 目（赤く光る）
    player.execute("fill ~-15 ~ ~70 ~-8 ~ ~77 red_concrete")
    player.execute("fill ~8 ~ ~70 ~15 ~ ~77 red_concrete")

    # 口（開いた口）
    player.execute("fill ~-10 ~ ~55 ~10 ~ ~65 black_concrete")
    player.execute("fill ~-8 ~ ~60 ~8 ~ ~62 white_concrete")

    # 胴体（シャツ - 青っぽい）
    player.execute("fill ~-20 ~ ~0 ~20 ~ ~50 blue_terracotta")
    player.execute("fill ~-25 ~ ~5 ~25 ~ ~45 blue_terracotta")

    # 腕（前に伸ばした）
    # 左腕
    player.execute("fill ~-50 ~ ~20 ~-25 ~ ~30 lime_terracotta")
    player.execute("fill ~-60 ~ ~15 ~-50 ~ ~25 lime_terracotta")

    # 右腕
    player.execute("fill ~25 ~ ~20 ~50 ~ ~30 lime_terracotta")
    player.execute("fill ~50 ~ ~15 ~60 ~ ~25 lime_terracotta")

    # 足
    player.execute("fill ~-15 ~ ~-50 ~-5 ~ ~0 brown_concrete")
    player.execute("fill ~5 ~ ~-50 ~15 ~ ~0 brown_concrete")

    # ズボン（茶色）
    player.execute("fill ~-18 ~ ~-30 ~18 ~ ~5 brown_terracotta")

    # 破れた服の表現
    for i in range(-60, 61, 15):
        player.execute(f"fill ~{i-2} ~ ~{i%30} ~{i+2} ~ ~{i%30+5} black_concrete")

    player.say("§aゾンビ完成！腕を前に出してる！")

def draw_skeleton():
    """スケルトン - 弓を構えたポーズ（200×200ブロック）"""
    player.say("§f巨大なスケルトンを描きます（200×200）...")

    # 地面を平らにする（骨の大地）
    player.execute("fill ~-100 ~-1 ~-100 ~100 ~-1 ~100 bone_block")

    # スケルトンの体（白い骨）
    # 頭蓋骨
    player.execute("fill ~-20 ~ ~60 ~20 ~ ~90 white_concrete")
    player.execute("fill ~-25 ~ ~65 ~25 ~ ~85 white_concrete")

    # 目窩（黒い穴）
    player.execute("fill ~-15 ~ ~75 ~-8 ~ ~82 black_concrete")
    player.execute("fill ~8 ~ ~75 ~15 ~ ~82 black_concrete")

    # 鼻の穴
    player.execute("fill ~-3 ~ ~70 ~3 ~ ~75 black_concrete")

    # 歯（ギザギザ）
    player.execute("fill ~-12 ~ ~65 ~12 ~ ~68 black_concrete")
    for i in range(-10, 11, 4):
        player.execute(f"fill ~{i} ~ ~68 ~{i+2} ~ ~70 white_concrete")

    # 肋骨（胴体）
    for rib in range(5):
        y_pos = 40 - rib * 8
        player.execute(f"fill ~-18 ~ ~{y_pos} ~18 ~ ~{y_pos+3} white_concrete")
        player.execute(f"fill ~-15 ~ ~{y_pos-2} ~15 ~ ~{y_pos+5} white_concrete")

    # 背骨
    player.execute("fill ~-2 ~ ~-20 ~2 ~ ~60 white_concrete")

    # 腕（弓を構える）
    # 左腕（弓を持つ）
    player.execute("fill ~-45 ~ ~30 ~-20 ~ ~40 white_concrete")
    # 右腕（弦を引く）
    player.execute("fill ~20 ~ ~35 ~40 ~ ~45 white_concrete")

    # 弓
    player.execute("fill ~-50 ~ ~25 ~-48 ~ ~45 brown_concrete")
    player.execute("fill ~-52 ~ ~27 ~-46 ~ ~29 white_wool")
    player.execute("fill ~-52 ~ ~41 ~-46 ~ ~43 white_wool")

    # 矢
    player.execute("fill ~-48 ~ ~34 ~35 ~ ~36 brown_concrete")
    player.execute("fill ~35 ~ ~33 ~38 ~ ~37 gray_concrete")

    # 足の骨
    player.execute("fill ~-12 ~ ~-60 ~-8 ~ ~-20 white_concrete")
    player.execute("fill ~8 ~ ~-60 ~12 ~ ~-20 white_concrete")

    # 足首
    player.execute("fill ~-15 ~ ~-65 ~-5 ~ ~-60 white_concrete")
    player.execute("fill ~5 ~ ~-65 ~15 ~ ~-60 white_concrete")

    player.say("§aスケルトン完成！弓矢で狙撃準備！")

def draw_enderman():
    """エンダーマン - 細長いシルエット（200×200ブロック）"""
    player.say("§5巨大なエンダーマンを描きます（200×200）...")

    # 地面を平らにする（エンドストーン）
    player.execute("fill ~-100 ~-1 ~-100 ~100 ~-1 ~100 end_stone")

    # エンダーマンの体（黒）
    # 頭部（細長い）
    player.execute("fill ~-15 ~ ~70 ~15 ~ ~95 black_concrete")
    player.execute("fill ~-12 ~ ~65 ~12 ~ ~100 black_concrete")

    # 目（紫色に光る）
    player.execute("fill ~-10 ~ ~85 ~-6 ~ ~89 purple_concrete")
    player.execute("fill ~6 ~ ~85 ~10 ~ ~89 purple_concrete")

    # 胴体（細長い）
    player.execute("fill ~-10 ~ ~20 ~10 ~ ~70 black_concrete")
    player.execute("fill ~-8 ~ ~15 ~8 ~ ~75 black_concrete")

    # 腕（長い）
    # 左腕
    player.execute("fill ~-35 ~ ~40 ~-15 ~ ~50 black_concrete")
    player.execute("fill ~-40 ~ ~10 ~-30 ~ ~45 black_concrete")

    # 右腕
    player.execute("fill ~15 ~ ~40 ~35 ~ ~50 black_concrete")
    player.execute("fill ~30 ~ ~10 ~40 ~ ~45 black_concrete")

    # 手（ブロックを持っている）
    player.execute("fill ~-45 ~ ~5 ~-35 ~ ~15 grass_block")
    player.execute("fill ~35 ~ ~5 ~45 ~ ~15 grass_block")

    # 足（長い）
    player.execute("fill ~-8 ~ ~-70 ~-4 ~ ~20 black_concrete")
    player.execute("fill ~4 ~ ~-70 ~8 ~ ~20 black_concrete")

    # テレポートパーティクル効果（紫のブロックで表現）
    for i in range(-90, 91, 30):
        for j in range(-90, 91, 30):
            if (i + j) % 60 == 0:
                player.execute(f"fill ~{i-2} ~ ~{j-2} ~{i+2} ~ ~{j+2} purple_wool")

    player.say("§aエンダーマン完成！テレポートしそう...")

def draw_pig():
    """ブタ - かわいい動物（200×200ブロック）"""
    player.say("§d巨大なブタを描きます（200×200）...")

    # 地面を平らにする（草原）
    player.execute("fill ~-100 ~-1 ~-100 ~100 ~-1 ~100 grass_block")

    # ブタの体（ピンク）
    # 頭部
    player.execute("fill ~-25 ~ ~40 ~25 ~ ~70 pink_concrete")
    player.execute("fill ~-30 ~ ~45 ~30 ~ ~65 pink_concrete")

    # 鼻（より濃いピンク）
    player.execute("fill ~-8 ~ ~70 ~8 ~ ~75 pink_terracotta")
    player.execute("fill ~-6 ~ ~75 ~6 ~ ~78 pink_terracotta")

    # 鼻の穴
    player.execute("fill ~-4 ~ ~76 ~-2 ~ ~77 black_concrete")
    player.execute("fill ~2 ~ ~76 ~4 ~ ~77 black_concrete")

    # 目
    player.execute("fill ~-15 ~ ~55 ~-10 ~ ~60 black_concrete")
    player.execute("fill ~10 ~ ~55 ~15 ~ ~60 black_concrete")

    # 耳（三角形）
    player.execute("fill ~-20 ~ ~45 ~-15 ~ ~50 pink_concrete")
    player.execute("fill ~15 ~ ~45 ~20 ~ ~50 pink_concrete")
    player.execute("fill ~-18 ~ ~50 ~-17 ~ ~52 pink_concrete")
    player.execute("fill ~17 ~ ~50 ~18 ~ ~52 pink_concrete")

    # 胴体（太い）
    player.execute("fill ~-35 ~ ~-20 ~35 ~ ~40 pink_concrete")
    player.execute("fill ~-40 ~ ~-15 ~40 ~ ~35 pink_concrete")

    # 4本の足（短い）
    player.execute("fill ~-25 ~ ~-50 ~-15 ~ ~-20 pink_concrete")
    player.execute("fill ~15 ~ ~-50 ~25 ~ ~-20 pink_concrete")
    player.execute("fill ~-30 ~ ~-55 ~-20 ~ ~-25 pink_concrete")
    player.execute("fill ~20 ~ ~-55 ~30 ~ ~-25 pink_concrete")

    # しっぽ（カール）
    player.execute("fill ~35 ~ ~0 ~45 ~ ~5 pink_concrete")
    player.execute("fill ~45 ~ ~5 ~50 ~ ~10 pink_concrete")
    player.execute("fill ~45 ~ ~10 ~40 ~ ~15 pink_concrete")

    player.say("§aブタ完成！かわいい〜！")

def on_help():
    """使い方を表示"""
    player.say("§b=== 超巨大ナスカの地上絵（200×200） ===")
    player.say("§6== 古代の図柄 ==")
    player.say("§e!bird - ハチドリ")
    player.say("§e!monkey - サル（渦巻き尻尾）")
    player.say("§e!spider - クモ（8本足）")
    player.say("§e!tree - 生命の樹")
    player.say("§e!condor - コンドル（翼を広げた）")
    player.say("§e!spiral - カラフル渦巻き")
    player.say("§a== Minecraftキャラクター ==")
    player.say("§2!creeper - クリーパー")
    player.say("§6!zombie - ゾンビ")
    player.say("§f!skeleton - スケルトン")
    player.say("§5!enderman - エンダーマン")
    player.say("§d!pig - ブタ")
    player.say("§c※200×200の超巨大サイズ！")
    player.say("§a高度Y=150以上から見ることを推奨")

# コマンド登録
# 古代ナスカの図柄
player.on_chat("bird", draw_hummingbird)
player.on_chat("monkey", draw_monkey)
player.on_chat("spider", draw_spider)
player.on_chat("tree", draw_tree)
player.on_chat("condor", draw_condor)
player.on_chat("spiral", draw_spiral)

# Minecraftキャラクター
player.on_chat("creeper", draw_creeper)
player.on_chat("zombie", draw_zombie)
player.on_chat("skeleton", draw_skeleton)
player.on_chat("enderman", draw_enderman)
player.on_chat("pig", draw_pig)

player.on_chat("nazca", on_help)

# 起動メッセージ
player.say("§6=== 超巨大ナスカアート起動！ ===")
player.say("§c200×200サイズにアップグレード！")
player.say("§a'!nazca' でヘルプ表示")