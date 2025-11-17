from sqlalchemy.orm import Session
from model import Comment
from schema import CommentCreate


def create_comment(db: Session, data: CommentCreate):
    comment = Comment(**data.dict())
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment


def get_comments(db: Session):
    return db.query(Comment).all()


def get_comments_by_blog(db: Session, blog_id: int):
    return db.query(Comment).filter(Comment.blog_id == blog_id).all()


def get_comments_by_user(db: Session, user_id: int):
    return db.query(Comment).filter(Comment.user_id == user_id).all()


def delete_comment(db: Session, comment_id: int):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if comment:
        db.delete(comment)
        db.commit()
    return comment
