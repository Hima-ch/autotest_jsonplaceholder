from pydantic import BaseModel

class Post(BaseModel):

    title: str
    body: str
    userId: int
    id: int