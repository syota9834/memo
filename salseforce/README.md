# salseforce

## 1. 環境の作成方法
### developer editionの使用
salseforce developer edition（無料）が使える

https://www.salesforce.com/products/free-trial/developer/

必要事項記入後、サインアップすると環境が作成される。

使用していないと`40日程度`で自動削除されるので注意。

使用可能な基本的な機能：
- 開発者コンソール
- apex, トリガー等の作成
- 外部API通信

---

## 2. 外部APIとの接続方法
1. 設定画面 > 外部アプリケーションへ遷移
2. 外部アプリケーションを構築する(OAuthフロー:client_credential)
3. 作成後、コンシューマー鍵と秘密鍵を取得
4. 取得したキーを外部APIの接続キーへ設定すれば疎通可能

---
