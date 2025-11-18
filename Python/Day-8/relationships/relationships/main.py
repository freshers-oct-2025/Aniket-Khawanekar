from fastapi import FastAPI
from db import Base, engine
from routers import user_router, blog_router, comment_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router.router)
app.include_router(blog_router.router)
app.include_router(comment_router.router)