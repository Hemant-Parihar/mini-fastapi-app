from pydantic import BaseModel

from blog.model.User import UserResponseDTO


class Blog(BaseModel):
    title: str
    body: str


class BlogResponse(Blog):
    user: UserResponseDTO
