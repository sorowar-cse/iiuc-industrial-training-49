from fastapi import FastAPI
import uvicorn

app = FastAPI()


news = {
    1: {"title": "News 1", "content": "This is the content of news 1", "author": "Author 1"},
    2: {"title": "News 2", "content": "This is the content of news 2", "author": "Author 2"},
    3: {"title": "News 3", "content": "This is the content of news 3", "author": "Author 3"},
    4: {"title": "News 4", "content": "This is the content of news 4", "author": "Author 4"},
    5: {"title": "News 5", "content": "This is the content of news 5", "author": "Author 5"}
}


@app.get("/")
def working():
    return {"Heyyyy!": "It's working!"}


@app.get("/news")
def all_news():
    return {"news": "All the news will be displayed here."}


@app.get("/news/{news_id}")
def read_news(news_id: int):
    if news_id in news:
        return news[news_id]
    else:
        return {"error": "News of ID- {news_id} not found!"}
    
@app.get("/news/{news_id}/content")
def news_by_title_query


if __name__ == "__myapi__":
    # uvicorn.run(app, host="localhost", port=8000, reload=True)
    uvicorn.run("basic:app", host="localhost", port=8000, reload=True)