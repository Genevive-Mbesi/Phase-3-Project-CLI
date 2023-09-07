from inventory.models.model import Product 
from sqlalchemy.orm import Session

class ProductClassMethods:
    @classmethod
    def create_product(cls, session: Session, name: str, description: str, quantity: int, price: int, category, supplier):
        """Create a new product and add it to the inventory."""
        # Create a new product instance
        product = Product(name=name, description=description, quantity=quantity, price=price, category=category, supplier=supplier)

        # Add the product to the session and commit it to the database
        session.add(product)
        session.commit()

    @classmethod
    def update_product(cls, session: Session, product_id: int, name: str, description: str, quantity: int, price: int, category, supplier):
        """Update product details."""
        # Query the database for the product by ID
        product = session.query(Product).filter_by(id=product_id).first()

        if product:
            # Update the product details
            product.name = name
            product.description = description
            product.quantity = quantity
            product.price = price
            product.category = category
            product.supplier = supplier

            # Commit the changes to the database
            session.commit()
        else:
            print(f"Product with ID {product_id} not found in the inventory.")

