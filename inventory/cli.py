import click
from inventory.models.model import Product

@click.group()
def cli():
    pass

@cli.command()
def add_product():
    session = Session()

    name = click.prompt('Enter the product name')
    description = click.prompt('Enter the product description')
    quantity = click.prompt('Enter the product quantity', type=int)
    price = click.prompt('Enter the product price', type=int)
    category_id = click.prompt('Enter the product category ID', type=int)

    ProductClassMethods.create_product(session, name, description, quantity, price, category_id)
    
    session.close()

if __name__ == '__main__':
    cli()

