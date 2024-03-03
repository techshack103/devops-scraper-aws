from typing import Union
from fastapi import FastAPI,Query
import devtoscraper


app = FastAPI()
@app.get("/test")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/scrape/{search_query}")
async def scrape_data(search_query: str,limit: int = Query(10, description="Number of results to fetch")):
    print(search_query)
    results = await devtoscraper.scrape_dev_to_search_results(search_query)
    return results
