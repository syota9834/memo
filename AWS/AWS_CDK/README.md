# AWS CDK

## 1. 概要

AWS CDK（Cloud Development Kit）は、プログラミング言語を使用してAWSのインフラストラクチャをコードで定義・構築するためのIaC（Infrastructure as Code）ツール。

TypeScript、JavaScript、Python、Java、C#、Goなどのプログラミング言語を使用してAWSリソースを定義できる。

TypeScriptを使用する場合、CDKのコードを記述すると、最終的にAWS CloudFormationのテンプレートが生成される。

基本的な流れ：

```text
TypeScript
    ↓
AWS CDK
    ↓
CloudFormation Template
    ↓
AWSリソースを作成・更新
```

---

## 2. AWS CDKの基本概念

AWS CDKでは、主に以下の3つの概念を使用する。

| 概念 | 説明 |
|---|---|
| App | CDKアプリケーション全体 |
| Stack | AWSリソースをまとめる単位 |
| Construct | AWSリソースを定義する単位 |

基本的な構造：

```text
App
└── Stack
    ├── Construct
    ├── Construct
    └── Construct
```

---

## 3. CDK CLIのインストール

AWS CDK CLIをインストールする。

```bash
npm install -g aws-cdk
```

インストール確認：

```bash
cdk --version
```

---

## 4. CDKプロジェクトの作成

プロジェクト用のディレクトリを作成する。

```bash
mkdir my-cdk-app

cd my-cdk-app
```

TypeScriptを使用したCDKプロジェクトを作成する。

```bash
cdk init app --language typescript
```

プロジェクト作成後の構成例：

```text
my-cdk-app/
├── bin/
│   └── my-cdk-app.ts
├── lib/
│   └── my-cdk-app-stack.ts
├── test/
│   └── my-cdk-app.test.ts
├── cdk.json
├── package.json
├── package-lock.json
├── tsconfig.json
└── README.md
```

---

## 5. CDKプロジェクトの主なファイル

| ファイル | 用途 |
|---|---|
| `bin/` | CDKアプリケーションのエントリーポイント |
| `lib/` | AWSリソースを定義するコード |
| `test/` | CDKコードのテスト |
| `cdk.json` | CDK CLIの設定 |
| `package.json` | Node.jsパッケージ管理 |
| `tsconfig.json` | TypeScriptの設定 |

---

## 6. binファイル

`bin/`にはCDKアプリケーションのエントリーポイントを記述する。

例：

```typescript
#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { MyCdkAppStack } from '../lib/my-cdk-app-stack';

const app = new cdk.App();

new MyCdkAppStack(
  app,
  'MyCdkAppStack'
);
```

ここではCDKの`App`を作成し、その中に`Stack`を追加している。

---

## 7. Stack

`Stack`は、AWSリソースをまとめる単位。

例：

```typescript
import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';

export class MyCdkAppStack extends cdk.Stack {

  constructor(
    scope: Construct,
    id: string,
    props?: cdk.StackProps
  ) {

    super(
      scope,
      id,
      props
    );

  }
}
```

AWSリソースは、このStackの中に定義する。

---

## 8. Construct

Constructは、AWSリソースを定義するための基本単位。

例えばS3バケットを作成する。

```typescript
import * as s3 from 'aws-cdk-lib/aws-s3';

const bucket = new s3.Bucket(
  this,
  'MyBucket'
);
```

基本構造：

```text
new Construct(
    scope,
    id,
    props
)
```

- `scope`：Constructの親
- `id`：Constructを識別するID
- `props`：AWSリソースの設定

---

## 9. S3バケットを作成

S3バケットを作成する。

```typescript
import * as s3 from 'aws-cdk-lib/aws-s3';

const bucket = new s3.Bucket(
  this,
  'MyBucket',
  {
    versioned: true,
  }
);
```

バージョニングを有効にする場合：

```typescript
versioned: true
```

---

## 10. Lambda関数を作成

Lambda関数を作成する。

```typescript
import * as lambda from 'aws-cdk-lib/aws-lambda';

const fn = new lambda.Function(
  this,
  'MyFunction',
  {
    runtime: lambda.Runtime.NODEJS_20_X,

    handler: 'index.handler',

    code: lambda.Code.fromAsset(
      'lambda'
    ),
  }
);
```

ディレクトリ構成：

```text
project/
├── lambda/
│   └── index.js
├── bin/
├── lib/
└── package.json
```

Lambdaコード：

```javascript
exports.handler = async (event) => {

    return {
        statusCode: 200,
        body: "Hello World"
    };

};
```

---

## 11. API Gateway + Lambda

LambdaとAPI Gatewayを組み合わせる。

```typescript
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as apigateway from 'aws-cdk-lib/aws-apigateway';


const fn = new lambda.Function(
  this,
  'MyFunction',
  {
    runtime: lambda.Runtime.NODEJS_20_X,

    handler: 'index.handler',

    code: lambda.Code.fromAsset(
      'lambda'
    ),
  }
);


const api = new apigateway.LambdaRestApi(
  this,
  'MyApi',
  {
    handler: fn,
  }
);
```

構成：

```text
Client
   ↓
API Gateway
   ↓
Lambda
   ↓
処理
```

---

## 12. DynamoDBテーブルを作成

DynamoDBテーブルを作成する。

```typescript
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb';

const table = new dynamodb.Table(
  this,
  'MyTable',
  {
    partitionKey: {
      name: 'id',
      type: dynamodb.AttributeType.STRING,
    },
  }
);
```

