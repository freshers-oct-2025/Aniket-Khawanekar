from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schema import UserCreate, UserResponse
from crud.user_crud import create_user, get_users, update_user, delete_user
from db import SessionLocal

router = APIRouter(prefix="/users", tags=["Users"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=UserResponse)
def create(data: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, data)


@router.get("/", response_model=list[UserResponse])
def read_users(db: Session = Depends(get_db)):
    return get_users(db)


@router.put("/{user_id}", response_model=UserResponse)
def update(user_id: int, name: str, db: Session = Depends(get_db)):
    return update_user(db, user_id, name)


@router.delete("/{user_id}")
def delete(user_id: int, db: Session = Depends(get_db)):
    return delete_user(db, user_id)
