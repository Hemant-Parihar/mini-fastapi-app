from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from blog import database
from blog.model.User import UserDTO, UserResponseDTO
from blog.service.UserService import UserService
from blog.router.authentication import get_current_active_user

router = APIRouter(
    prefix="/user",
    tags=["user"],
)

get_db = database.get_db


@router.post("", status_code=status.HTTP_201_CREATED, response_model=UserResponseDTO)
def create_user(request: UserDTO, db: Session = Depends(get_db)):
    return UserService().create_user(request, db)


@router.get("", response_model=List[UserResponseDTO])
def get_all_user(db: Session = Depends(get_db)):
    return UserService().get_all_user(db)


@router.get('/get_current_active_user', response_model=UserResponseDTO)
def get_current_active_user(current_user: UserResponseDTO = Depends(get_current_active_user)):
    return current_user
