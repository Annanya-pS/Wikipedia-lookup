from fastapi import FastAPI
import wikipedia

app = FastAPI(title="Wikipedia Lookup API")

@app.get("/")
async def get_wikipedia_url(topic: str):
    """
    Get exact Wikipedia URL for a topic.
    """
    try:
        wikipedia.set_lang("en")
        page = wikipedia.page(topic, auto_suggest=False)
        return {"topic": topic, "url": page.url}
    except:
        return {"topic": topic, "url": "https://en.wikipedia.org/wiki/Main_Page"}
