import pytest
from fastapi.testclient import TestClient
from fastapi import FastAPI
from notes.crud import api_router
from notes.database import get_db

app = FastAPI()
app.include_router(api_router)

@pytest.mark.asyncio
async def test_create_note(monkeypatch):
    # Mock DB session and result
    class DummyResult:
        def scalars(self):
            class DummyScalars:
                def all(self):
                    return []
            return DummyScalars()

    class DummySession:
        async def execute(self, *args, **kwargs): return DummyResult()
        async def commit(self): pass
        async def refresh(self, note): pass
        def add(self, note): pass

    async def dummy_get_db():
        yield DummySession()

    app.dependency_overrides[get_db] = dummy_get_db

    with TestClient(app=app, base_url="http://test") as client:
        response = client.post("/notes", data={
            "title": "Test Note",
            "content": "Test Content",
            "important": "on"
        })
    assert response.status_code == 200