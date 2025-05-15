# 📝 FastAPI Notes App

A simple yet production-ready Notes application built using **FastAPI**, **SQLAlchemy (async)**, **PostgreSQL**, and **Docker**.

> 📦 Built for local development and containerized deployment.

---

## 🚀 Features

* 🧠 Create, view, and delete notes
* ⭐ Mark notes as important
* ⚡ Asynchronous database access via `SQLAlchemy 2.0`
* 🖥️ Responsive UI with a Bootstrap-based template
* 🐳 Dockerized: Works identically on all systems
* 🔧 Config-driven via `.env` file
* ✅ Includes test scaffolding with `pytest`

---

## 📁 Project Structure

```bash
.
├── alembic/               # Alembic migrations
│   └── versions/
├── docs/                  # Project documentation
│   └── index.md
├── infra/                 # Docker & infrastructure
│   ├── docker-compose.yml
│   └── .env               # Environment config
├── src/                   # Source code
│   ├── main.py            # FastAPI entry point
│   └── notes/             # App logic (CRUD, models, db, etc.)
│       ├── crud.py
│       ├── database.py
│       ├── logger.py
│       └── models.py
└── tests/                 # Pytest test cases
```

---

## 🐳 Running with Docker (Recommended)

### 1⃣ Clone the Repo

```bash
git clone https://github.com/yourusername/notesapp.git
cd notesapp
```

### 2⃣ Set Up `.env`

Create your own `infra/.env` file for database credentials:

```env
POSTGRES_USER=youruser
POSTGRES_PASSWORD=yourpassword
POSTGRES_DB=notesdb
DATABASE_URL=postgresql+asyncpg://youruser:yourpassword@db:5432/notesdb
```

### 3⃣ Build & Start Containers

```bash
docker compose -f infra/docker-compose.yml up --build
```

This will:

* Build the Docker image for the FastAPI app
* Start both the API (`web`) and PostgreSQL (`db`) containers

### 4⃣ Apply Database Migrations

After the containers are running and the DB is ready:

```bash
docker compose -f infra/docker-compose.yml exec web alembic upgrade head
```

> 📝 This applies any pending database schema migrations.

---

## 🌐 Access the App

Visit: [http://localhost:8000/notes](http://localhost:8000/notes)

---

## 🧪 Running Locally Without Docker

### 1⃣ Install Requirements

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements/prod.txt
```

### 2⃣ Create `.env` File

Copy `infra/.env` to project root or adjust the path in your config.

### 3⃣ Run App Locally

```bash
uvicorn src.main:app --reload
```

---

## 🧪 Running Tests

```bash
pytest
```

> Test files live in the `tests/` directory.

---

## 💡 Migrations: Alembic Commands

Create a migration after editing models:

```bash
docker compose -f infra/docker-compose.yml exec web alembic revision --autogenerate -m "Add something"
```

Apply it:

```bash
docker compose -f infra/docker-compose.yml exec web alembic upgrade head
```

---

## 📄 Docs

Project documentation lives in:

```
docs/index.md
```
