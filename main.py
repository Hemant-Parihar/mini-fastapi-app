from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def index():
    return {"data": "Some Data returned."}


@app.get("/about")
def about():
    return {"data": {"About": "This site is built using fastAPI. FastApi are really good to build Asyn apis in python."}}