import click
from inventory.models.model import Category, Product, Supplier, engine, session


@click.group()
def cli():
    pass


@cli.command()
@click.option('--name', prompt='Category Name', help='Name of the category')
def create_category(name):
    category = Category.create(name)
    click.echo(f"Category '{category.name}' created with ID: {category.id}")

@cli.command()
@click.option('--name', prompt='Supplier Name', help='Name of the supplier')
def create_supplier(name):
    supplier = Supplier.create(name)
    click.echo(f"Supplier '{supplier.name}' created with ID: {supplier.id}")



@cli.command()
@click.option('--name', prompt='Product Name', help='Name of the product')
@click.option('--description', prompt='Product Description', help='Description of the product')
@click.option('--quantity', prompt='Quantity', default=0, type=int, help='Quantity of the product')
@click.option('--price', prompt='Price', type=int, help='Price of the product')
@click.option('--category_id', prompt='Category ID', type=int, help='ID of the category')
@click.option('--supplier_id', prompt='Supplier ID', type=int, help='ID of the supplier')
def create_product(name, description, quantity, price, category_id, supplier_id):
    category = Category.get_by_id(category_id)
    supplier = Supplier.get_by_id(supplier_id)
    product = Product.create(name, description, quantity, price, category, supplier)
    click.echo(f"Product '{product.name}' created with ID: {product.id}")

@cli.command()
@click.option('--product_id', prompt='Product id',type=int, help='Name of the product id')
def delete_product(product_id):
    Product.delete_product(product_id)

@cli.command()
@click.option('--product_id', prompt='Product id',type=int, help='Name of the product id')
@click.option('--name', prompt='Product Name', help='Name of the product')
@click.option('--quantity', prompt='Quantity', default=0, type=int, help='Quantity of the product')
@click.option('--price', prompt='Price', type=int, help='Price of the product')
def update_product(product_id,name,quantity,price):
    Product.update_product(product_id,name,quantity,price) 

@cli.command()
def list_categories():
    print("Inside list_categories function")  
    categories = Category.list_categories()
    click.echo("Categories:")
    for category in categories:
        click.echo(f"ID: {category.id}, Name: {category.name}")


@cli.command()
def list_products():
    products = Product.list_products()
    click.echo("Products:")
    for product in products:
        click.echo(f"ID: {product.id}, Name: {product.name}, Price: {product.price}")


if __name__ == '__main__':
    cli()
