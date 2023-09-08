from sqlalchemy.orm import sessionmaker
import os
import sys
from sqlalchemy import create_engine

# Append the parent directory to the sys path to enable relative imports
Project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
db_url = "sqlite:///inventory.db"
db_file = os.path.join(Project_dir, 'models', 'inventory.db')
engine = create_engine(f'sqlite:///{db_file}')

    # Create a SQLAlchemy engine and session
engine = create_engine('sqlite:///inventory.db')
Session = sessionmaker(bind=engine)
session = Session()


# Import path for the Product class
from model import Product

class ProductClassMethods:
    @classmethod
    def create_product(cls, session: Session, name: str, description: str, quantity: int, price: int, category_id: int):
        """Create a new product and add it to the inventory."""
        product = Product(name=name, description=description, quantity=quantity, price=price, category_id=category_id)

        session.add(product)
        session.commit()


session = Session() 
product1 = Product('Sugar', 'Mumias', 30, 200, 1)
product1.create_product()
