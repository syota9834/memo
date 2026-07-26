# FastAPI

## 目次
- [1. 概要](#1-概要)
- [2. インストール](#2-インストール)
- [3. 基本構造](#3-基本構造)
- [4. アプリケーションの起動](#4-アプリケーションの起動)
- [5. GETリクエスト](#5-getリクエスト)
- [6. POSTリクエスト](#6-postリクエスト)
- [7. パスパラメータ](#7-パスパラメータ)
- [8. クエリパラメータ](#8-クエリパラメータ)
- [9. Pydanticモデル](#9-pydanticモデル)
- [10. レスポンス](#10-レスポンス)
- [11. Response Model](#11-response-model)
- [12. APIドキュメント](#12-apiドキュメント)
- [13. HTTPステータスコード](#13-httpステータスコード)
- [14. HTTPException](#14-httpexception)
- [15. HTMLファイルを返す](#15-htmlファイルを返す)
- [16. index.htmlを使用したWebページ](#16-indexhtmlを使用したwebページ)
- [17. Jinja2Templatesを使用したHTMLページ](#17-jinja2templatesを使用したhtmlページ)
- [18. HTMLからAPIを呼び出す](#18-htmlからapiを呼び出す)
- [19. 実用的なAPIサンプル](#19-実用的なapiサンプル)
- [20. よく使うデコレータ](#20-よく使うデコレータ)
- [21. よく使うクラス・機能](#21-よく使うクラス機能)
- [22. よく使うコマンド](#22-よく使うコマンド)
- [23. APIドキュメント](#23-apiドキュメント)

## 1. 概要

FastAPIは、PythonでWeb APIを構築するためのWebフレームワーク。

主な特徴：

- PythonでAPIを簡単に構築できる
- 型ヒントを活用したデータバリデーション
- 自動的なAPIドキュメント生成
- 非同期処理（`async` / `await`）に対応
- 高速なWeb API開発が可能
- OpenAPIに対応
- Pydanticを利用したデータ検証が可能

APIだけでなく、HTMLファイルを返す簡単なWebアプリケーションも作成できる。

---

## 2. インストール

`pip`を使用してインストールする。

```bash
pip install fastapi
```

FastAPIアプリケーションを起動するために、ASGIサーバーの`uvicorn`も使用する。

```bash
pip install uvicorn
```

まとめてインストールする場合：

```bash
pip install fastapi uvicorn
```

---

## 3. 基本構造

FastAPIでは、`FastAPI`クラスのインスタンスを作成してWebアプリケーションを構築する。

```python
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {
        "message": "Hello World"
    }
```

---

## 4. アプリケーションの起動

`uvicorn`を使用してFastAPIアプリケーションを起動する。

ファイル名が`main.py`の場合：

```bash
uvicorn main:app
```

`--reload`を指定すると、ソースコードの変更を検知して自動的にサーバーを再起動する。

開発環境では以下のように起動できる。

```bash
uvicorn main:app --reload
```

起動後、ブラウザから以下にアクセスする。

```text
http://127.0.0.1:8000
```

---

## 5. GETリクエスト

`@app.get()`を使用してGETリクエストを処理する。

```python
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {
        "message": "Hello World"
    }
```

ブラウザからアクセスすると、JSON形式でレスポンスが返る。

```json
{
    "message": "Hello World"
}
```

---

## 6. POSTリクエスト

`@app.post()`を使用してPOSTリクエストを処理する。

```python
from fastapi import FastAPI


app = FastAPI()


@app.post("/items")
def create_item():
    return {
        "message": "Item created"
    }
```

GETとPOSTでは使用するデコレータが異なる。

```python
@app.get("/")
def get_data():
    ...


@app.post("/")
def create_data():
    ...
```

---

## 7. パスパラメータ

URLの一部をパラメータとして受け取ることができる。

```python
from fastapi import FastAPI


app = FastAPI()


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {
        "item_id": item_id
    }
```

以下のURLにアクセスした場合：

```text
/items/10
```

レスポンス：

```json
{
    "item_id": 10
}
```

型ヒントで`int`を指定しているため、`item_id`は整数として扱われる。

---

## 8. クエリパラメータ

URLのクエリパラメータを受け取ることができる。

```python
from fastapi import FastAPI


app = FastAPI()


@app.get("/items")
def read_items(
    skip: int = 0,
    limit: int = 10,
):
    return {
        "skip": skip,
        "limit": limit,
    }
```

以下のURLにアクセスする。

```text
/items?skip=10&limit=20
```

レスポンス：

```json
{
    "skip": 10,
    "limit": 20
}
```

---

## 9. Pydanticモデル

リクエストボディを受け取る場合、Pydanticモデルを使用できる。

```python
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    description: str | None = None


@app.post("/items")
def create_item(item: Item):
    return item
```

以下のJSONを送信する。

```json
{
    "name": "Book",
    "price": 1500,
    "description": "Python book"
}
```

FastAPIがPydanticモデルに基づいてデータを検証する。

---

## 10. レスポンス

FastAPIでは、Pythonの辞書を返すとJSONレスポンスとして返すことができる。

```python
@app.get("/")
def read_root():
    return {
        "message": "Hello World"
    }
```

リストも返すことができる。

```python
@app.get("/items")
def read_items():
    return [
        {
            "id": 1,
            "name": "Item 1",
        },
        {
            "id": 2,
            "name": "Item 2",
        },
    ]
```

---

## 11. Response Model

レスポンスの形式をPydanticモデルで定義できる。

```python
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    id: int
    name: str


@app.get(
    "/items",
    response_model=Item,
)
def read_item():
    return {
        "id": 1,
        "name": "Book",
    }
```

`response_model`を指定することで、レスポンスのデータ形式を明確にできる。

---

## 12. APIドキュメント

FastAPIでは、APIドキュメントが自動生成される。

### Swagger UI

以下にアクセスする。

```text
http://127.0.0.1:8000/docs
```

Swagger UIを使用してAPIをブラウザ上から確認・実行できる。

### ReDoc

以下にアクセスする。

```text
http://127.0.0.1:8000/redoc
```

ReDoc形式のAPIドキュメントを確認できる。

---

## 13. HTTPステータスコード

APIのレスポンスにHTTPステータスコードを指定できる。

```python
from fastapi import FastAPI
from fastapi import status


app = FastAPI()


@app.post(
    "/items",
    status_code=status.HTTP_201_CREATED,
)
def create_item():
    return {
        "message": "Created"
    }
```

代表的なステータスコード：

| ステータスコード | 意味 |
|---|---|
| `200` | OK |
| `201` | Created |
| `204` | No Content |
| `400` | Bad Request |
| `401` | Unauthorized |
| `403` | Forbidden |
| `404` | Not Found |
| `500` | Internal Server Error |

---

## 14. HTTPException

APIでエラーを返す場合、`HTTPException`を使用できる。

```python
from fastapi import FastAPI
from fastapi import HTTPException


app = FastAPI()


@app.get("/items/{item_id}")
def read_item(item_id: int):

    if item_id == 0:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
        )

    return {
        "item_id": item_id
    }
```

---

## 15. HTMLファイルを返す

FastAPIでは、HTMLファイルを返してWebページを作成することもできる。

`HTMLResponse`を使用する。

```python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get(
    "/",
    response_class=HTMLResponse,
)
def read_root():

    return """
    <html>
        <body>
            <h1>Hello World</h1>
        </body>
    </html>
    """
```

ブラウザで以下にアクセスする。

```text
http://127.0.0.1:8000
```

HTMLページが表示される。

---

## 16. index.htmlを使用したWebページ

HTMLファイルを別ファイルとして管理することもできる。

### ディレクトリ構成

```text
project/
├── main.py
└── templates/
    └── index.html
```

### index.html

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>FastAPI App</title>
</head>

<body>

    <h1>Hello FastAPI!</h1>

    <p>
        FastAPIで作成したWebページです。
    </p>

</body>
</html>
```

### main.py

```python
from fastapi import FastAPI
from fastapi.responses import FileResponse


app = FastAPI()


@app.get("/")
def read_root():

    return FileResponse(
        "templates/index.html"
    )
```

サーバーを起動する。

```bash
uvicorn main:app --reload
```

ブラウザからアクセスする。

```text
http://127.0.0.1:8000
```

`index.html`がブラウザに表示される。

---

## 17. Jinja2Templatesを使用したHTMLページ

動的にHTMLを生成する場合は、Jinja2を使用できる。

インストール：

```bash
pip install jinja2
```

### ディレクトリ構成

```text
project/
├── main.py
└── templates/
    └── index.html
```

### index.html

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>FastAPI App</title>
</head>

<body>

    <h1>{{ title }}</h1>

    <p>{{ message }}</p>

</body>
</html>
```

### main.py

```python
from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates


app = FastAPI()

templates = Jinja2Templates(
    directory="templates"
)


@app.get("/")
def read_root(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "title": "FastAPI App",
            "message": "Hello FastAPI!",
        },
    )
```

`{{ title }}`や`{{ message }}`の部分に、Pythonから渡した値が埋め込まれる。

---

## 18. HTMLからAPIを呼び出す

FastAPIでは、HTMLページとAPIを組み合わせることができる。

### ディレクトリ構成

```text
project/
├── main.py
└── templates/
    └── index.html
```

### main.py

```python
from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates


app = FastAPI()

templates = Jinja2Templates(
    directory="templates"
)


@app.get("/")
def index(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
    )


@app.get("/api/message")
def get_message():

    return {
        "message": "Hello from API!"
    }
```

### index.html

```html
<!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="UTF-8">
    <title>FastAPI App</title>
</head>

<body>

    <h1>FastAPI</h1>

    <button onclick="getMessage()">
        APIを呼び出す
    </button>

    <p id="result"></p>

    <script>

        async function getMessage() {

            const response = await fetch(
                "/api/message"
            );

            const data = await response.json();

            document.getElementById(
                "result"
            ).textContent = data.message;
        }

    </script>

</body>

</html>
```

処理の流れ：

```text
ブラウザ
    ↓
index.htmlを表示
    ↓
ボタンをクリック
    ↓
JavaScriptのfetch()
    ↓
GET /api/message
    ↓
FastAPI
    ↓
JSONを返す
    ↓
JavaScriptで結果を表示
```

---

## 19. 実用的なAPIサンプル

簡単なCRUD APIを作成する。

### データモデル

```python
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float
```

### API

```python
from fastapi import FastAPI


app = FastAPI()


items = []


@app.get("/items")
def get_items():

    return items


@app.post("/items")
def create_item(item: Item):

    items.append(item)

    return item
```

### GET

```text
GET /items
```

すべてのItemを取得する。

### POST

```text
POST /items
```

Itemを新規作成する。

JSON：

```json
{
    "name": "Book",
    "price": 1500
}
```

---

## 20. よく使うデコレータ

| デコレータ | 用途 |
|---|---|
| `@app.get()` | GETリクエスト |
| `@app.post()` | POSTリクエスト |
| `@app.put()` | PUTリクエスト |
| `@app.patch()` | PATCHリクエスト |
| `@app.delete()` | DELETEリクエスト |

---

## 21. よく使うクラス・機能

| クラス・機能 | 用途 |
|---|---|
| `FastAPI` | FastAPIアプリケーション |
| `BaseModel` | Pydanticモデル |
| `HTTPException` | HTTPエラー |
| `FileResponse` | ファイルをレスポンスとして返す |
| `HTMLResponse` | HTMLをレスポンスとして返す |
| `Jinja2Templates` | Jinja2テンプレートを使用 |
| `TemplateResponse` | HTMLテンプレートをレスポンスとして返す |

---

## 22. よく使うコマンド

### インストール

```bash
pip install fastapi uvicorn
```

### Jinja2を使用する場合

```bash
pip install jinja2
```

### 開発サーバー起動

```bash
uvicorn main:app --reload
```

### ポートを指定

```bash
uvicorn main:app --reload --port 8080
```

### ホストを指定

```bash
uvicorn main:app --reload --host 0.0.0.0
```

---

## 23. APIドキュメント

FastAPIでは、APIドキュメントが自動生成される。

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

---