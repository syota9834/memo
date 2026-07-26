# ASP.NET Core + Blazor Web App

.NET 8を使用したASP.NET Core Blazor Web Appの技術メモ。

---

# 目次

- [1. Blazorとは](#1-blazorとは)
- [2. Blazor Web App](#2-blazor-web-app)
- [3. プロジェクト作成](#3-プロジェクト作成)
- [4. プロジェクト構成](#4-プロジェクト構成)
- [5. Program.cs](#5-programcs)
- [6. Components](#6-components)
- [7. Razorコンポーネント](#7-razorコンポーネント)
- [8. .razorファイル](#8-razorファイル)
- [9. .razor.csファイル](#9-razorcsファイル)
- [10. @pageとルーティング](#10-pageとルーティング)
- [11. @code](#11-code)
- [12. イベント処理](#12-イベント処理)
- [13. データバインディング](#13-データバインディング)
- [14. @bind](#14-bind)
- [15. コンポーネント間のデータ受け渡し](#15-コンポーネント間のデータ受け渡し)
- [16. Parameter](#16-parameter)
- [17. EventCallback](#17-eventcallback)
- [18. Layout](#18-layout)
- [19. wwwroot](#19-wwwroot)
- [20. CSS](#20-css)
- [21. JavaScriptとの連携](#21-javascriptとの連携)
- [22. Dependency Injection](#22-dependency-injection)
- [23. Service](#23-service)
- [24. API通信](#24-api通信)
- [25. appsettings.json](#25-appsettingsjson)
- [26. 非同期処理](#26-非同期処理)
- [27. フォーム](#27-フォーム)
- [28. バリデーション](#28-バリデーション)
- [29. レンダリングモード](#29-レンダリングモード)
- [30. Interactive Server](#30-interactive-server)
- [31. Interactive WebAssembly](#31-interactive-webassembly)
- [32. Interactive Auto](#32-interactive-auto)
- [33. コンポーネントのライフサイクル](#33-コンポーネントのライフサイクル)
- [34. 実務での基本的な構成例](#34-実務での基本的な構成例)
- [35. 簡単なフロントエンド作成例](#35-簡単なフロントエンド作成例)
- [36. 実務メモ](#36-実務メモ)

---

# 1. Blazorとは

Blazorは、C#と.NETを使用してWeb UIを構築するためのフレームワーク。

ASP.NET Core上で動作し、Razor構文を使用してUIコンポーネントを作成する。

主な特徴：

- C#でWeb UIを開発できる
- Razor構文を使用する
- コンポーネントベースでUIを構築できる
- HTML / CSSと組み合わせて使用できる
- JavaScriptとの連携も可能
- ASP.NET CoreのDIを利用できる
- APIやデータベースと連携できる

基本的なイメージ：

```text
ASP.NET Core
    │
    └── Blazor
          │
          ├── Razor Component
          │      ├── HTML
          │      ├── Razor
          │      └── C#
          │
          ├── Dependency Injection
          │
          ├── Service
          │
          └── API / Database
```

---

# 2. Blazor Web App

.NET 8では、BlazorのWebアプリケーションを構築する方法としてBlazor Web Appが提供されている。

Blazor Web Appでは、アプリケーションの用途に応じてレンダリング方式を選択できる。

代表的なレンダリングモード：

- Static SSR
- Interactive Server
- Interactive WebAssembly
- Interactive Auto

---

# 3. プロジェクト作成

.NET SDKのバージョン確認：

```bash
dotnet --version
```

Blazor Web Appを作成：

```bash
dotnet new blazor -n MyBlazorApp
```

プロジェクトディレクトリへ移動：

```bash
cd MyBlazorApp
```

アプリケーション起動：

```bash
dotnet run
```

ブラウザから表示：

```text
https://localhost:xxxx
```

---

# 4. プロジェクト構成

.NET 8のBlazor Web Appでは、基本的に以下のような構成になる。

```text
MyBlazorApp/
│
├── Components/
│   ├── Layout/
│   │   ├── MainLayout.razor
│   │   └── NavMenu.razor
│   │
│   ├── Pages/
│   │   ├── Home.razor
│   │   ├── Counter.razor
│   │   └── Weather.razor
│   │
│   ├── App.razor
│   └── Routes.razor
│
├── wwwroot/
│   ├── css/
│   ├── js/
│   └── images/
│
├── appsettings.json
├── appsettings.Development.json
├── Program.cs
└── MyBlazorApp.csproj
```

主な役割：

| ファイル / フォルダ | 役割 |
|---|---|
| `Components/` | Razorコンポーネント |
| `Components/Pages/` | ページとして使用するコンポーネント |
| `Components/Layout/` | レイアウト関連 |
| `App.razor` | アプリケーションのルート |
| `Routes.razor` | ルーティング |
| `wwwroot/` | CSS、JavaScript、画像など |
| `Program.cs` | アプリケーション設定 |
| `appsettings.json` | 設定値 |
| `.csproj` | プロジェクト設定 |

---

# 5. Program.cs

ASP.NET Coreアプリケーションの起動設定を行う。

基本的な構成：

```csharp
var builder = WebApplication.CreateBuilder(args);

builder.Services
    .AddRazorComponents()
    .AddInteractiveServerComponents();

var app = builder.Build();

app.UseHttpsRedirection();

app.UseStaticFiles();

app.UseAntiforgery();

app.MapRazorComponents<App>()
    .AddInteractiveServerRenderMode();

app.Run();
```

大まかな流れ：

```text
WebApplicationBuilder
        ↓
サービス登録
        ↓
WebApplication作成
        ↓
Middleware設定
        ↓
Razor Components設定
        ↓
アプリケーション起動
```

---

# 6. Components

Blazorでは、UIをコンポーネント単位で構築する。

例えば：

```text
Components/
├── Pages/
│   ├── Home.razor
│   └── Counter.razor
│
├── Layout/
│   ├── MainLayout.razor
│   └── NavMenu.razor
│
└── Shared/
    └── MyButton.razor
```

コンポーネントは、他のコンポーネントから呼び出すことができる。

---

# 7. Razorコンポーネント

`.razor`ファイルはRazorコンポーネントとして扱われる。

例：

```razor
<h1>Hello World</h1>

<p>Blazor Component</p>
```

HTMLのように記述できる。

また、C#コードを組み合わせることができる。

```razor
<h1>@message</h1>

@code {
    private string message = "Hello Blazor";
}
```

---

# 8. .razorファイル

`.razor`ファイルには、UIとRazor構文を記述する。

```razor
<h1>@title</h1>

<button @onclick="ClickButton">
    クリック
</button>

@code {
    private string title = "Hello";

    private void ClickButton()
    {
        title = "Clicked!";
    }
}
```

---

# 9. .razor.csファイル

RazorコンポーネントのC#コードを分離できる。

例えば：

```text
Counter.razor
Counter.razor.cs
```

## Counter.razor

```razor
<h1>Counter</h1>

<p>Current count: @currentCount</p>

<button @onclick="IncrementCount">
    Click me
</button>
```

## Counter.razor.cs

```csharp
public partial class Counter
{
    private int currentCount = 0;

    private void IncrementCount()
    {
        currentCount++;
    }
}
```

このようにUIとロジックを分離できる。

```text
Counter.razor
    ↓
UI
    ↓
Counter.razor.cs
    ↓
C#ロジック
```

---

# 10. @pageとルーティング

`@page`を指定すると、URLからコンポーネントにアクセスできる。

```razor
@page "/counter"

<h1>Counter</h1>
```

ブラウザ：

```text
/counter
```

にアクセスすると、該当コンポーネントが表示される。

---

## ルートパラメータ

```razor
@page "/user/{id:int}"

<h1>User ID: @id</h1>

@code {
    [Parameter]
    public int id { get; set; }
}
```

URL：

```text
/user/123
```

の場合、

```text
id = 123
```

となる。

---

# 11. @code

`.razor`ファイル内にC#コードを記述する場合は、`@code`を使用する。

```razor
<h1>@message</h1>

@code {
    private string message = "Hello";

    private void ChangeMessage()
    {
        message = "Changed";
    }
}
```

ただし、コード量が多くなる場合は`.razor.cs`に分離する。

---

# 12. イベント処理

Blazorではイベント属性を使用してイベントを処理できる。

```razor
<button @onclick="OnClick">
    クリック
</button>

@code {
    private void OnClick()
    {
        Console.WriteLine("Clicked");
    }
}
```

代表的なイベント：

| イベント | 用途 |
|---|---|
| `@onclick` | クリック |
| `@onchange` | 値変更 |
| `@oninput` | 入力 |
| `@onkeydown` | キー入力 |
| `@onkeyup` | キーを離す |

---

# 13. データバインディング

UIとC#のデータを紐付けることができる。

```razor
<p>名前：@name</p>

<input @bind="name" />

@code {
    private string name = "";
}
```

入力値を変更すると、`name`の値も更新される。

---

# 14. @bind

`@bind`を使用すると、双方向データバインディングを行える。

```razor
<input @bind="name" />

<p>@name</p>
```

入力：

```text
Taro
```

結果：

```text
Taro
```

---

## @bind:event

イベントを指定することもできる。

```razor
<input
    @bind="name"
    @bind:event="oninput"
/>
```

通常の`@bind`よりも入力時にリアルタイムで値を更新できる。

---

# 15. コンポーネント間のデータ受け渡し

Blazorでは、コンポーネント間でデータを受け渡すことができる。

```text
親コンポーネント
      │
      │ Parameter
      ↓
子コンポーネント
```

逆方向にデータを返す場合は`EventCallback`を使用する。

```text
親コンポーネント
      ↑
      │ EventCallback
      │
子コンポーネント
```

---

# 16. Parameter

子コンポーネントに値を渡す場合、`[Parameter]`を使用する。

## Child.razor

```razor
<p>名前：@Name</p>

@code {
    [Parameter]
    public string Name { get; set; }
}
```

親側：

```razor
<Child Name="Taro" />
```

結果：

```text
名前：Taro
```

---

# 17. EventCallback

子コンポーネントから親コンポーネントへイベントを通知する場合に使用する。

## Child.razor

```razor
<button @onclick="OnClick">
    クリック
</button>

@code {
    [Parameter]
    public EventCallback OnClicked { get; set; }

    private async Task OnClick()
    {
        await OnClicked.InvokeAsync();
    }
}
```

親：

```razor
<Child OnClicked="HandleClick" />

@code {
    private void HandleClick()
    {
        Console.WriteLine("Child clicked");
    }
}
```

---

# 18. Layout

複数ページで共通するレイアウトを定義する。

```text
MainLayout.razor
│
├── Header
├── Navigation
├── @Body
└── Footer
```

例：

```razor
<div class="page">

    <header>
        Header
    </header>

    <main>
        @Body
    </main>

</div>
```

`@Body`にページのコンテンツが表示される。

---

# 19. wwwroot

静的ファイルを配置する。

```text
wwwroot/
├── css/
│   └── app.css
│
├── js/
│   └── app.js
│
└── images/
    └── logo.png
```

主な用途：

- CSS
- JavaScript
- 画像
- フォント
- その他静的ファイル

---

# 20. CSS

CSSを使用してUIを装飾する。

```css
button {
    padding: 10px;
    border-radius: 5px;
}
```

コンポーネントにCSSを適用する。

```razor
<button class="my-button">
    Click
</button>
```

---

## CSS Isolation

コンポーネント単位でCSSを分離できる。

```text
Counter.razor
Counter.razor.css
```

`Counter.razor.css`：

```css
h1 {
    font-size: 30px;
}
```

このCSSは対象コンポーネントにスコープされる。

---

# 21. JavaScriptとの連携

BlazorではJavaScriptを呼び出すこともできる。

JavaScript：

```javascript
function showMessage() {
    alert("Hello JavaScript");
}
```

C#：

```csharp
@inject IJSRuntime JS

<button @onclick="ShowMessage">
    Click
</button>

@code {
    private async Task ShowMessage()
    {
        await JS.InvokeVoidAsync(
            "showMessage"
        );
    }
}
```

BlazorからJavaScriptを呼び出す場合は、`IJSRuntime`を使用する。

---

# 22. Dependency Injection

BlazorではASP.NET CoreのDIを使用できる。

サービス登録：

```csharp
builder.Services.AddScoped<MyService>();
```

コンポーネント：

```razor
@inject MyService Service
```

使用：

```razor
<p>@Service.GetMessage()</p>
```

---

# 23. Service

ビジネスロジックやAPI通信などをServiceに分離する。

例：

```csharp
public class MyService
{
    public string GetMessage()
    {
        return "Hello Service";
    }
}
```

登録：

```csharp
builder.Services.AddScoped<MyService>();
```

使用：

```razor
@inject MyService Service

<p>
    @Service.GetMessage()
</p>
```

基本的な構成：

```text
Razor Component
      ↓
Service
      ↓
API / Database
```

UIにビジネスロジックを直接書かず、Serviceに分離することで保守性を高められる。

---

# 24. API通信

BlazorからWeb APIを呼び出すことができる。

`HttpClient`を使用する。

```csharp
@inject HttpClient Http

@code {
    private async Task GetData()
    {
        var result =
            await Http.GetFromJsonAsync<MyData>(
                "/api/data"
            );
    }
}
```

API側：

```csharp
[ApiController]
[Route("api/[controller]")]
public class DataController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(
            new
            {
                Message = "Hello API"
            }
        );
    }
}
```

処理の流れ：

```text
Blazor Component
      ↓
HttpClient
      ↓
ASP.NET Core Web API
      ↓
JSON
      ↓
Blazor Component
```

---

# 25. appsettings.json

アプリケーションの設定を記述する。

例：

```json
{
    "ApiSettings": {
        "BaseUrl": "https://example.com"
    }
}
```

環境ごとに設定を分けることもできる。

```text
appsettings.json
appsettings.Development.json
appsettings.Production.json
```

注意：

パスワードやAPIキーなどの機密情報を直接コミットしない。

---

# 26. 非同期処理

BlazorではAPI通信などで非同期処理を使用することが多い。

```csharp
private async Task GetData()
{
    var result =
        await Service.GetDataAsync();
}
```

イベント処理も非同期にできる。

```razor
<button @onclick="GetData">
    データ取得
</button>
```

---

# 27. フォーム

Blazorでは`EditForm`を使用してフォームを作成できる。

```razor
<EditForm Model="user" OnValidSubmit="Submit">

    <InputText
        @bind-Value="user.Name"
    />

    <button type="submit">
        送信
    </button>

</EditForm>

@code {
    private User user = new();

    private void Submit()
    {
        Console.WriteLine(user.Name);
    }

    public class User
    {
        public string Name { get; set; }
    }
}
```

---

# 28. バリデーション

DataAnnotationsを使用して入力値を検証できる。

```csharp
using System.ComponentModel.DataAnnotations;

public class User
{
    [Required]
    public string Name { get; set; }

    [EmailAddress]
    public string Email { get; set; }
}
```

フォーム：

```razor
<EditForm
    Model="user"
    OnValidSubmit="Submit"
>

    <DataAnnotationsValidator />

    <ValidationSummary />

    <InputText
        @bind-Value="user.Name"
    />

    <button type="submit">
        送信
    </button>

</EditForm>
```

---

# 29. レンダリングモード

.NET 8のBlazor Web Appでは、コンポーネントのレンダリング方式を指定できる。

代表的なモード：

```text
Static SSR
Interactive Server
Interactive WebAssembly
Interactive Auto
```

レンダリングモードによって、

- どこで処理されるか
- JavaScriptが必要か
- インタラクティブ処理をどう行うか

などが変わる。

---

# 30. Interactive Server

サーバー側でインタラクティブ処理を行う。

```razor
@rendermode InteractiveServer
```

イメージ：

```text
ブラウザ
    │
    │ 通信
    ↓
ASP.NET Core
    │
    ↓
Blazor Component
```

メリット：

- C#コードをサーバー側で実行
- WebAssemblyをダウンロードする必要がない
- サーバー側のリソースにアクセスしやすい

---

# 31. Interactive WebAssembly

ブラウザ上で.NETコードを実行する。

```razor
@rendermode InteractiveWebAssembly
```

イメージ：

```text
ブラウザ
    │
    ↓
WebAssembly
    │
    ↓
Blazor Component
    │
    ↓
API
```

メリット：

- クライアント側で処理
- サーバーとの通信を減らせる場合がある

---

# 32. Interactive Auto

初回はサーバー側で処理し、条件が整えばWebAssemblyへ移行する方式。

```razor
@rendermode InteractiveAuto
```

アプリケーションの構成によって、適切なレンダリング方式を選択する。

---

# 33. コンポーネントのライフサイクル

Blazorコンポーネントにはライフサイクルがある。

代表的なメソッド：

```csharp
OnInitialized()
OnInitializedAsync()

OnParametersSet()
OnParametersSetAsync()

OnAfterRender()
OnAfterRenderAsync()
```

初期化処理：

```csharp
protected override async Task OnInitializedAsync()
{
    // 初期データ取得
}
```

初回表示後：

```csharp
protected override async Task OnAfterRenderAsync(
    bool firstRender)
{
    if (firstRender)
    {
        // 初回描画後の処理
    }
}
```

---

# 34. 実務での基本的な構成例

実務では、以下のようにUIとロジックを分離する構成が考えられる。

```text
Components/
│
├── Pages/
│   └── User.razor
│
├── Shared/
│   └── UserTable.razor
│
Services/
└── UserService.cs

Models/
└── User.cs
```

処理の流れ：

```text
User.razor
    ↓
UserService
    ↓
API
    ↓
User Model
    ↓
User.razor
    ↓
UserTable.razor
    ↓
画面表示
```

---

# 35. 簡単なフロントエンド作成例

名前を入力して画面に表示する簡単なBlazorコンポーネントを作成する。

## ディレクトリ構成

```text
Components/
└── Pages/
    ├── UserInput.razor
    └── UserInput.razor.cs
```

---

## UserInput.razor

```razor
@page "/user-input"

<h1>ユーザー入力</h1>

<div>

    <label>
        名前：
    </label>

    <input
        @bind="name"
        @bind:event="oninput"
    />

</div>

@if (!string.IsNullOrEmpty(name))
{
    <p>
        こんにちは、@name さん！
    </p>
}
```

---

## UserInput.razor.cs

```csharp
public partial class UserInput
{
    private string name = "";
}
```

処理の流れ：

```text
ユーザーが入力
    ↓
@bind
    ↓
nameが更新
    ↓
コンポーネントが再描画
    ↓
画面に名前を表示
```

---

# よく使うRazor構文

| 構文 | 用途 |
|---|---|
| `@page` | URLルートを指定 |
| `@code` | C#コードを記述 |
| `@inject` | DIされたサービスを取得 |
| `@bind` | 双方向データバインディング |
| `@onclick` | クリックイベント |
| `@onchange` | 値変更イベント |
| `@if` | 条件分岐 |
| `@foreach` | 繰り返し |
| `@rendermode` | レンダリングモード指定 |

---

# よく使うBlazor属性

| 属性 | 用途 |
|---|---|
| `[Parameter]` | 親から値を受け取る |
| `[CascadingParameter]` | Cascading Valueから値を受け取る |
| `[Inject]` | DIされたサービスを取得 |
| `[SupplyParameterFromQuery]` | Query Stringから値を取得 |

---

# よく使うイベント

| イベント | 用途 |
|---|---|
| `@onclick` | クリック |
| `@onchange` | 値変更 |
| `@oninput` | 入力 |
| `@onkeydown` | キー押下 |
| `@onkeyup` | キーを離す |

---

# よく使うコンポーネント

| コンポーネント | 用途 |
|---|---|
| `EditForm` | フォーム |
| `InputText` | テキスト入力 |
| `InputNumber` | 数値入力 |
| `InputSelect` | セレクトボックス |
| `InputCheckbox` | チェックボックス |
| `ValidationSummary` | バリデーションエラー表示 |
| `DataAnnotationsValidator` | DataAnnotationsによる検証 |

---

# 開発時の基本的な流れ

```text
1. Blazor Web Appプロジェクト作成
        ↓
2. Razor Component作成
        ↓
3. .razorにUI作成
        ↓
4. 必要に応じて.razor.csにロジック分離
        ↓
5. Model / DTO作成
        ↓
6. Service作成
        ↓
7. DI登録
        ↓
8. APIと連携
        ↓
9. CSSでUI調整
        ↓
10. dotnet run
        ↓
11. ブラウザで確認
```

---

# よく使うコマンド

## プロジェクト作成

```bash
dotnet new blazor -n MyBlazorApp
```

## プロジェクト起動

```bash
dotnet run
```

## ビルド

```bash
dotnet build
```

## テスト

```bash
dotnet test
```

## 発行

```bash
dotnet publish
```

---
