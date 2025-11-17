from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schema import BlogCreate, BlogResponse
from crud.blog_crud import create_blog, get_blogs, update_blog, delete_blog
from db import SessionLocal

router = APIRouter(prefix="/blogs", tags=["Blogs"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=BlogResponse)
def create(data: BlogCreate, db: Session = Depends(get_db)):
    return create_blog(db, data)


@router.get("/", response_model=list[BlogResponse])
def read(db: Session = Depends(get_db)):
    return get_blogs(db)


@router.put("/{blog_id}", response_model=BlogResponse)
def update(blog_id: int, title: str, content: str, db: Session = Depends(get_db)):
    return update_blog(db, blog_id, title, content)


@router.delete("/{blog_id}")
def delete(blog_id: int, db: Session = Depends(get_db)):
    return delete_blog(db, blog_id)
