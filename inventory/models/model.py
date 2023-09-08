from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os
import sys

Project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    # Define your database connection URL
import os

# Define the absolute path to the database file
db_file = os.path.join(os.path.dirname(__file__), 'inventory.db')

# Use the absolute path to create the engine
engine = create_engine(f'sqlite:///{db_file}')

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Category(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    products = relationship('Product', back_populates='category')

    @classmethod
    def create(cls, name):
        category = cls(name=name)
        session.add(category)
        session.commit()
        return category

    @classmethod
    def get_by_id(cls, category_id):
        return session.query(cls).filter_by(id=category_id).first()

    @classmethod
    def list_categories(cls):
        return session.query(cls).all()

    def __str__(self):
        return self.name


class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    quantity = Column(Integer, default=0)
    price = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category', back_populates='products')
    
    #  relationship with Supplier
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))
    supplier = relationship('Supplier', back_populates='products')  



    @classmethod
    def create(cls, name, description, quantity, price, category, supplier):
        product = cls(name=name, description=description, quantity=quantity, price=price, category=category, supplier=supplier)
        session.add(product)
        session.commit()
        return product

    @classmethod
    def get_by_id(cls, product_id):
        return session.query(cls).filter_by(id=product_id).first()

    @classmethod
    def list_products(cls):
        return session.query(cls).all()

    def __str__(self):
        return self.name
    
    @classmethod
    def delete_product(cls,product_id):
        product=session.query(Product).filter_by(id = product_id).one()
        session.delete(product)
        session.commit()
        
    @classmethod
    def update_product(cls,product_id,name,quantity,price):
        product=session.query(Product).filter_by(id = product_id).one()
        product.name=name
        product.quantity=quantity
        product.price=price
        session.commit()

    


class Supplier(Base):
    __tablename__ = 'suppliers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    #  relationship with Product
    products = relationship('Product', back_populates='supplier')  

    @classmethod
    def create(cls, name):
        supplier = cls(name=name)
        session.add(supplier)
        session.commit()
        return supplier

    @classmethod
    def get_by_id(cls, supplier_id):
        return session.query(cls).filter_by(id=supplier_id).first()

    def __str__(self):
        return self.name
