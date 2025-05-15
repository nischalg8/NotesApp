# FastAPI Notes App
# FastAPI Notes App

A simple notes application built with FastAPI, SQLAlchemy, PostgreSQL, and Docker.

## Features

- Create, view, and delete notes
- Mark notes as important
- Responsive Bootstrap Template UI used 
- Async database operations 
- Dockerized for easy deployment

## Getting Started

### Prerequisites

- Docker & Docker Compose
- Python 3.11+ (for local development/testing)

### Running with Docker

## Build-containers

docker compose -f infra/docker-compose.yml up --build


## Apply migrations 


docker compose -f infra/docker-compose.yml exec web alembic upgrade head


## Visit [http://localhost:8000/notes](http://localhost:8000/notes) in your browser.

### Running Locally

1. Install dependencies:
    
    pip install -r requirements/prod.txt
    
2. Set up your `.env` file (see `infra/.env` for an example).
3. Run the app:
    
    uvicorn src.main:app --reload
    

## Project Structure

```
src/
  notes/
    crud.py
    database.py
    logger.py
    models.py
    ...
  templates/
    index.html
  main.py
alembic/
  versions/
infra/
  docker-compose.yml
  .env
docs/
  index.md
```

## Testing

- Tests are in the `tests/` directory.
- Run tests with:
    pytest

