# Minecraft Education Edition Samples

マインクラフト教育版のサンプルコード集です。

## 概要

このリポジトリには、Minecraft Education Editionで使用できる様々なサンプルコードやプロジェクトが含まれています。教育現場での活用や、プログラミング学習の参考にご利用ください。

## 📁 プロジェクト一覧

### 1. 🦣 超大型巨人ビルダー (Colossal Titan Builder)
高さ60ブロックの巨大な巨人を自動建築するプログラムです。

**ファイル:**
- `colossal-titan-builder.js` - メインプログラム
- `colossal-titan-evaluation.md` - コード評価レポート
- `execution-guide-elementary.md` - 小学5年生向け実行ガイド

**コマンド:**

**巨人建築:**
- `setup_colossal` - 巨人建築用のビルダー設定
- `colossal` - 単体の超大型巨人を建築
- `army [数]` - 巨人軍団を建築（デフォルト5体、最大30体）
  - 例: `army` - 5体生成
  - 例: `army 10` - 10体生成
  - 例: `army 30` - 30体生成（最大）

**城壁建築:**
- `setup` - 城壁建築用のビルダー設定
- `wall [半径] [高さ]` - 円形城壁を建築
  - 例: `wall` - 半径30、高さ5の城壁（デフォルト）
  - 例: `wall 40` - 半径40、高さ5の城壁
  - 例: `wall 40 10` - 半径40、高さ10の城壁
  - 範囲: 半径10-50、高さ3-20

**特徴:**
- 段階的な建築プロセスで学習効果を高める
- 3D座標・円形計算の理解に最適
- パラメータによるカスタマイズ可能
- 建築中の座標ズレ防止機能

## 使い方

1. Minecraft Education Editionを起動
2. コードビルダーを開く（Cキー）
3. JavaScriptモードを選択
4. サンプルコードを開く
5. チャットでコマンドを入力して実行

## 必要環境

- Minecraft Education Edition
- Code Builder (MakeCode, Python, またはJavaScript)

## ライセンス

教育目的での使用を推奨します。

## 貢献

プルリクエストやイシューの報告を歓迎します。

## 連絡先

質問や提案がある場合は、イシューを作成してください。