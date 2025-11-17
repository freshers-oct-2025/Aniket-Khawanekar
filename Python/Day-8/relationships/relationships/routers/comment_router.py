from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schema import CommentCreate, CommentResponse
from crud.comment_crud import (
    create_comment, 
    get_comments,
    get_comments_by_blog,
    delete_comment
)
from db import SessionLocal

router = APIRouter(prefix="/comments", tags=["Comments"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=CommentResponse)
def create(data: CommentCreate, db: Session = Depends(get_db)):
    return create_comment(db, data)


@router.get("/", response_model=list[CommentResponse])
def read_all(db: Session = Depends(get_db)):
    return get_comments(db)


@router.get("/blog/{blog_id}", response_model=list[CommentResponse])
def read_by_blog(blog_id: int, db: Session = Depends(get_db)):
    return get_comments_by_blog(db, blog_id)


@router.delete("/{comment_id}")
def delete(comment_id: int, db: Session = Depends(get_db)):
    return delete_comment(db, comment_id)
