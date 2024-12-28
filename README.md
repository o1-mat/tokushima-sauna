# Tokushima Sauna 

## アプリケーションの概要
「Tokushima Sauna」は、私の生まれ育った徳島県にある温泉・サウナ施設の魅力を広く伝えることを目的とした情報共有型のプラットフォームです。
徳島県の豊かな自然と調和した温泉・サウナ施設の特長を紹介し、観光客や地元住民がそれぞれのニーズに合った施設を見つけられる場を提供します。


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
[Uploading 画面遷移図.drawio…]()<mxfile host="app.diagrams.net" agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0" version="24.7.7" pages="2">
  <diagram name="ページ1" id="WWi67oSeqfHyLh5d5hT4">
    <mxGraphModel dx="1531" dy="789" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="BshGY1LEYWbQobP7QXll-54" value="会員情報" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;fillColor=#cce5ff;strokeColor=#36393d;" parent="1" vertex="1">
          <mxGeometry x="-185" y="40" width="160" height="330" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-55" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=1;" parent="BshGY1LEYWbQobP7QXll-54" vertex="1">
          <mxGeometry y="30" width="160" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-56" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-55" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-57" value="ID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-55" vertex="1">
          <mxGeometry x="30" width="130" height="30" as="geometry">
            <mxRectangle width="130" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-70" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-54" vertex="1">
          <mxGeometry y="60" width="160" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-71" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-70" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-72" value="名前" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-70" vertex="1">
          <mxGeometry x="30" width="130" height="30" as="geometry">
            <mxRectangle width="130" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-58" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-54" vertex="1">
          <mxGeometry y="90" width="160" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-59" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-58" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-60" value="メールアドレス" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-58" vertex="1">
          <mxGeometry x="30" width="130" height="30" as="geometry">
            <mxRectangle width="130" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-61" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-54" vertex="1">
          <mxGeometry y="120" width="160" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-62" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-61" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-63" value="パスワード" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-61" vertex="1">
          <mxGeometry x="30" width="130" height="30" as="geometry">
            <mxRectangle width="130" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-79" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-54" vertex="1">
          <mxGeometry y="150" width="160" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-80" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-79" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-81" value="郵便番号" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-79" vertex="1">
          <mxGeometry x="30" width="130" height="30" as="geometry">
            <mxRectangle width="130" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-76" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-54" vertex="1">
          <mxGeometry y="180" width="160" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-77" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-76" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-78" value="住所" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-76" vertex="1">
          <mxGeometry x="30" width="130" height="30" as="geometry">
            <mxRectangle width="130" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-73" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-54" vertex="1">
          <mxGeometry y="210" width="160" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-74" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-73" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-75" value="電話番号" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-73" vertex="1">
          <mxGeometry x="30" width="130" height="30" as="geometry">
            <mxRectangle width="130" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-64" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-54" vertex="1">
          <mxGeometry y="240" width="160" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-65" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-64" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-66" value="登録日" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-64" vertex="1">
          <mxGeometry x="30" width="130" height="30" as="geometry">
            <mxRectangle width="130" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="H-TTyzO7pXd-IZ4ivNvl-1" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-54" vertex="1">
          <mxGeometry y="270" width="160" height="30" as="geometry" />
        </mxCell>
        <mxCell id="H-TTyzO7pXd-IZ4ivNvl-2" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="H-TTyzO7pXd-IZ4ivNvl-1" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="H-TTyzO7pXd-IZ4ivNvl-3" value="更新日" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="H-TTyzO7pXd-IZ4ivNvl-1" vertex="1">
          <mxGeometry x="30" width="130" height="30" as="geometry">
            <mxRectangle width="130" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-67" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-54" vertex="1">
          <mxGeometry y="300" width="160" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-68" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-67" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-69" value="更新日" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-67" vertex="1">
          <mxGeometry x="30" width="130" height="30" as="geometry">
            <mxRectangle width="130" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-98" value="予約" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;fillColor=#dae8fc;strokeColor=#000000;" parent="1" vertex="1">
          <mxGeometry x="95" y="40" width="160" height="240" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-99" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=1;" parent="BshGY1LEYWbQobP7QXll-98" vertex="1">
          <mxGeometry y="30" width="160" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-100" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-99" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-101" value="ID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-99" vertex="1">
          <mxGeometry x="30" width="130" height="30" as="geometry">
            <mxRectangle width="130" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-102" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-98" vertex="1">
          <mxGeometry y="60" width="160" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-103" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-102" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-104" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-102" vertex="1">
          <mxGeometry x="30" width="130" height="30" as="geometry">
            <mxRectangle width="130" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-129" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=1;" parent="BshGY1LEYWbQobP7QXll-98" vertex="1">
          <mxGeometry y="90" width="160" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-130" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-129" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-131" value="店舗ID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-129" vertex="1">
          <mxGeometry x="30" width="130" height="30" as="geometry">
            <mxRectangle width="130" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-108" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-98" vertex="1">
          <mxGeometry y="120" width="160" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-109" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-108" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-110" value="予約日" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-108" vertex="1">
          <mxGeometry x="30" width="130" height="30" as="geometry">
            <mxRectangle width="130" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-111" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-98" vertex="1">
          <mxGeometry y="150" width="160" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-112" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-111" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-113" value="人数" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-111" vertex="1">
          <mxGeometry x="30" width="130" height="30" as="geometry">
            <mxRectangle width="130" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-135" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-98" vertex="1">
          <mxGeometry y="180" width="160" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-136" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-135" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-137" value="登録日" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-135" vertex="1">
          <mxGeometry x="30" width="130" height="30" as="geometry">
            <mxRectangle width="130" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-132" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-98" vertex="1">
          <mxGeometry y="210" width="160" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-133" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-132" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-134" value="更新日" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-132" vertex="1">
          <mxGeometry x="30" width="130" height="30" as="geometry">
            <mxRectangle width="130" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-124" value="" style="shape=table;startSize=0;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=0;align=center;resizeLast=1;strokeColor=none;fillColor=none;collapsible=0;" parent="1" vertex="1">
          <mxGeometry x="95" y="100" width="160" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-125" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=1;" parent="BshGY1LEYWbQobP7QXll-124" vertex="1">
          <mxGeometry width="160" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-126" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-125" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-127" value="会員ID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-125" vertex="1">
          <mxGeometry x="30" width="130" height="30" as="geometry">
            <mxRectangle width="130" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-212" value="レビュー" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;fillColor=#dae8fc;strokeColor=#000000;" parent="1" vertex="1">
          <mxGeometry x="95" y="440" width="160" height="240" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-213" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=1;" parent="BshGY1LEYWbQobP7QXll-212" vertex="1">
          <mxGeometry y="30" width="160" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-214" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-213" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-215" value="ID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-213" vertex="1">
          <mxGeometry x="30" width="130" height="30" as="geometry">
            <mxRectangle width="130" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-226" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=1;" parent="BshGY1LEYWbQobP7QXll-212" vertex="1">
          <mxGeometry y="60" width="160" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-227" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-226" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-228" value="会員ID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-226" vertex="1">
          <mxGeometry x="30" width="130" height="30" as="geometry">
            <mxRectangle width="130" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-230" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=1;" parent="BshGY1LEYWbQobP7QXll-212" vertex="1">
          <mxGeometry y="90" width="160" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-231" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-230" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-232" value="店舗ID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-230" vertex="1">
          <mxGeometry x="30" width="130" height="30" as="geometry">
            <mxRectangle width="130" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-222" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-212" vertex="1">
          <mxGeometry y="120" width="160" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-223" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-222" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-224" value="星の数" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-222" vertex="1">
          <mxGeometry x="30" width="130" height="30" as="geometry">
            <mxRectangle width="130" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-239" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-212" vertex="1">
          <mxGeometry y="150" width="160" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-240" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-239" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-241" value="コメント" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-239" vertex="1">
          <mxGeometry x="30" width="130" height="30" as="geometry">
            <mxRectangle width="130" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-236" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-212" vertex="1">
          <mxGeometry y="180" width="160" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-237" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-236" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-238" value="登録日" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-236" vertex="1">
          <mxGeometry x="30" width="130" height="30" as="geometry">
            <mxRectangle width="130" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-233" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-212" vertex="1">
          <mxGeometry y="210" width="160" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-234" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-233" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-235" value="更新日" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-233" vertex="1">
          <mxGeometry x="30" width="130" height="30" as="geometry">
            <mxRectangle width="130" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-242" value="店舗情報" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;fillColor=#dae8fc;strokeColor=#000000;" parent="1" vertex="1">
          <mxGeometry x="375" y="40" width="159.99999999999977" height="450" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-243" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=1;" parent="BshGY1LEYWbQobP7QXll-242" vertex="1">
          <mxGeometry y="30" width="159.99999999999977" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-244" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-243" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-245" value="ID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-243" vertex="1">
          <mxGeometry x="30" width="129.99999999999977" height="30" as="geometry">
            <mxRectangle width="129.99999999999977" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-256" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=1;" parent="BshGY1LEYWbQobP7QXll-242" vertex="1">
          <mxGeometry y="60" width="159.99999999999977" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-257" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-256" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-258" value="カテゴリID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-256" vertex="1">
          <mxGeometry x="30" width="129.99999999999977" height="30" as="geometry">
            <mxRectangle width="129.99999999999977" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-249" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-242" vertex="1">
          <mxGeometry y="90" width="159.99999999999977" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-250" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-249" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-251" value="店名" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-249" vertex="1">
          <mxGeometry x="30" width="129.99999999999977" height="30" as="geometry">
            <mxRectangle width="129.99999999999977" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-252" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-242" vertex="1">
          <mxGeometry y="120" width="159.99999999999977" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-253" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-252" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-254" value="画像" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-252" vertex="1">
          <mxGeometry x="30" width="129.99999999999977" height="30" as="geometry">
            <mxRectangle width="129.99999999999977" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-289" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-242" vertex="1">
          <mxGeometry y="150" width="159.99999999999977" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-290" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-289" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-291" value="説明" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-289" vertex="1">
          <mxGeometry x="30" width="129.99999999999977" height="30" as="geometry">
            <mxRectangle width="129.99999999999977" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-286" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-242" vertex="1">
          <mxGeometry y="180" width="159.99999999999977" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-287" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-286" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-288" value="価格帯 (下限)" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-286" vertex="1">
          <mxGeometry x="30" width="129.99999999999977" height="30" as="geometry">
            <mxRectangle width="129.99999999999977" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-283" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-242" vertex="1">
          <mxGeometry y="210" width="159.99999999999977" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-284" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-283" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-285" value="価格帯 (上限)" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-283" vertex="1">
          <mxGeometry x="30" width="129.99999999999977" height="30" as="geometry">
            <mxRectangle width="129.99999999999977" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-280" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-242" vertex="1">
          <mxGeometry y="240" width="159.99999999999977" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-281" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-280" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-282" value="営業時間 (開店)" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-280" vertex="1">
          <mxGeometry x="30" width="129.99999999999977" height="30" as="geometry">
            <mxRectangle width="129.99999999999977" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-277" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-242" vertex="1">
          <mxGeometry y="270" width="159.99999999999977" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-278" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-277" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-279" value="営業時間 (閉店)" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-277" vertex="1">
          <mxGeometry x="30" width="129.99999999999977" height="30" as="geometry">
            <mxRectangle width="129.99999999999977" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-274" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-242" vertex="1">
          <mxGeometry y="300" width="159.99999999999977" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-275" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-274" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-276" value="郵便番号" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-274" vertex="1">
          <mxGeometry x="30" width="129.99999999999977" height="30" as="geometry">
            <mxRectangle width="129.99999999999977" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-271" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-242" vertex="1">
          <mxGeometry y="330" width="159.99999999999977" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-272" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-271" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-273" value="住所" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-271" vertex="1">
          <mxGeometry x="30" width="129.99999999999977" height="30" as="geometry">
            <mxRectangle width="129.99999999999977" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-268" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-242" vertex="1">
          <mxGeometry y="360" width="159.99999999999977" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-269" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-268" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-270" value="電話番号" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-268" vertex="1">
          <mxGeometry x="30" width="129.99999999999977" height="30" as="geometry">
            <mxRectangle width="129.99999999999977" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-262" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-242" vertex="1">
          <mxGeometry y="390" width="159.99999999999977" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-263" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-262" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-264" value="登録日" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-262" vertex="1">
          <mxGeometry x="30" width="129.99999999999977" height="30" as="geometry">
            <mxRectangle width="129.99999999999977" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-259" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-242" vertex="1">
          <mxGeometry y="420" width="159.99999999999977" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-260" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-259" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-261" value="更新日" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-259" vertex="1">
          <mxGeometry x="30" width="129.99999999999977" height="30" as="geometry">
            <mxRectangle width="129.99999999999977" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-292" value="会社情報" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;fillColor=#dae8fc;strokeColor=#000000;" parent="1" vertex="1">
          <mxGeometry x="655" y="40" width="161" height="300" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-293" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=1;" parent="BshGY1LEYWbQobP7QXll-292" vertex="1">
          <mxGeometry y="30" width="161" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-294" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-293" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-295" value="ID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-293" vertex="1">
          <mxGeometry x="30" width="131" height="30" as="geometry">
            <mxRectangle width="131" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-296" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-292" vertex="1">
          <mxGeometry y="60" width="161" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-297" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-296" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-298" value="会社名" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-296" vertex="1">
          <mxGeometry x="30" width="131" height="30" as="geometry">
            <mxRectangle width="131" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-299" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-292" vertex="1">
          <mxGeometry y="90" width="161" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-300" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-299" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-301" value="代表" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-299" vertex="1">
          <mxGeometry x="30" width="131" height="30" as="geometry">
            <mxRectangle width="131" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-302" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-292" vertex="1">
          <mxGeometry y="120" width="161" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-303" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-302" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-304" value="設立日" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-302" vertex="1">
          <mxGeometry x="30" width="131" height="30" as="geometry">
            <mxRectangle width="131" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-317" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-292" vertex="1">
          <mxGeometry y="150" width="161" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-318" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-317" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-319" value="郵便番号" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-317" vertex="1">
          <mxGeometry x="30" width="131" height="30" as="geometry">
            <mxRectangle width="131" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-314" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-292" vertex="1">
          <mxGeometry y="180" width="161" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-315" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-314" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-316" value="住所" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-314" vertex="1">
          <mxGeometry x="30" width="131" height="30" as="geometry">
            <mxRectangle width="131" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-311" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-292" vertex="1">
          <mxGeometry y="210" width="161" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-312" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-311" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-313" value="事業内容" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-311" vertex="1">
          <mxGeometry x="30" width="131" height="30" as="geometry">
            <mxRectangle width="131" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-308" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-292" vertex="1">
          <mxGeometry y="240" width="161" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-309" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-308" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-310" value="登録日" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-308" vertex="1">
          <mxGeometry x="30" width="131" height="30" as="geometry">
            <mxRectangle width="131" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-305" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-292" vertex="1">
          <mxGeometry y="270" width="161" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-306" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-305" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-307" value="更新日" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-305" vertex="1">
          <mxGeometry x="30" width="131" height="30" as="geometry">
            <mxRectangle width="131" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-320" value="カテゴリ" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;fillColor=#dae8fc;strokeColor=#000000;" parent="1" vertex="1">
          <mxGeometry x="655" y="360" width="161" height="150" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-321" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=1;" parent="BshGY1LEYWbQobP7QXll-320" vertex="1">
          <mxGeometry y="30" width="161" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-322" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-321" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-323" value="ID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-321" vertex="1">
          <mxGeometry x="30" width="131" height="30" as="geometry">
            <mxRectangle width="131" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-324" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-320" vertex="1">
          <mxGeometry y="60" width="161" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-325" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-324" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-326" value="カテゴリ名" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-324" vertex="1">
          <mxGeometry x="30" width="131" height="30" as="geometry">
            <mxRectangle width="131" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-327" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-320" vertex="1">
          <mxGeometry y="90" width="161" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-328" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-327" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-329" value="登録日" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-327" vertex="1">
          <mxGeometry x="30" width="131" height="30" as="geometry">
            <mxRectangle width="131" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-330" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="BshGY1LEYWbQobP7QXll-320" vertex="1">
          <mxGeometry y="120" width="161" height="30" as="geometry" />
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-331" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-330" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-332" value="更新日" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="BshGY1LEYWbQobP7QXll-330" vertex="1">
          <mxGeometry x="30" width="131" height="30" as="geometry">
            <mxRectangle width="131" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-335" value="" style="edgeStyle=entityRelationEdgeStyle;fontSize=12;html=1;endArrow=ERzeroToMany;startArrow=ERzeroToOne;rounded=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" parent="1" target="BshGY1LEYWbQobP7QXll-226" edge="1">
          <mxGeometry width="100" height="100" relative="1" as="geometry">
            <mxPoint x="-25" y="90" as="sourcePoint" />
            <mxPoint x="45" y="105" as="targetPoint" />
            <Array as="points">
              <mxPoint x="55" y="110" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-337" value="" style="edgeStyle=entityRelationEdgeStyle;fontSize=12;html=1;endArrow=ERzeroToMany;startArrow=ERzeroToOne;rounded=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;exitX=0.991;exitY=0.078;exitDx=0;exitDy=0;exitPerimeter=0;" parent="1" target="BshGY1LEYWbQobP7QXll-125" edge="1">
          <mxGeometry width="100" height="100" relative="1" as="geometry">
            <mxPoint x="-25.440000000000055" y="73.34000000000003" as="sourcePoint" />
            <mxPoint x="96" y="116" as="targetPoint" />
            <Array as="points">
              <mxPoint x="-9" y="81" />
              <mxPoint x="56" y="101" />
              <mxPoint x="16" y="106" />
              <mxPoint x="6" y="109" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-346" value="" style="edgeStyle=entityRelationEdgeStyle;fontSize=12;html=1;endArrow=ERzeroToOne;startArrow=ERzeroToMany;rounded=0;endFill=0;startFill=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;" parent="1" source="BshGY1LEYWbQobP7QXll-129" edge="1">
          <mxGeometry width="100" height="100" relative="1" as="geometry">
            <mxPoint x="275" y="180" as="sourcePoint" />
            <mxPoint x="375" y="80" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-347" value="" style="edgeStyle=entityRelationEdgeStyle;fontSize=12;html=1;endArrow=ERzeroToOne;startArrow=ERzeroToMany;rounded=0;endFill=0;startFill=0;entryX=-0.007;entryY=0.724;entryDx=0;entryDy=0;entryPerimeter=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;" parent="1" source="BshGY1LEYWbQobP7QXll-230" edge="1">
          <mxGeometry width="100" height="100" relative="1" as="geometry">
            <mxPoint x="256" y="550" as="sourcePoint" />
            <mxPoint x="374.8800000000001" y="88.72000000000003" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="BshGY1LEYWbQobP7QXll-348" value="" style="edgeStyle=entityRelationEdgeStyle;fontSize=12;html=1;endArrow=ERzeroToOne;startArrow=ERzeroToMany;rounded=0;endFill=0;startFill=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" parent="1" target="BshGY1LEYWbQobP7QXll-321" edge="1">
          <mxGeometry width="100" height="100" relative="1" as="geometry">
            <mxPoint x="535" y="120" as="sourcePoint" />
            <mxPoint x="635" y="20" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="KEm-2Wa7JaH2dqeRTrk2-49" value="お気に入り" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;fillColor=#dae8fc;strokeColor=#000000;" parent="1" vertex="1">
          <mxGeometry x="95" y="700" width="160" height="150" as="geometry" />
        </mxCell>
        <mxCell id="KEm-2Wa7JaH2dqeRTrk2-50" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=1;" parent="KEm-2Wa7JaH2dqeRTrk2-49" vertex="1">
          <mxGeometry y="30" width="160" height="30" as="geometry" />
        </mxCell>
        <mxCell id="KEm-2Wa7JaH2dqeRTrk2-51" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="KEm-2Wa7JaH2dqeRTrk2-50" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="KEm-2Wa7JaH2dqeRTrk2-52" value="ID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;whiteSpace=wrap;html=1;" parent="KEm-2Wa7JaH2dqeRTrk2-50" vertex="1">
          <mxGeometry x="30" width="130" height="30" as="geometry">
            <mxRectangle width="130" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="KEm-2Wa7JaH2dqeRTrk2-53" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=1;" parent="KEm-2Wa7JaH2dqeRTrk2-49" vertex="1">
          <mxGeometry y="60" width="160" height="30" as="geometry" />
        </mxCell>
        <mxCell id="KEm-2Wa7JaH2dqeRTrk2-54" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="KEm-2Wa7JaH2dqeRTrk2-53" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="KEm-2Wa7JaH2dqeRTrk2-55" value="会員ID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;whiteSpace=wrap;html=1;" parent="KEm-2Wa7JaH2dqeRTrk2-53" vertex="1">
          <mxGeometry x="30" width="130" height="30" as="geometry">
            <mxRectangle width="130" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="KEm-2Wa7JaH2dqeRTrk2-56" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=1;" parent="KEm-2Wa7JaH2dqeRTrk2-49" vertex="1">
          <mxGeometry y="90" width="160" height="30" as="geometry" />
        </mxCell>
        <mxCell id="KEm-2Wa7JaH2dqeRTrk2-57" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="KEm-2Wa7JaH2dqeRTrk2-56" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="KEm-2Wa7JaH2dqeRTrk2-58" value="店舗ID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;whiteSpace=wrap;html=1;" parent="KEm-2Wa7JaH2dqeRTrk2-56" vertex="1">
          <mxGeometry x="30" width="130" height="30" as="geometry">
            <mxRectangle width="130" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="KEm-2Wa7JaH2dqeRTrk2-65" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="KEm-2Wa7JaH2dqeRTrk2-49" vertex="1">
          <mxGeometry y="120" width="160" height="30" as="geometry" />
        </mxCell>
        <mxCell id="KEm-2Wa7JaH2dqeRTrk2-66" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="KEm-2Wa7JaH2dqeRTrk2-65" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="KEm-2Wa7JaH2dqeRTrk2-67" value="登録日" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="KEm-2Wa7JaH2dqeRTrk2-65" vertex="1">
          <mxGeometry x="30" width="130" height="30" as="geometry">
            <mxRectangle width="130" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="KEm-2Wa7JaH2dqeRTrk2-78" value="有料会員" style="shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;fillColor=#dae8fc;strokeColor=#000000;" parent="1" vertex="1">
          <mxGeometry x="95" y="300" width="159.99999999999977" height="120" as="geometry" />
        </mxCell>
        <mxCell id="KEm-2Wa7JaH2dqeRTrk2-79" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=1;" parent="KEm-2Wa7JaH2dqeRTrk2-78" vertex="1">
          <mxGeometry y="30" width="159.99999999999977" height="30" as="geometry" />
        </mxCell>
        <mxCell id="KEm-2Wa7JaH2dqeRTrk2-80" value="PK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="KEm-2Wa7JaH2dqeRTrk2-79" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="KEm-2Wa7JaH2dqeRTrk2-81" value="ID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;whiteSpace=wrap;html=1;" parent="KEm-2Wa7JaH2dqeRTrk2-79" vertex="1">
          <mxGeometry x="30" width="129.99999999999977" height="30" as="geometry">
            <mxRectangle width="129.99999999999977" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="KEm-2Wa7JaH2dqeRTrk2-85" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=1;" parent="KEm-2Wa7JaH2dqeRTrk2-78" vertex="1">
          <mxGeometry y="60" width="159.99999999999977" height="30" as="geometry" />
        </mxCell>
        <mxCell id="KEm-2Wa7JaH2dqeRTrk2-86" value="FK" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;fontStyle=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="KEm-2Wa7JaH2dqeRTrk2-85" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="KEm-2Wa7JaH2dqeRTrk2-87" value="会員ID" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;fontStyle=5;overflow=hidden;whiteSpace=wrap;html=1;" parent="KEm-2Wa7JaH2dqeRTrk2-85" vertex="1">
          <mxGeometry x="30" width="129.99999999999977" height="30" as="geometry">
            <mxRectangle width="129.99999999999977" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="KEm-2Wa7JaH2dqeRTrk2-88" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom=0;" parent="KEm-2Wa7JaH2dqeRTrk2-78" vertex="1">
          <mxGeometry y="90" width="159.99999999999977" height="30" as="geometry" />
        </mxCell>
        <mxCell id="KEm-2Wa7JaH2dqeRTrk2-89" value="" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;editable=1;overflow=hidden;whiteSpace=wrap;html=1;" parent="KEm-2Wa7JaH2dqeRTrk2-88" vertex="1">
          <mxGeometry width="30" height="30" as="geometry">
            <mxRectangle width="30" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="KEm-2Wa7JaH2dqeRTrk2-90" value="コード" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;" parent="KEm-2Wa7JaH2dqeRTrk2-88" vertex="1">
          <mxGeometry x="30" width="129.99999999999977" height="30" as="geometry">
            <mxRectangle width="129.99999999999977" height="30" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="KEm-2Wa7JaH2dqeRTrk2-103" value="" style="edgeStyle=entityRelationEdgeStyle;fontSize=12;html=1;endArrow=ERzeroToMany;startArrow=ERzeroToOne;rounded=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;" parent="1" target="KEm-2Wa7JaH2dqeRTrk2-85" edge="1">
          <mxGeometry width="100" height="100" relative="1" as="geometry">
            <mxPoint x="-25" y="81" as="sourcePoint" />
            <mxPoint x="95" y="371" as="targetPoint" />
            <Array as="points">
              <mxPoint x="55" y="101" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="KEm-2Wa7JaH2dqeRTrk2-104" value="" style="edgeStyle=entityRelationEdgeStyle;fontSize=12;html=1;endArrow=ERzeroToMany;startArrow=ERzeroToOne;rounded=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" parent="1" target="KEm-2Wa7JaH2dqeRTrk2-53" edge="1">
          <mxGeometry width="100" height="100" relative="1" as="geometry">
            <mxPoint x="-25" y="97" as="sourcePoint" />
            <mxPoint x="70" y="630" as="targetPoint" />
            <Array as="points">
              <mxPoint x="55" y="117" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="KEm-2Wa7JaH2dqeRTrk2-105" value="" style="edgeStyle=entityRelationEdgeStyle;fontSize=12;html=1;endArrow=ERzeroToOne;startArrow=ERzeroToMany;rounded=0;endFill=0;startFill=0;entryX=-0.007;entryY=0.724;entryDx=0;entryDy=0;entryPerimeter=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;" parent="1" source="KEm-2Wa7JaH2dqeRTrk2-56" edge="1">
          <mxGeometry width="100" height="100" relative="1" as="geometry">
            <mxPoint x="256" y="550" as="sourcePoint" />
            <mxPoint x="375" y="97" as="targetPoint" />
          </mxGeometry>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
  <diagram id="bKsBdx8_17rImUnag6a6" name="ページ2">
    <mxGraphModel dx="2295" dy="1856" grid="0" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="0" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="uZVP7jplPoIl5v418rTI-21" style="edgeStyle=none;curved=1;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;fontSize=16;startSize=8;endSize=8;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1" source="uZVP7jplPoIl5v418rTI-2">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="-88.73331705729174" y="-575.6666666666666" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-2" value="トップページ" style="rounded=0;whiteSpace=wrap;html=1;fontStyle=1;fontSize=16;fontFamily=Verdana;" vertex="1" parent="1">
          <mxGeometry x="-318" y="-600" width="119" height="49" as="geometry" />
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-3" style="edgeStyle=none;curved=1;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.75;exitY=1;exitDx=0;exitDy=0;fontSize=16;startSize=8;endSize=8;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1" source="uZVP7jplPoIl5v418rTI-2" target="uZVP7jplPoIl5v418rTI-2">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-20" value="" style="endArrow=classic;html=1;rounded=0;fontSize=16;startSize=8;endSize=8;curved=1;entryX=0.017;entryY=0.5;entryDx=0;entryDy=0;entryPerimeter=0;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="-149" y="-476" as="sourcePoint" />
            <mxPoint x="-84.97699999999986" y="-476.5" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-23" value="検索結果" style="rounded=0;whiteSpace=wrap;html=1;fontStyle=1;fontSize=16;fontFamily=Verdana;" vertex="1" parent="1">
          <mxGeometry x="-85" y="-501" width="119" height="49" as="geometry" />
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-25" value="" style="endArrow=none;html=1;rounded=0;fontSize=16;startSize=8;endSize=8;curved=1;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="-150" y="-84" as="sourcePoint" />
            <mxPoint x="-150" y="-576" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-29" value="マイページ" style="rounded=0;whiteSpace=wrap;html=1;fontStyle=1;fontSize=16;fontFamily=Verdana;" vertex="1" parent="1">
          <mxGeometry x="-87" y="-403" width="119" height="49" as="geometry" />
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-30" value="新規登録" style="rounded=0;whiteSpace=wrap;html=1;fontStyle=1;fontSize=16;fontFamily=Verdana;" vertex="1" parent="1">
          <mxGeometry x="-87" y="-305" width="119" height="49" as="geometry" />
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-32" value="" style="endArrow=classic;html=1;rounded=0;fontSize=16;startSize=8;endSize=8;curved=1;entryX=0.017;entryY=0.5;entryDx=0;entryDy=0;entryPerimeter=0;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="-151" y="-379.17" as="sourcePoint" />
            <mxPoint x="-87" y="-379.17" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-33" value="" style="endArrow=classic;html=1;rounded=0;fontSize=16;startSize=8;endSize=8;curved=1;entryX=0.017;entryY=0.5;entryDx=0;entryDy=0;entryPerimeter=0;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="-150" y="-281.16999999999996" as="sourcePoint" />
            <mxPoint x="-86" y="-281.16999999999996" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-34" style="edgeStyle=none;curved=1;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.75;exitY=1;exitDx=0;exitDy=0;fontSize=16;startSize=8;endSize=8;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="196.25" y="-29" as="sourcePoint" />
            <mxPoint x="196.25" y="-29" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-37" value="施設詳細" style="rounded=0;whiteSpace=wrap;html=1;fontStyle=1;fontSize=16;fontFamily=Verdana;" vertex="1" parent="1">
          <mxGeometry x="-87" y="-600" width="119" height="49" as="geometry" />
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-40" value="" style="endArrow=classic;html=1;rounded=0;fontSize=16;startSize=8;endSize=8;curved=1;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="-28" y="-501" as="sourcePoint" />
            <mxPoint x="-28.170000000000016" y="-551" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-41" value="ログイン" style="rounded=0;whiteSpace=wrap;html=1;fontStyle=1;fontSize=16;fontFamily=Verdana;" vertex="1" parent="1">
          <mxGeometry x="-87" y="-207" width="119" height="49" as="geometry" />
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-42" value="" style="endArrow=classic;html=1;rounded=0;fontSize=16;startSize=8;endSize=8;curved=1;entryX=0.017;entryY=0.5;entryDx=0;entryDy=0;entryPerimeter=0;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="-150" y="-183.16999999999996" as="sourcePoint" />
            <mxPoint x="-86" y="-183.16999999999996" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-46" style="edgeStyle=none;curved=1;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;fontSize=16;startSize=8;endSize=8;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="142.26668294270826" y="-576.1666666666666" as="targetPoint" />
            <mxPoint x="32" y="-575.5" as="sourcePoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-47" value="レビュー一覧" style="rounded=0;whiteSpace=wrap;html=1;fontStyle=1;fontSize=16;fontFamily=Verdana;" vertex="1" parent="1">
          <mxGeometry x="143" y="-600" width="119" height="49" as="geometry" />
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-48" value="" style="endArrow=classic;html=1;rounded=0;fontSize=16;startSize=8;endSize=8;curved=1;entryX=0.017;entryY=0.5;entryDx=0;entryDy=0;entryPerimeter=0;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="78.97999999999999" y="-476" as="sourcePoint" />
            <mxPoint x="143.00300000000013" y="-476.5" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-49" value="" style="endArrow=none;html=1;rounded=0;fontSize=16;startSize=8;endSize=8;curved=1;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="78" y="-474" as="sourcePoint" />
            <mxPoint x="77.97999999999999" y="-576" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-50" value="お気に入り登録" style="rounded=0;whiteSpace=wrap;html=1;fontStyle=1;fontSize=16;fontFamily=Verdana;" vertex="1" parent="1">
          <mxGeometry x="143" y="-501" width="119" height="49" as="geometry" />
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-51" style="edgeStyle=none;curved=1;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;fontSize=16;startSize=8;endSize=8;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="372.26668294270826" y="-576.1666666666666" as="targetPoint" />
            <mxPoint x="262" y="-575.5" as="sourcePoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-52" value="レビュー投稿&lt;div style=&quot;font-size: 16px;&quot;&gt;(登録会員のみ)&lt;/div&gt;" style="rounded=0;whiteSpace=wrap;html=1;fontStyle=1;fontSize=16;fontFamily=Verdana;" vertex="1" parent="1">
          <mxGeometry x="373" y="-600" width="119" height="49" as="geometry" />
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-53" value="" style="endArrow=classic;html=1;rounded=0;fontSize=16;startSize=8;endSize=8;curved=1;entryX=0.017;entryY=0.5;entryDx=0;entryDy=0;entryPerimeter=0;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="308.98" y="-476" as="sourcePoint" />
            <mxPoint x="373.00300000000016" y="-476.5" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-54" value="" style="endArrow=none;html=1;rounded=0;fontSize=16;startSize=8;endSize=8;curved=1;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="308" y="-378" as="sourcePoint" />
            <mxPoint x="307.98" y="-576" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-55" value="レビュー編集" style="rounded=0;whiteSpace=wrap;html=1;fontStyle=1;fontSize=16;fontFamily=Verdana;" vertex="1" parent="1">
          <mxGeometry x="373" y="-501" width="119" height="49" as="geometry" />
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-56" value="" style="endArrow=classic;html=1;rounded=0;fontSize=16;startSize=8;endSize=8;curved=1;entryX=0.017;entryY=0.5;entryDx=0;entryDy=0;entryPerimeter=0;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="308.98" y="-378" as="sourcePoint" />
            <mxPoint x="373.00300000000016" y="-378.5" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-58" style="edgeStyle=none;curved=1;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;fontSize=16;startSize=8;endSize=8;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="432.5" y="-354" as="sourcePoint" />
            <mxPoint x="432.5" y="-354" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-60" value="レビュー削除" style="rounded=0;whiteSpace=wrap;html=1;fontStyle=1;fontSize=16;fontFamily=Verdana;" vertex="1" parent="1">
          <mxGeometry x="373" y="-403" width="119" height="49" as="geometry" />
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-61" style="edgeStyle=none;curved=1;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;fontSize=16;startSize=8;endSize=8;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="142.26668294270826" y="-379.16666666666663" as="targetPoint" />
            <mxPoint x="32" y="-378.5" as="sourcePoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-63" value="" style="endArrow=classic;html=1;rounded=0;fontSize=16;startSize=8;endSize=8;curved=1;entryX=0.017;entryY=0.5;entryDx=0;entryDy=0;entryPerimeter=0;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="78.98000000000002" y="-279" as="sourcePoint" />
            <mxPoint x="143.00300000000016" y="-279.5" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-64" value="" style="endArrow=none;html=1;rounded=0;fontSize=16;startSize=8;endSize=8;curved=1;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="78" y="-278" as="sourcePoint" />
            <mxPoint x="77.98000000000002" y="-379" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-65" value="会員情報編集" style="rounded=0;whiteSpace=wrap;html=1;fontStyle=1;fontSize=16;fontFamily=Verdana;" vertex="1" parent="1">
          <mxGeometry x="143" y="-403" width="119" height="49" as="geometry" />
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-67" style="edgeStyle=none;curved=1;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;fontSize=16;startSize=8;endSize=8;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="202.5" y="-256" as="sourcePoint" />
            <mxPoint x="202.5" y="-256" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-68" value="お気に入り一覧" style="rounded=0;whiteSpace=wrap;html=1;fontStyle=1;fontSize=16;fontFamily=Verdana;" vertex="1" parent="1">
          <mxGeometry x="143" y="-305" width="119" height="49" as="geometry" />
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-69" value="" style="endArrow=classic;html=1;rounded=0;fontSize=16;startSize=8;endSize=8;curved=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1" target="uZVP7jplPoIl5v418rTI-71">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="262" y="-280" as="sourcePoint" />
            <mxPoint x="326.02300000000014" y="-280.5" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-70" style="edgeStyle=none;curved=1;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;fontSize=16;startSize=8;endSize=8;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="385.52" y="-256" as="sourcePoint" />
            <mxPoint x="385.52" y="-256" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-71" value="お気に入り解除" style="rounded=0;whiteSpace=wrap;html=1;fontStyle=1;fontSize=16;fontFamily=Verdana;" vertex="1" parent="1">
          <mxGeometry x="373" y="-305" width="119" height="49" as="geometry" />
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-72" value="ログアウト" style="rounded=0;whiteSpace=wrap;html=1;fontStyle=1;fontSize=16;fontFamily=Verdana;" vertex="1" parent="1">
          <mxGeometry x="-87" y="-109" width="119" height="49" as="geometry" />
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-73" value="" style="endArrow=classic;html=1;rounded=0;fontSize=16;startSize=8;endSize=8;curved=1;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="-151" y="-84" as="sourcePoint" />
            <mxPoint x="-86" y="-84" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-75" style="edgeStyle=none;curved=1;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;fontSize=16;startSize=8;endSize=8;fontStyle=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;fontFamily=Verdana;" edge="1" parent="1" target="uZVP7jplPoIl5v418rTI-79">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="354" y="274" as="targetPoint" />
            <mxPoint x="261.75" y="274.5" as="sourcePoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-76" value="ログイン" style="rounded=0;whiteSpace=wrap;html=1;fontStyle=1;fontSize=16;fontFamily=Verdana;" vertex="1" parent="1">
          <mxGeometry x="-318" y="187" width="119" height="49" as="geometry" />
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-77" style="edgeStyle=none;curved=1;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.75;exitY=1;exitDx=0;exitDy=0;fontSize=16;startSize=8;endSize=8;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="227" y="236" as="sourcePoint" />
            <mxPoint x="227" y="236" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-79" value="施設詳細" style="rounded=0;whiteSpace=wrap;html=1;fontStyle=1;fontSize=16;fontFamily=Verdana;" vertex="1" parent="1">
          <mxGeometry x="371" y="250" width="119" height="49" as="geometry" />
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-81" value="施設登録" style="rounded=0;whiteSpace=wrap;html=1;fontStyle=1;fontSize=16;fontFamily=Verdana;" vertex="1" parent="1">
          <mxGeometry x="371" y="313" width="119" height="49" as="geometry" />
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-82" value="施設&lt;span style=&quot;background-color: initial; font-size: 16px;&quot;&gt;編集&lt;/span&gt;" style="rounded=0;whiteSpace=wrap;html=1;fontStyle=1;fontSize=16;fontFamily=Verdana;" vertex="1" parent="1">
          <mxGeometry x="371" y="376" width="119" height="49" as="geometry" />
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-83" value="" style="endArrow=classic;html=1;rounded=0;fontSize=16;startSize=8;endSize=8;curved=1;entryX=0.017;entryY=0.5;entryDx=0;entryDy=0;entryPerimeter=0;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="307" y="336.8299999999999" as="sourcePoint" />
            <mxPoint x="371" y="336.8299999999999" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-84" value="" style="endArrow=classic;html=1;rounded=0;fontSize=16;startSize=8;endSize=8;curved=1;entryX=0.017;entryY=0.5;entryDx=0;entryDy=0;entryPerimeter=0;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="308" y="399.83000000000004" as="sourcePoint" />
            <mxPoint x="372" y="399.83000000000004" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-87" value="施設削除" style="rounded=0;whiteSpace=wrap;html=1;fontStyle=1;fontSize=16;fontFamily=Verdana;" vertex="1" parent="1">
          <mxGeometry x="371" y="439" width="119" height="49" as="geometry" />
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-88" value="" style="endArrow=classic;html=1;rounded=0;fontSize=16;startSize=8;endSize=8;curved=1;entryX=0.017;entryY=0.5;entryDx=0;entryDy=0;entryPerimeter=0;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="308" y="462.83000000000004" as="sourcePoint" />
            <mxPoint x="372" y="462.83000000000004" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-89" value="ログアウト" style="rounded=0;whiteSpace=wrap;html=1;fontStyle=1;fontSize=16;fontFamily=Verdana;" vertex="1" parent="1">
          <mxGeometry x="142.75" y="1076" width="119" height="49" as="geometry" />
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-90" value="" style="endArrow=classic;html=1;rounded=0;fontSize=16;startSize=8;endSize=8;curved=1;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="86" y="1100" as="sourcePoint" />
            <mxPoint x="142" y="1100" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-91" style="edgeStyle=none;curved=1;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;fontSize=16;startSize=8;endSize=8;fontStyle=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;fontFamily=Verdana;" edge="1" parent="1" target="uZVP7jplPoIl5v418rTI-92">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="-87.73331705729174" y="211.33333333333337" as="targetPoint" />
            <mxPoint x="-198" y="211.5" as="sourcePoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-92" value="管理画面" style="rounded=0;whiteSpace=wrap;html=1;fontStyle=1;fontSize=16;fontFamily=Verdana;" vertex="1" parent="1">
          <mxGeometry x="-88" y="187" width="119" height="49" as="geometry" />
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-96" style="edgeStyle=none;curved=1;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;fontSize=16;startSize=8;endSize=8;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="141.26668294270826" y="211.33333333333337" as="targetPoint" />
            <mxPoint x="31" y="211.5" as="sourcePoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-97" style="edgeStyle=none;curved=1;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.75;exitY=1;exitDx=0;exitDy=0;fontSize=16;startSize=8;endSize=8;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="1.25" y="236" as="sourcePoint" />
            <mxPoint x="1.25" y="236" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-98" value="会員一覧" style="rounded=0;whiteSpace=wrap;html=1;fontStyle=1;fontSize=16;fontFamily=Verdana;" vertex="1" parent="1">
          <mxGeometry x="143" y="187" width="119" height="49" as="geometry" />
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-99" value="" style="endArrow=none;html=1;rounded=0;fontSize=16;startSize=8;endSize=8;curved=1;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="308" y="461" as="sourcePoint" />
            <mxPoint x="308" y="276" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-100" style="edgeStyle=none;curved=1;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;fontSize=16;startSize=8;endSize=8;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="372.26668294270826" y="211.33333333333337" as="targetPoint" />
            <mxPoint x="262" y="211.5" as="sourcePoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-101" style="edgeStyle=none;curved=1;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.75;exitY=1;exitDx=0;exitDy=0;fontSize=16;startSize=8;endSize=8;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="217" y="175" as="sourcePoint" />
            <mxPoint x="217" y="175" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-102" value="会員詳細" style="rounded=0;whiteSpace=wrap;html=1;fontStyle=1;fontSize=16;fontFamily=Verdana;" vertex="1" parent="1">
          <mxGeometry x="371.25" y="187" width="119" height="49" as="geometry" />
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-103" style="edgeStyle=none;curved=1;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.75;exitY=1;exitDx=0;exitDy=0;fontSize=16;startSize=8;endSize=8;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="237" y="250" as="sourcePoint" />
            <mxPoint x="237" y="250" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-105" style="edgeStyle=none;curved=1;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.75;exitY=1;exitDx=0;exitDy=0;fontSize=16;startSize=8;endSize=8;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="227" y="185" as="sourcePoint" />
            <mxPoint x="227" y="185" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-106" value="施設一覧" style="rounded=0;whiteSpace=wrap;html=1;fontStyle=1;fontSize=16;fontFamily=Verdana;" vertex="1" parent="1">
          <mxGeometry x="142.75" y="250" width="119" height="49" as="geometry" />
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-107" value="" style="endArrow=none;html=1;rounded=0;fontSize=16;startSize=8;endSize=8;curved=1;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="86" y="1100" as="sourcePoint" />
            <mxPoint x="86" y="212" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-108" style="edgeStyle=none;curved=1;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;fontSize=16;startSize=8;endSize=8;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="142.75" y="274" as="targetPoint" />
            <mxPoint x="85.75" y="274" as="sourcePoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-127" style="edgeStyle=none;curved=1;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;fontSize=16;startSize=8;endSize=8;fontStyle=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;fontFamily=Verdana;" edge="1" parent="1" target="uZVP7jplPoIl5v418rTI-128">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="354" y="529" as="targetPoint" />
            <mxPoint x="261.75" y="529.5" as="sourcePoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-128" value="カテゴリ登録" style="rounded=0;whiteSpace=wrap;html=1;fontStyle=1;fontSize=16;fontFamily=Verdana;" vertex="1" parent="1">
          <mxGeometry x="371" y="505" width="119" height="49" as="geometry" />
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-129" value="カテゴリ編集" style="rounded=0;whiteSpace=wrap;html=1;fontStyle=1;fontSize=16;fontFamily=Verdana;" vertex="1" parent="1">
          <mxGeometry x="371" y="568" width="119" height="49" as="geometry" />
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-130" value="カテゴリ削除" style="rounded=0;whiteSpace=wrap;html=1;fontStyle=1;fontSize=16;fontFamily=Verdana;" vertex="1" parent="1">
          <mxGeometry x="371" y="631" width="119" height="49" as="geometry" />
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-131" value="" style="endArrow=classic;html=1;rounded=0;fontSize=16;startSize=8;endSize=8;curved=1;entryX=0.017;entryY=0.5;entryDx=0;entryDy=0;entryPerimeter=0;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="307" y="591.8299999999999" as="sourcePoint" />
            <mxPoint x="371" y="591.8299999999999" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-132" value="" style="endArrow=classic;html=1;rounded=0;fontSize=16;startSize=8;endSize=8;curved=1;entryX=0.017;entryY=0.5;entryDx=0;entryDy=0;entryPerimeter=0;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="308" y="654.83" as="sourcePoint" />
            <mxPoint x="372" y="654.83" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-135" value="" style="endArrow=none;html=1;rounded=0;fontSize=16;startSize=8;endSize=8;curved=1;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="308" y="656" as="sourcePoint" />
            <mxPoint x="308" y="531" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-136" style="edgeStyle=none;curved=1;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.75;exitY=1;exitDx=0;exitDy=0;fontSize=16;startSize=8;endSize=8;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="237" y="505" as="sourcePoint" />
            <mxPoint x="237" y="505" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-137" value="カテゴリ一覧" style="rounded=0;whiteSpace=wrap;html=1;fontStyle=1;fontSize=16;fontFamily=Verdana;" vertex="1" parent="1">
          <mxGeometry x="142.75" y="505" width="119" height="49" as="geometry" />
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-138" style="edgeStyle=none;curved=1;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;fontSize=16;startSize=8;endSize=8;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="142.75" y="529" as="targetPoint" />
            <mxPoint x="85.75" y="529" as="sourcePoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-139" style="edgeStyle=none;curved=1;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;fontSize=16;startSize=8;endSize=8;fontStyle=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;fontFamily=Verdana;" edge="1" parent="1" target="uZVP7jplPoIl5v418rTI-140">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="354" y="722" as="targetPoint" />
            <mxPoint x="261.75" y="722.5" as="sourcePoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-140" value="お気に入り登録" style="rounded=0;whiteSpace=wrap;html=1;fontStyle=1;fontSize=16;fontFamily=Verdana;" vertex="1" parent="1">
          <mxGeometry x="371" y="698" width="119" height="49" as="geometry" />
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-141" value="お気に入り編集" style="rounded=0;whiteSpace=wrap;html=1;fontStyle=1;fontSize=16;fontFamily=Verdana;" vertex="1" parent="1">
          <mxGeometry x="371" y="761" width="119" height="49" as="geometry" />
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-142" value="お気に入り削除" style="rounded=0;whiteSpace=wrap;html=1;fontStyle=1;fontSize=16;fontFamily=Verdana;" vertex="1" parent="1">
          <mxGeometry x="371" y="824" width="119" height="49" as="geometry" />
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-143" value="" style="endArrow=classic;html=1;rounded=0;fontSize=16;startSize=8;endSize=8;curved=1;entryX=0.017;entryY=0.5;entryDx=0;entryDy=0;entryPerimeter=0;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="307" y="784.8299999999999" as="sourcePoint" />
            <mxPoint x="371" y="784.8299999999999" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-144" value="" style="endArrow=classic;html=1;rounded=0;fontSize=16;startSize=8;endSize=8;curved=1;entryX=0.017;entryY=0.5;entryDx=0;entryDy=0;entryPerimeter=0;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="308" y="847.83" as="sourcePoint" />
            <mxPoint x="372" y="847.83" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-145" value="" style="endArrow=none;html=1;rounded=0;fontSize=16;startSize=8;endSize=8;curved=1;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="308" y="849" as="sourcePoint" />
            <mxPoint x="308" y="724" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-146" style="edgeStyle=none;curved=1;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.75;exitY=1;exitDx=0;exitDy=0;fontSize=16;startSize=8;endSize=8;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="237" y="698" as="sourcePoint" />
            <mxPoint x="237" y="698" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-147" value="お気に入り一覧" style="rounded=0;whiteSpace=wrap;html=1;fontStyle=1;fontSize=16;fontFamily=Verdana;" vertex="1" parent="1">
          <mxGeometry x="142.75" y="698" width="119" height="49" as="geometry" />
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-148" style="edgeStyle=none;curved=1;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;fontSize=16;startSize=8;endSize=8;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="142.75" y="722" as="targetPoint" />
            <mxPoint x="85.75" y="722" as="sourcePoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-149" style="edgeStyle=none;curved=1;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;fontSize=16;startSize=8;endSize=8;fontStyle=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;fontFamily=Verdana;" edge="1" parent="1" target="uZVP7jplPoIl5v418rTI-150">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="355" y="913" as="targetPoint" />
            <mxPoint x="262.75" y="913.5" as="sourcePoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-150" value="レビュー登録" style="rounded=0;whiteSpace=wrap;html=1;fontStyle=1;fontSize=16;fontFamily=Verdana;" vertex="1" parent="1">
          <mxGeometry x="372" y="889" width="119" height="49" as="geometry" />
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-151" value="レビュー編集" style="rounded=0;whiteSpace=wrap;html=1;fontStyle=1;fontSize=16;fontFamily=Verdana;" vertex="1" parent="1">
          <mxGeometry x="372" y="952" width="119" height="49" as="geometry" />
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-152" value="レビュー削除" style="rounded=0;whiteSpace=wrap;html=1;fontStyle=1;fontSize=16;fontFamily=Verdana;" vertex="1" parent="1">
          <mxGeometry x="372" y="1015" width="119" height="49" as="geometry" />
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-153" value="" style="endArrow=classic;html=1;rounded=0;fontSize=16;startSize=8;endSize=8;curved=1;entryX=0.017;entryY=0.5;entryDx=0;entryDy=0;entryPerimeter=0;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="308" y="975.8299999999999" as="sourcePoint" />
            <mxPoint x="372" y="975.8299999999999" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-154" value="" style="endArrow=classic;html=1;rounded=0;fontSize=16;startSize=8;endSize=8;curved=1;entryX=0.017;entryY=0.5;entryDx=0;entryDy=0;entryPerimeter=0;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="309" y="1038.83" as="sourcePoint" />
            <mxPoint x="373" y="1038.83" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-155" value="" style="endArrow=none;html=1;rounded=0;fontSize=16;startSize=8;endSize=8;curved=1;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="309" y="1040" as="sourcePoint" />
            <mxPoint x="309" y="915" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-156" style="edgeStyle=none;curved=1;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.75;exitY=1;exitDx=0;exitDy=0;fontSize=16;startSize=8;endSize=8;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="238" y="889" as="sourcePoint" />
            <mxPoint x="238" y="889" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-157" value="レビュー一覧" style="rounded=0;whiteSpace=wrap;html=1;fontStyle=1;fontSize=16;fontFamily=Verdana;" vertex="1" parent="1">
          <mxGeometry x="143.75" y="889" width="119" height="49" as="geometry" />
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-158" style="edgeStyle=none;curved=1;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;fontSize=16;startSize=8;endSize=8;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="143.75" y="913" as="targetPoint" />
            <mxPoint x="86.75" y="913" as="sourcePoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="uZVP7jplPoIl5v418rTI-161" style="edgeStyle=none;curved=1;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;fontSize=16;startSize=8;endSize=8;fontStyle=1;fontFamily=Verdana;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="202.25" y="-158" as="sourcePoint" />
            <mxPoint x="202.25" y="-158" as="targetPoint" />
          </mxGeometry>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>




## 今後の改善点
- **マップ機能** :  Google Maps API を活用し、施設の位置情報をインタラクティブに表示する機能を追加。
- **評価ランキング機能** : Django ORM を用いてデータベースの評価を集計してランキングリストを生成。フロントエンドには JavaScript を用いてユーザー操作に応じてランキングをリアルタイムで更新する機能を実装。
