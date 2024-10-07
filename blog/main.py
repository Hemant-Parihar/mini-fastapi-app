from fastapi import FastAPI

from .database import engine, Base
from blog.router import blogrouter, users, authentication

app = FastAPI()

app.include_router(authentication.router)
app.include_router(blogrouter.router)
app.include_router(users.router)

Base.metadata.create_all(engine)
