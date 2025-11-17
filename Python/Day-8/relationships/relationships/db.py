from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL="postgresql://postgres:root@localhost:5432/dataconnet"

engine=create_engine(DATABASE_URL)
SessionLocal=sessionmaker(bing=engine,autoflush=False,autocommit=False)

Base=declarative_base()