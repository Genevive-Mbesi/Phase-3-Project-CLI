from sqlalchemy.orm import Session
import os
import sys

# Append the parent directory to the sys path to enable relative imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Import the Supplier class from module
from model import Supplier

class SupplierClassMethods:
    @classmethod
    def create_supplier(cls, session: Session, name: str):
        """Create a new supplier and add it to the inventory."""
        # Create a new supplier instance 
        supplier = Supplier(name=name)

        # Add the supplier to the session and commit it to the database
        session.add(supplier)
        session.commit()

    @classmethod
    def update_supplier(cls, session: Session, supplier_id: int, name: str):
        """Update supplier details."""
        # Query the database for the supplier by ID
        supplier = session.query(Supplier).filter_by(id=supplier_id).first()

        if supplier:
            # Update the supplier details
            supplier.name = name

            # Commit the changes to the database
            session.commit()
        else:
            print(f"Supplier with ID {supplier_id} not found in the inventory.")

# create a Supplier instance and call the create_supplier method
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    Project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    # Define your database connection URL
    db_url = "sqlite:///inventory.db"

    db_file = os.path.join(Project_dir, 'models', 'inventory.db')
    engine = create_engine(f'sqlite:///{db_file}')

    # Create a SQLAlchemy engine and session
    engine = create_engine('sqlite:///inventory.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a SupplierClassMethods instance
    supplier_methods = SupplierClassMethods()

    # Create a new supplier
    supplier_name = "Genevive"
    supplier_methods.create_supplier(session, supplier_name)

