from pydantic import BaseModel

class UserCreate(BaseModel):
    name:str
    
class UserResponse(BaseModel):
    id:int
    name:str 
    class config:
        orm_mode=True
        
class BlogCreate(BaseModel):
    title:str
    content:str
    user_id:int
    
class BlogResponse(BaseModel):
    id: int
    title: str
    content: str
    class Config:
        from_attributes=True


class CommentCreate(BaseModel):
    text: str
    blog_id: int
    user_id: int


class CommentResponse(BaseModel):
    id: int
    text: str
    class Config:
        from_attributes=True