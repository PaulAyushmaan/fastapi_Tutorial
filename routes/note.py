from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Request, APIRouter
from models.note import Note
from config.db import conn
from schemas.note import noteEntity, notesEntity
from fastapi.templating import Jinja2Templates
note = APIRouter()

templates = Jinja2Templates(directory="template")


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
    newDocs = []
    # count = conn.notes.notes.count_documents({})
    # print(f"Total documents in 'notes' collection: {count}")
    for doc in docs:
        newDocs.append({
            "title": doc["title"],
            "desc": doc["desc"],
            "important": doc["important"]
        })
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})


@note.post("/")
async def create_note(request: Request):
    form = await request.form()
    formDict = dict(form)

    # type: ignore
    formDict["important"] = True if formDict.get(  # type: ignore
        "important") == "on" else False
    note = conn.notes.notes.insert_one(formDict)
    return {"Success": True}
