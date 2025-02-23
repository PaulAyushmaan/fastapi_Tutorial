# from typing import Union

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="template")

conn = MongoClient(
    "mongodb+srv://ayushmaanpaul2004:Bti494n9spIV32Jt@cluster0.htvhe.mongodb.net/notes")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
    newDocs = []
    # count = conn.notes.notes.count_documents({})
    # print(f"Total documents in 'notes' collection: {count}")
    for doc in docs:
        newDocs.append({
            "id": doc["_id"],
            "note": doc["note"]
        })
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})


@app.get("/items/{item_id}")
def read_items(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
