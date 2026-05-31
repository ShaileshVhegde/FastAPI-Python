from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url="postgresql://postgres:SVHsvh123321pg@localhost:5432/Shailesh"
engine=create_engine(db_url)

session=sessionmaker(autocommit=False, autoflush=False, bind=engine)