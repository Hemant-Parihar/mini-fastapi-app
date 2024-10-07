from datetime import datetime, timedelta, timezone
from typing import Union

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

import jwt
from blog.Entities import UserEntity
from blog.database import get_db
from blog.hashing import verify_password
from blog.model.request import Login, Token

router = APIRouter(tags=["Authentication"])


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@router.post("/login")
def login(request: Login, db: Session = Depends(get_db)):
    user = db.query(UserEntity).filter(UserEntity.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    if not verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Wrong Password")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

