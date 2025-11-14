from fastapi import FastAPI ,Depends
from models import Product
import database_model
from database import SessionLocal, engine

app=FastAPI()

database_model.Base.metadata.create_all(bind=engine)
@app.get("/")
def greet():
    return"Fast api start"

Products=[
    Product(id=1,name="Phone",description="Budget phone",price=99,quantity=10),
    Product(id=2,name="Laptop",description="gaming laptop",price=999,quantity=6)
]

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = SessionLocal()
    count = db.query(database_model.Product).count()
    if count > 0:
        db.close()
        return
    for product in Products:
        db.close()
        db.add(database_model.Product(**product.model_dump()))
    db.commit()
    db.close()
init_db()

@app.get("/products")
def get_all_products(db: SessionLocal=Depends(get_db)):
    db_products=db.query(database_model.Product).all()
    return db_products

@app.get("/product/{id}")
def get_product_by_id(id:int,db: SessionLocal=Depends(get_db)):
    db_product=db.query(database_model.Product).filter(database_model.Product.id==id).first()
    if db_product:    
        return db_product
        
    return "Product Not found"
        
        
@app.post("/product")
def add_product(product:Product,db: SessionLocal=Depends(get_db)):
    db.add(database_model.Product(**product.model_dump()))
    db.commit()
    return product

@app.put("/product")
def update_product(id:int,product:Product,db: SessionLocal=Depends(get_db)):
    db_product=db.query(database_model.Product).filter(database_model.Product.id==id).first()
    if db_product:
        db_product.name=product.name
        db_product.description=product.description
        db_product.price=product.price
        db_product.quantity=product.quantity
        db.commit()
        return "Product updated"
    else:
        return "Product not found"

@app.delete("/product")
def delete_product(id:int,db:SessionLocal=Depends(get_db)):
    db_product=db.query(database_model.Product).filter(database_model.Product.id==id).first()
    if db_product:    
        db.delete(db_product)
        db.commit()
    else:    
        return "Product not found"