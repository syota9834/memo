# Django

PythonでWebアプリケーションを開発するためのWebフレームワーク。

Djangoは「バッテリー同梱（Batteries Included）」の思想を持っており、Webアプリケーション開発に必要な機能が一通り揃っている。

主な機能：

- URLルーティング
- View
- Template
- ORM
- データベース連携
- Form
- バリデーション
- 認証
- 管理画面
- セッション
- Middleware
- CSRF対策
- REST API

---

# 目次

- [1. Djangoとは](#1-djangoとは)
- [2. Djangoの特徴](#2-djangoの特徴)
- [3. Djangoの基本構成](#3-djangoの基本構成)
- [4. プロジェクトとアプリケーション](#4-プロジェクトとアプリケーション)
- [5. プロジェクト作成](#5-プロジェクト作成)
- [6. 開発サーバー起動](#6-開発サーバー起動)
- [7. プロジェクト構成](#7-プロジェクト構成)
- [8. manage.py](#8-managepy)
- [9. settings.py](#9-settingspy)
- [10. URLルーティング](#10-urlルーティング)
- [11. View](#11-view)
- [12. Template](#12-template)
- [13. Template構文](#13-template構文)
- [14. Static Files](#14-static-files)
- [15. Model](#15-model)
- [16. Django ORM](#16-django-orm)
- [17. QuerySet](#17-queryset)
- [18. データ取得](#18-データ取得)
- [19. データ登録](#19-データ登録)
- [20. データ更新](#20-データ更新)
- [21. データ削除](#21-データ削除)
- [22. Migration](#22-migration)
- [23. Modelのリレーション](#23-modelのリレーション)
- [24. Form](#24-form)
- [25. ModelForm](#25-modelform)
- [26. CRUDアプリケーション](#26-crudアプリケーション)
- [27. Class Based View](#27-class-based-view)
- [28. Function Based View](#28-function-based-view)
- [29. Django Admin](#29-django-admin)
- [30. ユーザー認証](#30-ユーザー認証)
- [31. Middleware](#31-middleware)
- [32. セッション](#32-セッション)
- [33. CSRF](#33-csrf)
- [34. JSONレスポンス](#34-jsonレスポンス)
- [35. Django REST Framework](#35-django-rest-framework)
- [36. API作成例](#36-api作成例)
- [37. 非同期処理](#37-非同期処理)
- [38. 環境変数](#38-環境変数)
- [39. DjangoとFastAPIの違い](#39-djangoとfastapiの違い)

---

# 1. Djangoとは

DjangoはPythonでWebアプリケーションを開発するためのWebフレームワーク。

基本的には以下のような構成でWebアプリケーションを構築する。

```text
ユーザー
   ↓
URL
   ↓
View
   ↓
Model / Service
   ↓
Database
   ↓
View
   ↓
Template
   ↓
HTML
   ↓
ユーザー
```

APIとして利用する場合：

```text
Client
   ↓
HTTP Request
   ↓
URL
   ↓
View
   ↓
Service / Model
   ↓
Database
   ↓
JSON Response
   ↓
Client
```

---

# 2. Djangoの特徴

DjangoにはWebアプリケーション開発に必要な機能が多く用意されている。

代表的な機能：

- URL Routing
- View
- Template Engine
- ORM
- Form
- Authentication
- Admin
- Middleware
- Session
- CSRF Protection

特にORMとAdmin画面はDjangoの大きな特徴。

---

# 3. Djangoの基本構成

Djangoでは、プロジェクトとアプリケーションという単位で構成する。

```text
Django Project
│
├── Project
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── Application
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── forms.py
    └── admin.py
```

基本的な役割：

```text
URL
 ↓
View
 ↓
Model
 ↓
Database

View
 ↓
Template
 ↓
HTML
```

---

# 4. プロジェクトとアプリケーション

## Project

Webアプリケーション全体の設定を管理する。

主なファイル：

```text
settings.py
urls.py
asgi.py
wsgi.py
```

---

## Application

機能単位で作成する。

例えばECサイトなら：

```text
project/
├── users/
├── products/
├── orders/
└── payments/
```

のように分割できる。

---

# 5. プロジェクト作成

Djangoをインストール：

```bash
pip install django
```

プロジェクト作成：

```bash
django-admin startproject config .
```

アプリケーション作成：

```bash
python manage.py startapp users
```

---

# 6. 開発サーバー起動

```bash
python manage.py runserver
```

デフォルトでは、

```text
http://127.0.0.1:8000/
```

でアクセスできる。

---

# 7. プロジェクト構成

一般的な構成例：

```text
project/
│
├── manage.py
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── users/
    ├── migrations/
    ├── templates/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    └── views.py
```

---

# 8. manage.py

Djangoプロジェクトを操作するためのCLI。

代表的なコマンド：

```bash
python manage.py runserver
```

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

```bash
python manage.py createsuperuser
```

```bash
python manage.py shell
```

---

# 9. settings.py

Djangoアプリケーション全体の設定を管理する。

主な設定：

```python
INSTALLED_APPS = [
    ...
]
```

```python
MIDDLEWARE = [
    ...
]
```

```python
DATABASES = {
    ...
}
```

```python
TEMPLATES = [
    ...
]
```

```python
STATIC_URL = "static/"
```

---

# 10. URLルーティング

URLとViewを紐付ける。

## urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.hello),
]
```

---

## View

```python
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello Django")
```

ブラウザ：

```text
/hello/
```

にアクセスすると、

```text
Hello Django
```

と表示される。

---

# 11. View

ViewはHTTPリクエストを受け取り、レスポンスを返す。

```python
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello")
```

基本的な流れ：

```text
HTTP Request
    ↓
URL Resolver
    ↓
View
    ↓
HTTP Response
```

---

# 12. Template

HTMLをTemplateとして分離できる。

ディレクトリ：

```text
templates/
└── hello.html
```

`hello.html`：

```html
<!DOCTYPE html>
<html>
<head>
    <title>Hello</title>
</head>

<body>

<h1>Hello Django</h1>

</body>
</html>
```

View：

```python
from django.shortcuts import render

def hello(request):
    return render(
        request,
        "hello.html"
    )
```

---

# 13. Template構文

Django Templateでは、変数を表示できる。

```html
<h1>{{ name }}</h1>
```

View：

```python
def hello(request):

    context = {
        "name": "Taro"
    }

    return render(
        request,
        "hello.html",
        context
    )
```

---

## if

```html
{% if user.is_authenticated %}

<p>ログインしています</p>

{% else %}

<p>ログインしていません</p>

{% endif %}
```

---

## for

```html
<ul>

{% for user in users %}

<li>
    {{ user.name }}
</li>

{% endfor %}

</ul>
```

---

# 14. Static Files

CSSやJavaScript、画像などの静的ファイルを管理する。

```text
static/
├── css/
│   └── style.css
│
├── js/
│   └── app.js
│
└── images/
    └── logo.png
```

Template：

```html
{% load static %}

<link
    rel="stylesheet"
    href="{% static 'css/style.css' %}"
>
```

---

# 15. Model

Modelはデータベースのテーブル構造をPythonクラスとして定義する。

```python
from django.db import models

class User(models.Model):

    name = models.CharField(
        max_length=100
    )

    email = models.EmailField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )
```

イメージ：

```text
Python Class
     ↓
Django ORM
     ↓
Database Table
```

---

# 16. Django ORM

Django ORMを使用すると、SQLを直接記述せずにデータベースを操作できる。

例えば：

```python
User.objects.all()
```

はSQLに変換されて実行される。

```sql
SELECT *
FROM user;
```

---

# 17. QuerySet

Django ORMではQuerySetを使用してデータを操作する。

```python
users = User.objects.all()
```

条件指定：

```python
users = User.objects.filter(
    name="Taro"
)
```

---

# 18. データ取得

全件取得：

```python
User.objects.all()
```

条件指定：

```python
User.objects.filter(
    name="Taro"
)
```

1件取得：

```python
User.objects.get(
    id=1
)
```

存在確認：

```python
User.objects.filter(
    id=1
).exists()
```

---

# 19. データ登録

```python
User.objects.create(
    name="Taro",
    email="taro@example.com"
)
```

または：

```python
user = User(
    name="Taro",
    email="taro@example.com"
)

user.save()
```

---

# 20. データ更新

```python
user = User.objects.get(
    id=1
)

user.name = "Jiro"

user.save()
```

QuerySetで更新：

```python
User.objects.filter(
    id=1
).update(
    name="Jiro"
)
```

---

# 21. データ削除

```python
user = User.objects.get(
    id=1
)

user.delete()
```

複数削除：

```python
User.objects.filter(
    name="Taro"
).delete()
```

---

# 22. Migration

Modelの変更をデータベースに反映する。

Modelを変更：

```python
class User(models.Model):

    name = models.CharField(
        max_length=100
    )

    age = models.IntegerField()
```

Migrationファイル作成：

```bash
python manage.py makemigrations
```

DBに反映：

```bash
python manage.py migrate
```

基本的な流れ：

```text
models.py変更
    ↓
makemigrations
    ↓
Migrationファイル作成
    ↓
migrate
    ↓
Database更新
```

---

# 23. Modelのリレーション

DjangoではModel同士のリレーションを定義できる。

## ForeignKey

1対多の関係。

```python
class Post(models.Model):

    title = models.CharField(
        max_length=100
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
```

```text
User
 │
 ├── Post
 ├── Post
 └── Post
```

---

## OneToOneField

1対1の関係。

```python
profile = models.OneToOneField(
    User,
    on_delete=models.CASCADE
)
```

---

## ManyToManyField

多対多の関係。

```python
tags = models.ManyToManyField(
    Tag
)
```

---

# 24. Form

フォーム入力を扱うための機能。

```python
from django import forms

class UserForm(forms.Form):

    name = forms.CharField(
        max_length=100
    )

    email = forms.EmailField()
```

---

# 25. ModelForm

Modelを元にフォームを作成できる。

```python
from django import forms

class UserForm(
    forms.ModelForm
):

    class Meta:

        model = User

        fields = [
            "name",
            "email"
        ]
```

ModelFormを使用すると、

```text
Model
  ↓
ModelForm
  ↓
HTML Form
```

という形でフォームを構築できる。

---

# 26. CRUDアプリケーション

CRUD：

```text
Create
Read
Update
Delete
```

Djangoでは以下のように実装する。

```text
Create
    ↓
Model.objects.create()

Read
    ↓
Model.objects.get()
Model.objects.filter()

Update
    ↓
object.save()
QuerySet.update()

Delete
    ↓
object.delete()
```

---

# 27. Class Based View

Viewをクラスとして定義する。

```python
from django.views import View
from django.http import HttpResponse

class HelloView(View):

    def get(self, request):

        return HttpResponse(
            "Hello"
        )
```

URL：

```python
from django.urls import path

urlpatterns = [

    path(
        "hello/",
        HelloView.as_view()
    )

]
```

---

# 28. Function Based View

関数でViewを定義する。

```python
def hello(request):

    return HttpResponse(
        "Hello"
    )
```

シンプルな処理ではFunction Based Viewが分かりやすい。

---

# 29. Django Admin

Djangoには管理画面が標準で用意されている。

管理ユーザー作成：

```bash
python manage.py createsuperuser
```

Model登録：

```python
from django.contrib import admin

from .models import User

admin.site.register(User)
```

管理画面：

```text
/admin/
```

からデータを操作できる。

---

# 30. ユーザー認証

Djangoには認証機能が用意されている。

主な機能：

- ログイン
- ログアウト
- ユーザー作成
- パスワード管理
- セッション

ログイン状態確認：

```python
if request.user.is_authenticated:

    print("ログイン済み")
```

---

# 31. Middleware

MiddlewareはHTTP Request / Responseの処理に割り込む仕組み。

```text
Request
   ↓
Middleware
   ↓
View
   ↓
Middleware
   ↓
Response
```

代表的な用途：

- 認証
- ロギング
- セキュリティ
- セッション
- リクエスト加工

---

# 32. セッション

ユーザーごとの情報をサーバー側で保持できる。

保存：

```python
request.session[
    "username"
] = "Taro"
```

取得：

```python
username = request.session.get(
    "username"
)
```

---

# 33. CSRF

CSRF（Cross-Site Request Forgery）対策機能がDjangoには組み込まれている。

FormでPOSTする場合：

```html
<form method="post">

    {% csrf_token %}

    <button type="submit">
        送信
    </button>

</form>
```

DjangoではPOSTフォームにCSRFトークンを含める。

---

# 34. JSONレスポンス

APIなどでJSONを返す場合は`JsonResponse`を使用できる。

```python
from django.http import JsonResponse

def api(request):

    return JsonResponse({
        "message": "Hello"
    })
```

レスポンス：

```json
{
    "message": "Hello"
}
```

---

# 35. Django REST Framework

Django REST Framework（DRF）は、DjangoでREST APIを構築するためのライブラリ。

主な機能：

- Serializer
- APIView
- ViewSet
- Router
- Authentication
- Permission

基本的な構成：

```text
Client
    ↓
URL
    ↓
View
    ↓
Serializer
    ↓
Model
    ↓
Database
```

---

# 36. API作成例

Serializer：

```python
from rest_framework import serializers

class UserSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = User

        fields = [
            "id",
            "name",
            "email"
        ]
```

ViewSet：

```python
from rest_framework.viewsets import ModelViewSet

class UserViewSet(
    ModelViewSet
):

    queryset = User.objects.all()

    serializer_class = UserSerializer
```

Router：

```python
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(
    "users",
    UserViewSet
)
```

これによりCRUD APIを構築できる。

---

# 37. 非同期処理

Djangoでは非同期Viewを定義できる。

```python
async def hello(request):

    return JsonResponse({
        "message": "Hello"
    })
```

非同期処理が必要な場合は`async` / `await`を使用する。

---

# 38. 環境変数

環境ごとに異なる設定値は環境変数で管理する。

例：

```text
SECRET_KEY
DATABASE_URL
DEBUG
```

Python：

```python
import os

SECRET_KEY = os.environ.get(
    "SECRET_KEY"
)
```

本番環境では、

- SECRET_KEY
- DBパスワード
- APIキー

などの機密情報をGitにコミットしない。

---

# 39. DjangoとFastAPIの違い

## Django

```text
Django
├── ORM
├── Admin
├── Authentication
├── Template
├── Form
└── Middleware
```

Webアプリケーションを作るための機能が一通り揃っている。

---

## FastAPI

```text
FastAPI
├── API
├── Pydantic
├── Dependency Injection
└── OpenAPI
```

API開発に特化している。

---

## 比較

| 項目 | Django | FastAPI |
|---|---|---|
| Webアプリ | ◎ | ○ |
| REST API | ○ | ◎ |
| ORM | 標準搭載 | 外部ライブラリ |
| Admin | 標準搭載 | なし |
| Template | 標準搭載 | なし |
| Form | 標準搭載 | API中心 |
| 認証 | 標準機能あり | 自分で構築 |
| 非同期 | 対応 | 得意 |
| APIドキュメント | DRF等 | OpenAPI自動生成 |

---

# Djangoでよく使うコマンド

プロジェクト作成：

```bash
django-admin startproject config .
```

アプリ作成：

```bash
python manage.py startapp app_name
```

サーバー起動：

```bash
python manage.py runserver
```

Migration作成：

```bash
python manage.py makemigrations
```

Migration適用：

```bash
python manage.py migrate
```

スーパーユーザー作成：

```bash
python manage.py createsuperuser
```

Django Shell：

```bash
python manage.py shell
```

---

# Djangoの基本的な処理フロー

HTMLを返す場合：

```text
Browser
    ↓
HTTP Request
    ↓
urls.py
    ↓
views.py
    ↓
models.py
    ↓
Database
    ↓
views.py
    ↓
Template
    ↓
HTML Response
    ↓
Browser
```

APIの場合：

```text
Client
    ↓
HTTP Request
    ↓
urls.py
    ↓
View
    ↓
Serializer
    ↓
Model
    ↓
Database
    ↓
Serializer
    ↓
JSON Response
    ↓
Client
```

---

# Djangoでよく使うファイル

| ファイル | 役割 |
|---|---|
| `settings.py` | プロジェクト設定 |
| `urls.py` | URLルーティング |
| `views.py` | リクエスト処理 |
| `models.py` | DBモデル |
| `forms.py` | フォーム |
| `admin.py` | Admin設定 |
| `apps.py` | App設定 |
| `tests.py` | テスト |
| `manage.py` | CLI |
| `migrations/` | DB変更履歴 |

---

# Djangoの基本的な開発フロー

```text
1. Project作成
        ↓
2. App作成
        ↓
3. settings.pyにApp追加
        ↓
4. Model作成
        ↓
5. makemigrations
        ↓
6. migrate
        ↓
7. URL設定
        ↓
8. View作成
        ↓
9. Template作成
        ↓
10. Service / ORM実装
        ↓
11. テスト
        ↓
12. runserver
        ↓
13. 動作確認
```

---

# 関連技術

- Python
- Django REST Framework
- PostgreSQL
- MySQL
- SQLite
- Redis
- Celery
- Gunicorn
- Nginx
- Docker
