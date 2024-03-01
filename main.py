from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

items = []

class Item(BaseModel):
    text: str = None
    is_done: bool = False

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/items", response_model=list[Item])
def list_items(limit: int = 10):
    return items[0:limit]

@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return items

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> str:
    item = items[item_id]
    return item

