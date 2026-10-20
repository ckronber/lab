from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

class Item(BaseModel):
    name: str 

# Define items at application start
items = {"rock", "paper", "scissors"}

app = FastAPI()

@app.delete("/items")
# Make asynchronous
async def root(item: Item):
    name = item.name
    # Check if name is in items
    if name not in items:
        # Return the status code for not found
        raise HTTPException(status_code=404, detail="Item not found.")
    items.remove(name)
    return {"message": "Item deleted"}