import pytest
from httpx import AsyncClient
from fastapi import FastAPI
from notes.crud import api_router

app = FastAPI()
app.include_router(api_router)

@pytest.mark.asyncio
async def test_create_note(monkeypatch):
    # Mock DB session
    class DummySession:
        async def execute(self, *args, **kwargs): return None
        async def commit(self): pass
        async def refresh(self, note): pass
        def add(self, note): pass

    async def dummy_get_db():
        yield DummySession()

    app.dependency_overrides = {}
    app.dependency_overrides[api_router.dependencies[0].dependency] = dummy_get_db

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/notes", data={
            "title": "Test Note",
            "content": "Test Content",
            "important": "on"
        })
    assert response.status_code == 200