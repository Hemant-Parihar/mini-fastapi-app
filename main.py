from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"data": "Check docs at /docs"}


@app.get("/about")
def about():
    return {"data": {"About": "This site is built using fastAPI. FastApi are really good to build Asyn apis in python."}}