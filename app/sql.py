from sqlalchemy import create_engine  
from sqlalchemy import Column, String  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker
from os import environ

db_user = "inventory-app"
db_password = environ["POSTGRES_PASSWORD"]
db_string = "postgres://" + db_user + ":" + db_password + "@db/"

db = create_engine(db_string)  
base = declarative_base()

class Ingredient(base):  
    __tablename__ = 'ingredients'

    barcode = Column(String, primary_key=True)
    name = Column(String)

Session = sessionmaker(db)  
session = Session()

base.metadata.create_all(db)

# Create 
ground_beef = Ingredient(barcode="9685310001", name="Ground Beef")  
session.add(ground_beef)  
session.commit()

# Read
ingredients = session.query(Ingredient)  
for i in ingredients:  
    print(i.name)


# Delete
session.delete(ground_beef)  
session.commit() 
