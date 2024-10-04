from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str

    class config:
        from_attributes = True
