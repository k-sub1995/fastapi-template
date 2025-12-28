# Backend Architecture Sample (Extended Official Template)

This project follows the **Official FastAPI Template** structure, extended with a **Service Layer** to accommodate complex business logic (Clean Architecture / 3-Layer Architecture approach).

## Table of Contents

<!-- TOC -->
- [Backend Architecture Sample (Extended Official Template)](#backend-architecture-sample-extended-official-template)
  - [Table of Contents](#table-of-contents)
  - [Directory Structure](#directory-structure)
  - [Layered Architecture Mapping](#layered-architecture-mapping)
  - [Key Concepts](#key-concepts)
    - [Why services and crud?](#why-services-and-crud)
    - [Data Flow](#data-flow)


## Directory Structure

```text
app/
├── api/             # [Presentation Layer] Router & Endpoints
│   └── v1/
│       └── endpoints/
├── services/        # [Business Logic Layer] Complex Logic (Excel, AI)
├── crud/            # [Data Access Layer] Database CRUD Operations
├── models/          # [Data Access Layer] Database Models (SQLAlchemy)
├── schemas/         # [DTO] Data Transfer Objects (Pydantic)
├── core/            # Configuration & Security
└── main.py          # App Entrypoint
```

## Layered Architecture Mapping

We map these directories to the standard **3-Layer Architecture** (Separation of Concerns).

| Layer | Directory | Role |
| :--- | :--- | :--- |
| **1. Presentation** | `api/` | **Interface**. Handles HTTP requests/responses. Validates inputs using `schemas`. Calls `services` or `crud`. **No business logic here.** |
| **2. Buisness / Service** | `services/` | **Logic**. Where the "magic" happens. Excel parsing, AI Prompting, Statistics calculation. Orchestrates `crud` operations. |
| **3. Data Access** | `crud/`  `models/` | **Persistence**. Direct interaction with the Database. `models` define the table structure. `crud` executes SQL queries. |

## Key Concepts

### Why services and crud?

- **CRUD**: For simple resource management (e.g., "Create User", "Get Item"). Official template puts logic here if simple.
- **Service**: For operations that don't map 1:1 to a DB table or require significant processing *before* saving (e.g., "Parse Resume Excel", "Generate AI Feedback").

### Data Flow

1. **Request** comes to `api/` (validated by `schemas`).
2. `api/` calls `services/` (for complex tasks) or `crud/` (for simple tasks).
3. `services/` processes data and calls `crud/` to save/retrieve.
4. `crud/` uses `models/` to query the Database.
5. **Response** is returned as `schemas` (DTO).

## How to Run (Sample)

### Prerequisites

- Python 3.13+ (with [uv](https://github.com/astral-sh/uv) installed)
- Docker

### Local Development (uv)

```bash
# Install dependencies
uv sync

# Run server
uv run uvicorn app.main:app --reload
```

### Docker

```bash
docker compose up --build
```

Access swagger docs at: [http://localhost:8000/docs](http://localhost:8000/docs)
