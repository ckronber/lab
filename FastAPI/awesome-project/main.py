from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import typing


class Item(BaseModel):
    id : int 
    name: str 
    description: str 
    price: float 
    isoffer: bool 

# Define items at application start
#items = {"bananas": "Yellow fruit."}
items = {"apples", "oranges"}

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
    
# get with 
@app.get("/hello")
def hello(name:str = "Alan"):
    return {"message":f"Hello {name}"}

@app.put("/items")
def update_item(item: Item):
    name= item.name
    # Update the description
    items[item] = item.description
    return item

@app.delete("/items")
def delete_item(item: Item):
    name = item.name
    # Delete the item
    if name in items:
        items.remove(name)
    else:
        # Raise HTTPException with status code for "not found"
        raise HTTPException(status_code=404, detail="Item not found.")
    return {}

"""
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.post("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
"""