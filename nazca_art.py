# Minecraft Education Edition - ナスカの地上絵ジェネレーター
# 超巨大200x200サイズで空から見ないとわからない地上絵を描く

def draw_hummingbird():
    """ハチドリ - ナスカの地上絵で最も有名な図柄（200×200ブロック）"""
    player.say("§6超巨大なハチドリを描きます（200×200）...")

    # 地面を平らにする（白い砂漠を作る）
    player.execute("fill ~-100 ~-1 ~-100 ~100 ~-1 ~100 sandstone")

    # ハチドリの本体（黒曜石で描画）
    # 胴体（中央の太い部分）
    player.execute("fill ~-40 ~ ~-10 ~40 ~ ~10 obsidian")
    player.execute("fill ~-35 ~ ~-12 ~35 ~ ~12 obsidian")

    # 頭部
    player.execute("fill ~41 ~ ~-6 ~60 ~ ~6 obsidian")
    player.execute("fill ~55 ~ ~-4 ~65 ~ ~4 obsidian")

    # くちばし（超長い - ハチドリの特徴）
    player.execute("fill ~66 ~ ~-2 ~95 ~ ~2 obsidian")
    player.execute("fill ~96 ~ ~-1 ~100 ~ ~1 obsidian")

    # 上の翼（大きく広げた翼）
    player.execute("fill ~-20 ~ ~13 ~20 ~ ~16 obsidian")
    player.execute("fill ~-30 ~ ~17 ~10 ~ ~22 obsidian")
    player.execute("fill ~-40 ~ ~23 ~0 ~ ~50 obsidian")
    player.execute("fill ~-35 ~ ~51 ~-10 ~ ~60 obsidian")
    player.execute("fill ~-30 ~ ~61 ~-15 ~ ~70 obsidian")
    player.execute("fill ~-25 ~ ~71 ~-20 ~ ~80 obsidian")

    # 下の翼（対称的に）
    player.execute("fill ~-20 ~ ~-16 ~20 ~ ~-13 obsidian")
    player.execute("fill ~-30 ~ ~-22 ~10 ~ ~-17 obsidian")
    player.execute("fill ~-40 ~ ~-50 ~0 ~ ~-23 obsidian")
    player.execute("fill ~-35 ~ ~-60 ~-10 ~ ~-51 obsidian")
    player.execute("fill ~-30 ~ ~-70 ~-15 ~ ~-61 obsidian")
    player.execute("fill ~-25 ~ ~-80 ~-20 ~ ~-71 obsidian")

    # 尾羽（広がった美しい尾）
    player.execute("fill ~-41 ~ ~-4 ~-50 ~ ~4 obsidian")
    player.execute("fill ~-51 ~ ~-2 ~-70 ~ ~2 obsidian")
    player.execute("fill ~-71 ~ ~-6 ~-80 ~ ~-2 obsidian")
    player.execute("fill ~-71 ~ ~2 ~-80 ~ ~6 obsidian")
    player.execute("fill ~-81 ~ ~-8 ~-90 ~ ~-4 obsidian")
    player.execute("fill ~-81 ~ ~4 ~-90 ~ ~8 obsidian")

    player.say("§a超巨大ハチドリ完成！空から見てください！")

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

def on_help():
    """使い方を表示"""
    player.say("§b=== 超巨大ナスカの地上絵（200×200） ===")
    player.say("§e!bird - ハチドリ")
    player.say("§e!monkey - サル（渦巻き尻尾）")
    player.say("§e!spider - クモ（8本足）")
    player.say("§e!tree - 生命の樹")
    player.say("§e!condor - コンドル（翼を広げた）")
    player.say("§e!spiral - カラフル渦巻き")
    player.say("§c※200×200の超巨大サイズ！")
    player.say("§a高度Y=150以上から見ることを推奨")

# コマンド登録
player.on_chat("bird", draw_hummingbird)
player.on_chat("monkey", draw_monkey)
player.on_chat("spider", draw_spider)
player.on_chat("tree", draw_tree)
player.on_chat("condor", draw_condor)
player.on_chat("spiral", draw_spiral)
player.on_chat("nazca", on_help)

# 起動メッセージ
player.say("§6=== 超巨大ナスカアート起動！ ===")
player.say("§c200×200サイズにアップグレード！")
player.say("§a'!nazca' でヘルプ表示")