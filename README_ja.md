# Backend Architecture Sample

[FastAPI 公式テンプレート](https://github.com/fastapi/full-stack-fastapi-template) をベースにしたテンプレート。

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/k-sub1995/fastapi-template.git
cd fastapi-template
```

### 2. Run the application

```bash
docker compose up
```

## Usage

コンテナ起動後、以下のエンドポイントへアクセス可能。

- **API Server**: `http://localhost:8000`
- **Health Check**: `http://localhost:8000/`

## API Documentation

ソースコードからAPIドキュメントが自動生成される。

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Architecture

[FastAPI 公式テンプレート](https://github.com/fastapi/full-stack-fastapi-template) をベースに**Clean Architecture** の思想を取り入れ、**Service Layer** を拡張している。

### 3層アーキテクチャ

1. **プレゼンテーション層** (`app/api`): HTTPリクエスト/レスポンスのハンドリング。ここにビジネスロジックは書かない。
2. **ビジネスロジック層** (`app/services`): 複雑な業務ロジック、計算、外部連携を担当。
3. **データアクセス層** (`app/crud`, `app/models`): データベース操作を担当。

## Directory Strategy

各ディレクトリの責務は以下の通り。開発時は適切な場所に配置すること。

| ディレクトリ | 役割 | 説明 |
| :--- | :--- | :--- |
| `app/api/` | **Interface** | 入力検証、ルーティング。`services` または `crud` を呼び出す。 |
| `app/services/` | **Logic** | 複雑なビジネスロジック（計算、ファイル解析など）。 |
| `app/crud/` | **DB Actions** | クエリを実行する**関数群** (Create, Read, Update, Delete)。 |
| `app/models/` | **DB Definitions** | データベースのテーブル構造を定義する**クラス群** (SQLAlchemy)。 |
| `app/schemas/` | **DTO** | Pydanticモデル。リクエスト/レスポンスの型定義とバリデーション。 |
| `app/core/` | **Config** | 環境設定、セキュリティ、共通定数。 |

```text
app/
├── api/             # Presentation Layer
├── core/            # Configuration
├── crud/            # Data Access Layer
├── models/          # Data Access Layer
├── schemas/         # DTO
├── services/        # Business Logic Layer
└── main.py          # Entrypoint
```
