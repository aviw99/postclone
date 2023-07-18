from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
from vars import requests
app = FastAPI()


req_get_all, req_get_id, req_get_name, req_post, req_put_id, req_delete_id = requests()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get(req_get_all)
def read_root():
    return {"Hello": "World"}


@app.get(req_get_id)
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put(req_put_id)
def update_item(item_id: int, item: Item):
    return{'item_name': item.name, 'item_id': item_id, 'is_offer': item.is_offer}
