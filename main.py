from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="MCP Server Example")

class SearchRequest(BaseModel):
    query: str

class SearchResult(BaseModel):
    id: str
    title: str
    snippet: str

class SearchResponse(BaseModel):
    results: List[SearchResult]

class FetchRequest(BaseModel):
    ids: List[str]

class FetchItem(BaseModel):
    id: str
    content: str

class FetchResponse(BaseModel):
    items: List[FetchItem]

@app.post("/search", response_model=SearchResponse)
async def search(request: SearchRequest):
    # Example search implementation returning placeholder results
    results = [
        SearchResult(id="1", title=f"Result for {request.query}", snippet=f"Sample snippet about {request.query}."),
        SearchResult(id="2", title=f"Another result for {request.query}", snippet=f"Another snippet about {request.query}.")
    ]
    return SearchResponse(results=results)

@app.post("/fetch", response_model=FetchResponse)
async def fetch(request: FetchRequest):
    # Example fetch implementation returning placeholder content
    items = []
    for id in request.ids:
        items.append(FetchItem(id=id, content=f"Content for id {id}."))
    return FetchResponse(items=items)
