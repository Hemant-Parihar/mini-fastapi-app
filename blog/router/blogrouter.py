from typing import List

from fastapi import APIRouter, status, Depends
from blog import database
from sqlalchemy.orm import Session
from blog.model.Blog import Blog
from blog.service.BlogService import BlogService

router = APIRouter(
    prefix="/blog",
    tags=["blog"],
)

get_db = database.get_db


@router.post("", status_code=status.HTTP_201_CREATED, response_model=Blog)
def create_blog(request: Blog, db: Session = Depends(get_db)):
    return BlogService().create_blog(request, db)


@router.get("", response_model=List[Blog])
def get_all_blog(db: Session = Depends(get_db)):
    return BlogService().get_blogs(db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=Blog)
def get_blog(id, db: Session = Depends(get_db)):
    return BlogService().get_blog(id, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db)):
    return BlogService().delete_blog(id, db)
