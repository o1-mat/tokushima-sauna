# Tokushima Sauna 

## アプリケーションの概要
「Tokushima Sauna」は、私の生まれ育った徳島県にある温泉・サウナ施設の魅力を広く伝えることを目的とした情報共有型のプラットフォームです。
徳島県の豊かな自然と調和した温泉・サウナ施設の特長を紹介し、観光客や地元住民がそれぞれのニーズに合った施設を見つけられる場を提供します。


## リンク 
- **GitHub リポジトリ**
[Tokushima Sauna - GitHub]　　https://github.com/o1-mat/tokushima-sauna
- **デプロイされたアプリケーション**
[Tokushima Sauna アプリケーション]　　https://tokushima-sauna-d97c26d92e22.herokuapp.com/


## 画面遷移図
### ユーザー側
![画面遷移図(ユーザー側) ](https://github.com/user-attachments/assets/726ac07b-02fc-4424-8c0f-e07f268bdd66)
### 管理者側
![画面遷移図(管理者側) ](https://github.com/user-attachments/assets/b88fd31a-cf81-4d7e-b4ed-e888cc3d22a5)


## アプリケーション画面のプレビュー
![プレビュー検索フィルタ](https://github.com/user-attachments/assets/adf748c1-1fc0-414f-a3ea-fd8817bda3d2)
![プレビュー施設情報](https://github.com/user-attachments/assets/365dc679-d390-4254-a0dd-9a3dab015d25)
![プレビューお気に入り登録](https://github.com/user-attachments/assets/8df521d7-847e-4879-94d1-2c7b68cc4514)
![プレビューレビュー投稿](https://github.com/user-attachments/assets/df6a9c21-e533-4631-a100-b4b80554e747)
![プレビューユーザー認証](https://github.com/user-attachments/assets/45c0bca7-5276-4934-9b0e-393cf34bc67d)
![プレビュー管理者ダッシュボード](https://github.com/user-attachments/assets/9beaf762-6393-4f29-8ba2-10fae7b55f17)


## 主な機能
- **検索フィルタ** : 希望条件に合った温泉・サウナ施設を簡単に見つけられる。
- **施設情報** : 温泉・サウナ施設の詳細情報を閲覧可能。
- **お気に入り登録** : 気に入った施設をお気に入りとして登録可能。
- **レビュー投稿** : 会員登録済みのユーザーが施設のレビューを投稿可能。
- **ユーザー認証** : 登録、ログイン、アカウント管理が可能。
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
