from fastapi import APIRouter, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from notes.models import Note
from notes.database import get_db
from notes.logger import logger  # Import logger
from sqlalchemy.future import select
import os

api_router = APIRouter()

TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "templates")
templates = Jinja2Templates(directory=TEMPLATES_DIR)

@api_router.get("/notes")
async def read_notes(request: Request, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Note))
    notes = result.scalars().all()
    return templates.TemplateResponse(request, "index.html", {"notes": notes, "message": None, "error": None})

@api_router.post("/notes")
async def create_note(
    request: Request,
    title: str = Form(...),
    content: str = Form(...),
    important: bool = Form(False),
    db: AsyncSession = Depends(get_db)
):
    try:
        note = Note(title=title, content=content, important=important)
        db.add(note)
        await db.commit()
        await db.refresh(note)
        logger.info(f"Note added: {note.title} (id={note.id})")
        message = "Note added!"
        error = None
    except Exception as e:
        logger.error(f"Note not added: {e}")
        message = None
        error = "Note not added"
    result = await db.execute(select(Note))
    notes = result.scalars().all()
    return templates.TemplateResponse(request, "index.html", {"notes": notes, "message": message, "error": error})

@api_router.post("/notes/{note_id}")
async def delete_note(
    request: Request,
    note_id: int,
    method: str = Form(...),
    db: AsyncSession = Depends(get_db)
):
    if method == "delete":
        result = await db.execute(select(Note).where(Note.id == note_id))
        note = result.scalars().first()
        if note:
            await db.delete(note)
            await db.commit()
            logger.info(f"Note deleted: {note.title} (id={note.id})")
            message = "Note deleted successfully"
            error = None
        else:
            logger.warning(f"Attempted to delete non-existent note (id={note_id})")
            message = None
            error = "Note not found"
    else:
        logger.warning(f"Invalid method for delete_note: {method}")
        message = None
        error = "Invalid method"
    result = await db.execute(select(Note))
    notes = result.scalars().all()
    return templates.TemplateResponse(request, "index.html", {"notes": notes, "message": message, "error": error})