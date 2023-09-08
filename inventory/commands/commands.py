import click
from models.model import Product  
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

@click.group()
def cli():
    pass

@cli.command()
def list_products():
    """List all products in the inventory."""
    # Create an SQLAlchemy engine and session
    engine = create_engine('sqlite:///inventory.db') 
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database to retrieve all products
    products = session.query(Product).all()

    # Display the products
    if products:
        click.echo("List of Products:")
        for product in products:
            click.echo(f"Product ID: {product.id}")
            click.echo(f"Name: {product.name}")
            click.echo(f"Description: {product.description}")
            click.echo(f"Quantity: {product.quantity}")
            click.echo(f"Price: ${product.price}")
            click.echo(f"Category: {product.category.name}")  
            click.echo(f"Supplier: {product.supplier.name}")  
            click.echo("\n")
    else:
        click.echo("No products found in the inventory.")

    session.close()

@cli.command()
@click.argument('name')
@click.argument('description')
@click.argument('quantity', type=int)
@click.argument('price', type=int)
@click.option('--category', help='Product category')
@click.option('--supplier', help='Product supplier')
def add_product(name, description, quantity, price, category, supplier):
    """Add a new product to the inventory."""
    # Create an SQLAlchemy engine and session
    engine = create_engine('sqlite:///inventory.db') 
    Session = sessionmaker(bind=engine)
    session = Session()

    
    session.close()

