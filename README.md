# Tokushima Sauna 

## アプリケーションの概要
「Tokushima Sauna」は、私の地元である徳島県の豊かな自然と調和した温泉・サウナ施設の魅力を、より多くの人に伝えることを目的とした情報共有型プラットフォームです。 


## 作成に至った経緯
大学時代に温泉やサウナの魅力に触れ、その文化に惹かれました。一方で、地元徳島県の自然と調和した温泉やサウナの魅力が十分に知られていない現状に課題を感じました。
そこで、この魅力を多くの人に届けたいという思いから、アプリケーションの開発に取り組みました。


## リンク 
- **GitHub リポジトリ** : https://github.com/o1-mat/tokushima-sauna
- **デプロイされたアプリケーション** : https://tokushima-sauna-d97c26d92e22.herokuapp.com/


## 画面遷移図
### ユーザー側
![画面遷移図(ユーザー側) ](https://github.com/user-attachments/assets/0f9eea3b-742b-405c-80f6-a3c856db3bff)
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
- **HTML5** : コンテンツ構造の作成。
- **CSS3** : スタイリングとレスポンシブデザイン。
- **Bootstrap 5.2** : ユーザーインターフェースの効率的な構築
### バックエンド
- **Python 3.10** : アプリケーションのビジネスロジックを構築。
- **Django 5.1.4** : MVTパターンを採用し、データ処理とユーザー認証を実現。
- **Django-Allauth 65.3.0** : ユーザー認証とソーシャルログインの簡素化。
- **Gunicorn 23.0.0** : PythonアプリケーションのWSGI HTTPサーバー。
### データベース
- **PostgreSQL** : データを安全かつ効率的に保存。
- **PostgreSQL 14** : 高性能なリレーショナルデータベース。
- **Psycopg2 2.9.10** : PostgreSQL用Pythonアダプター。
- **Django-Database-URL 2.3.0** : データベースURL構成の簡易化。
### メディア管理
- **Cloudinary 1.41.0** : 画像最適化とクラウドストレージ。
- **Django-Cloudinary-Storage 0.3.0** : Cloudinaryとの統合。
### デプロイ
- **Heroku** : クラウドベースのホスティングサービス。
- **Django-Heroku 0.3.1** : メディア管理と画像最適化のためのサービス。
- **Whitenoise 6.8.2** : 静的ファイルの効率的な配信。
### その他ライブラリ
- **Requests 2.32.3** : HTTPリクエスト処理。
- **Pillow 11.0.0** : 画像操作ライブラリ。
- **SQLParse 0.5.3** : SQL文解析ライブラリ。


## 設計
Django が提供する Model-View-Template (MVT) デザインパターンを採用。
- **モデル (Model)** : アプリケーションで扱うデータ構造を定義する。施設情報やお気に入り・レビュー情報をデータベースに保存。
- **ビュー (View)** : ユーザーからのリクエストを受け取り、モデルからデータを取得し、テンプレートに渡す。
- **テンプレート (Template)** : ビューから受け取ったデータをHTMLに埋め込み、ユーザーに見える形で表示。


## ER図（DBテーブル設計）
![ER図](https://github.com/user-attachments/assets/0b4cfa65-494b-4c1c-8c7d-e0b3d39a8806)


## 今後の改善点
- **マップ機能** :  Google Maps API を活用し、施設の位置情報をインタラクティブに表示する機能を追加。
- **評価ランキング機能** : Django ORM を用いてデータベースの評価を集計してランキングリストを生成。フロントエンドには JavaScript を用いてユーザー操作に応じてランキングをリアルタイムで更新する機能を実装。
