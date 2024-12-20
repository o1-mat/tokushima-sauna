# Tokushima Sauna 

## アプリケーションの概要
「Tokushima Sauna」は、私の生まれ育った徳島県にある温泉・サウナ施設の魅力を広く伝えることを目的とした情報共有型のプラットフォームです。
徳島県の豊かな自然や文化と調和した温泉・サウナ施設の特長を紹介し、観光客や地元住民がそれぞれのニーズに合った施設を見つけられる場を提供します。

## リンク 
- **GitHub リポジトリ**　[Tokushima Sauna - GitHub]　　https://github.com/o1-mat/tokushima-sauna
- **デプロイされたアプリケーション**　[Tokushima Sauna アプリケーション]　　https://tokushima-sauna-d97c26d92e22.herokuapp.com/

### 主な機能
- **ユーザー認証** : 登録、ログイン、アカウント管理が可能。
- **施設情報** : 温泉・サウナ施設の詳細情報を閲覧可能。
- **検索フィルタ** : 希望条件に合った温泉・サウナ施設を簡単に見つけられる。
- **お気に入り登録** : 気に入った施設をお気に入りとして登録可能。
- **レビュー機能** : 会員登録済みのユーザーが施設のレビューを投稿可能。
- **管理者ダッシュボード** : 施設情報の更新やユーザーフィードバックの管理が可能。

## 使用技術
### フロントエンド
- **HTML** : コンテンツ構造の作成。
- **CSS** : スタイリングとレスポンシブデザインを実現。
- **Bootstrap** : ユーザーインターフェースの一貫性と効率的なレスポンシブデザインを実現。
### バックエンド
- **Python (Django フレームワーク)** : ビジネスロジック、データ処理、ユーザー認証を担当。
### データベース
- **PostgreSQL** : データを安全かつ効率的に保存。

### デプロイ
- **Heroku** : クラウドベースのホスティングサービス。
- **Cloudinary** : メディア管理と画像最適化のためのサービス。

## 設計
Django が提供する Model-View-Template (MVT) デザインパターンを採用。
- **モデル (Model)** : アプリケーションで扱うデータ構造を定義します。施設情報やお気に入り・レビュー情報をデータベースで管理。
- **ビュー (View)** : ユーザーからのリクエストを処理し、適切なレスポンスを生成。
e.g. 施設の一覧ページや詳細情報ページへのデータ取得
- **テンプレート (Template)** : 動的なHTMLコンテンツを生成し、ユーザーに表示されるページのレイアウトやデザインを管理

## 今後の改善点
- **マップ機能** : 現在地や指定エリア周辺のサウナ施設を地図上に表示する機能を追加。
- **評価ランキング機能** : 全施設の評価スコアを集計し、トップ５などのランキング形式で表示する機能を追加。