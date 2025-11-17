
from sqlalchemy.orm import Session
from model import User
from schema import UserCreate


def create_user(db: Session, data: UserCreate):
    user = User(name=data.name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_users(db: Session):
    return db.query(User).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user


def update_user(db: Session, user_id: int, name: str):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.name = name
        db.commit()
        db.refresh(user)
    return user
