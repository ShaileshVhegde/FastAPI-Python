from fastapi import FastAPI
from models import Product
app = FastAPI()
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

@app.get("/products")
def get_allproducts():
    return products

@app.post("/products")
def addproducts(product:Product):
    products.append(product)
    return product
    
@app.put("/products")
def updateproducts(id:int , product:Product):
    for i in range(len(products)):
        if products[i].id == id:
            
            products[i]=product
            return "Product updated sucssesfully"
    return "product not found"

@app.delete("/products")
def deleteproduct(id:int):
    for i in range(len(products)):
        if products[i].id==id:
            del products[i]
            return "product Deleted succsesfully"
    return "not product exist"
        