from sqlalchemy.orm import Session
from model import Blog
from schema import BlogCreate


def create_blog(db: Session, data: BlogCreate):
    blog = Blog(**data.dict())
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog


def get_blogs(db: Session):
    return db.query(Blog).all()


def get_blog_by_id(db: Session, blog_id: int):
    return db.query(Blog).filter(Blog.id == blog_id).first()


def delete_blog(db: Session, blog_id: int):
    blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if blog:
        db.delete(blog)
        db.commit()
    return blog


def update_blog(db: Session, blog_id: int, title: str, content: str):
    blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if blog:
        blog.title = title
        blog.content = content
        db.commit()
        db.refresh(blog)
    return blog
