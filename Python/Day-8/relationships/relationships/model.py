from sqlalchemy  import Column,Integer,String,ForeignKey,Text
from sqlalchemy.orm import relationship
from db import Base

class User(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    email=Column(String,unique=True)

    blogs=relationship("Blog",back_populates="owner")
    
class Blog(Base):
    __tablename__="blogs"
    
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    description=Column(Text)
    user_id=Column(Integer,ForeignKey("users.id"))
    
    owner=relationship("Users",back_populates="blogs")
    
    comments=relationship("Comment",back_populates="blogs")
    

class Comment(Base):
    __tablename__="comments"
    
    id=Column(Integer,primary_key=True)
    message=Column(Text)
    
    blog_id=Column(Integer,ForeignKey("blogs.id"))
    user_id=Column(Integer,ForeignKey("users.id"))
    
    blog=relationship("Blog",back_populates="comments")

