# Backend Architecture Sample

Template based on the [Official FastAPI Template](https://github.com/fastapi/full-stack-fastapi-template).

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

Once the container is running, access the following endpoints.

- **API Server**: `http://localhost:8000`
- **Health Check**: `http://localhost:8000/`

## API Documentation

API documentation is automatically generated from the source code.

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Testing

Run tests with pytest:

```bash
uv run pytest -v
```

Test structure:

- `tests/api/`: API endpoint tests
- `tests/services/`: Service layer tests
- `tests/conftest.py`: Shared fixtures

## Database Migration

Template Alembic for database migrations.

```bash
# Create migration
uv run alembic revision --autogenerate -m "description"

# Apply migrations
uv run alembic upgrade head

# Rollback
uv run alembic downgrade -1
```

## CI/CD

GitHub Actions workflow (`.github/workflows/ci.yaml`) runs:

- Ruff lint/format check
- pytest
- Slack notification on failure

See `docs/slack-webhook-setup.md` for Slack configuration.

## Architecture

Template based on the [Official FastAPI Template](https://github.com/fastapi/full-stack-fastapi-template), incorporating **Clean Architecture** principles and extending the **Service Layer**.

### 3-Layer Architecture

1. **Presentation Layer** (`app/api`): Handles HTTP requests/responses. No business logic here.
2. **Business Logic Layer** (`app/services`): Handles complex business logic, calculations, and external integrations.
3. **Data Access Layer** (`app/crud`, `app/models`): Handles database operations.

## Directory Strategy

Roles for each directory are as follows. Place code in the appropriate location during development.

| Directory | Role | Description |
| :--- | :--- | :--- |
| `app/api/` | **Interface** | Input validation, routing. Calls `services` or `crud`. |
| `app/services/` | **Logic** | Complex business logic (calculations, file parsing, etc.). |
| `app/crud/` | **DB Actions** | **Functions** to execute queries (Create, Read, Update, Delete). |
| `app/models/` | **DB Definitions** | **Classes** defining the database table structure (SQLAlchemy). |
| `app/schemas/` | **DTO** | Pydantic models. Request/response type definition and validation. |
| `app/core/` | **Config** | Environment settings, security, common constants. |
| `tests/` | **Testing** | pytest test files and fixtures. |
| `alembic/` | **Migration** | Database migration scripts. |
| `docs/` | **Documentation** | Additional documentation. |

```text
.
├── app/
│   ├── api/             # Presentation Layer
│   ├── core/            # Configuration
│   ├── crud/            # Data Access Layer
│   ├── models/          # Data Access Layer
│   ├── schemas/         # DTO
│   ├── services/        # Business Logic Layer
│   └── main.py          # Entrypoint
├── tests/               # Testing
├── alembic/             # Database Migration
└── docs/                # Documentation
```
