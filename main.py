from fastapi import Depends, FastAPI
from models import Product
from fastapi.middleware.cors import CORSMiddleware
from database import session,engine
import database_models
from sqlalchemy.orm import Session
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"]
)

database_models.Base.metadata.create_all(bind=engine)
@app.get("/")
def greet():
    return "welcome to first app"



products= [
    Product(
        id=1,
        name="iPhone 15",
        description="Apple smartphone with A16 Bionic chip",
        price=79999,
        quantity=5
    ),

    Product(
        id=2,
        name="Samsung Galaxy S24",
        description="Flagship Android phone with AMOLED display",
        price=74999,
        quantity=8
    ),

    Product(
        id=3,
        name="OnePlus 12",
        description="Fast performance smartphone with Snapdragon processor",
        price=64999,
        quantity=12
    ),

    Product(
        id=4,
        name="Boat Rockerz 450",
        description="Wireless Bluetooth headphones",
        price=1499,
        quantity=25
    ),

    Product(
        id=5,
        name="Dell Inspiron 15",
        description="Laptop with Intel i5 processor and 16GB RAM",
        price=58999,
        quantity=4
    )
]

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
def init_db():
    db=session()
    count=db.query(database_models.Product).count
    if count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
        db.commit()    
init_db()

@app.get("/products")
def get_allproducts(db: Session = Depends(get_db)):
    db_products = db.query(database_models.Product).all()
    return db_products

@app.get("/products/{id}")
def get_product_by_id(id:int,db: Session = Depends(get_db)):
    db_produt= db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_produt:
        return db_produt
    else:
       return "product not found"
@app.post("/products")
def addproducts(product:Product,db: Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product
    
@app.put("/products/{id}")
def updateproducts(id:int , product:Product,db: Session = Depends(get_db)):
    db_cheack = db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if db_cheack:
        db_cheack.name = product.name
        db_cheack.price=product.price
        db_cheack.id=product.id
        db_cheack.description=product.description
        db_cheack.quantity=product.quantity
        db.commit()
        return "product upadated"
    else:
        return " product not fount"
   

@app.delete("/products/{id}")
def deleteproduct(id:int,db: Session = Depends(get_db)):
    
    db_cheack = db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if db_cheack:
        db.delete(db_cheack) 
        db.commit() 
    else:
       return "not product exist"
        