パーティションキー：

```text
id
```

データ型：

```text
STRING
```

---

## 13. LambdaからDynamoDBへのアクセス権限

LambdaからDynamoDBを操作する場合、IAM権限を付与する。

```typescript
table.grantReadWriteData(fn);
```

これにより、LambdaにDynamoDBへの読み書き権限を付与できる。

構成：

```text
Lambda
    │
    │ IAM Role
    ↓
DynamoDB
```

CDKでは、リソース間の権限設定もコードで定義できる。

---

## 14. VPC

VPCを作成する。

```typescript
import * as ec2 from 'aws-cdk-lib/aws-ec2';

const vpc = new ec2.Vpc(
  this,
  'MyVpc',
  {
    maxAzs: 2,
  }
);
```

VPCの構成例：

```text
VPC
├── Availability Zone A
│   ├── Public Subnet
│   └── Private Subnet
│
└── Availability Zone B
    ├── Public Subnet
    └── Private Subnet
```

CDKでは、VPCに必要なリソースをある程度まとめて構築できる。

---

## 15. Constructの依存関係

CDKでは、AWSリソース間の関係をコードで定義できる。

例えば：

```text
API Gateway
    ↓
Lambda
    ↓
DynamoDB
```

CDKコード：

```typescript
const table = new dynamodb.Table(
  this,
  'MyTable',
  {
    partitionKey: {
      name: 'id',
      type: dynamodb.AttributeType.STRING,
    },
  }
);


const fn = new lambda.Function(
  this,
  'MyFunction',
  {
    runtime: lambda.Runtime.NODEJS_20_X,

    handler: 'index.handler',

    code: lambda.Code.fromAsset(
      'lambda'
    ),
  }
);


table.grantReadWriteData(fn);
```

リソース間の権限や依存関係をCDK側で定義できる。

---

## 16. cdk synth

CDKコードからCloudFormationテンプレートを生成する。

```bash
cdk synth
```

処理の流れ：

```text
TypeScript
    ↓
cdk synth
    ↓
CloudFormation Template
```

生成されたCloudFormationテンプレートを確認することで、CDKがどのようなAWSリソースを作成するか確認できる。

---

## 17. cdk diff

現在のAWS環境と、CDKコードとの差分を確認する。

```bash
cdk diff
```

リソースの追加・変更・削除などを事前に確認できる。

本番環境にデプロイする前に確認すると安全。

---

## 18. cdk deploy

CDKで定義したAWSリソースをデプロイする。

```bash
cdk deploy
```

処理の流れ：

```text
TypeScript
    ↓
cdk synth
    ↓
CloudFormation
    ↓
AWSリソースを作成・更新
```

確認を省略する場合：

```bash
cdk deploy --require-approval never
```

---

## 19. cdk destroy

CDKで作成したStackを削除する。

```bash
cdk destroy
```

AWS上のリソースが削除される可能性があるため注意。

特にS3やDynamoDBなどのデータを保持するリソースを削除する場合は注意する。

---

## 20. 実務での基本的な流れ

AWS CDKを使用した開発では、基本的に以下の流れで作業する。

```text
1. CDKプロジェクトを作成
        ↓
2. TypeScriptでAWSリソースを定義
        ↓
3. npm run build
        ↓
4. cdk synth
        ↓
5. cdk diff
        ↓
6. cdk deploy
        ↓
7. AWSリソースを確認
```

基本的なコマンド：

```bash
# TypeScriptをコンパイル
npm run build

# CloudFormationテンプレートを生成
cdk synth

# 差分を確認
cdk diff

# AWSへデプロイ
cdk deploy

# Stackを削除
cdk destroy
```

---

## AWS CDKの基本構成

```text
CDK App
│
├── bin/
│   └── app.ts
│
├── lib/
│   └── app-stack.ts
│
├── lambda/
│   └── index.js
│
├── test/
│   └── app-stack.test.ts
│
├── cdk.json
├── package.json
└── tsconfig.json
```

---

## CDKでよく使用するAWSリソース

| CDKモジュール | AWSサービス |
|---|---|
| `aws-s3` | S3 |
| `aws-lambda` | Lambda |
| `aws-apigateway` | API Gateway |
| `aws-dynamodb` | DynamoDB |
| `aws-ec2` | EC2 / VPC |
| `aws-ecs` | ECS |
| `aws-rds` | RDS |
| `aws-cloudfront` | CloudFront |
| `aws-route53` | Route 53 |
| `aws-iam` | IAM |
| `aws-sqs` | SQS |
| `aws-sns` | SNS |

---

## CDKのコード例

### S3

```typescript
import * as s3 from 'aws-cdk-lib/aws-s3';

const bucket = new s3.Bucket(
  this,
  'MyBucket'
);
```

### Lambda

```typescript
import * as lambda from 'aws-cdk-lib/aws-lambda';

const fn = new lambda.Function(
  this,
  'MyFunction',
  {
    runtime: lambda.Runtime.NODEJS_20_X,
    handler: 'index.handler',
    code: lambda.Code.fromAsset(
      'lambda'
    ),
  }
);
```

### DynamoDB

```typescript
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb';

const table = new dynamodb.Table(
  this,
  'MyTable',
  {
    partitionKey: {
      name: 'id',
      type: dynamodb.AttributeType.STRING,
    },
  }
);
```

### IAM権限

```typescript
table.grantReadWriteData(fn);
```

---
