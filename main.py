from fastapi import FastAPI
import wikipediaapi
from fastapi.responses import FileResponse

app = FastAPI()
wiki = wikipediaapi.Wikipedia('en')

@app.get("/search/{search_term}")
async def search_wikipedia(search_term: str):
    page = wiki.page(search_term)
    
    if page.exists():
        return {
            "title": page.title,
            "summary": page.summary
        }
    else:
        return {
            "error": f"No page found for '{search_term}'"
        }

@app.get("/.well-known/ai-plugin.json")
async def ai_plugin_json():
    return FileResponse("ai-plugin.json", media_type="application/json")

@app.get("/openapi.json")
async def openapi_json():
    return FileResponse("openapi.json", media_type="application/json")