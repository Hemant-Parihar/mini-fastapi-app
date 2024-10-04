from pydantic import BaseModel


class UserDTO(BaseModel):
    username: str
    email: str
    password: str


class UserResponseDTO(BaseModel):
    username: str
    email: str

    class Config:
        from_attributes = True
