from pydantic import BaseModel


class UserDTO(BaseModel):
    username: str
    email: str
    password: str


class UserResponseDTO(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True
