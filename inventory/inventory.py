# inventory.py

from utils import read_file, write_file

PRODUCT_FILE = "inventory/data/products.csv"


def load_products():
    """
    Loads all products from products.csv
    Converts each row into a dictionary
    Returns a list of product dictionaries
    """
    file_content = read_file(PRODUCT_FILE)

    # Skip the header row
    file_data = file_content[1:]

    products = []

    for item in file_data:
        parts = item.strip().split(',')

        product = {
            "product_id": parts[0],
            "product_name": parts[1],
            "product_price": parts[2],
            "product_quantity": parts[3]
        }

        products.append(product)

    return products


def update_stock(product_id, quantity_sold):
    """
    Reduces stock for a given product_id
    Assumes validation has already happened
    Writes updated inventory back to CSV
    """

    products = load_products()

    # Find the product and reduce its quantity
    for product in products:
        if product['product_id'] == str(product_id):
            current_stock = int(product["product_quantity"])
            product['product_quantity'] = str(current_stock - quantity_sold)

    # Rebuild CSV content
    lines = ["product_id,name,price,stock\n"]

    for product in products:
        line = (
            product["product_id"] + "," +
            product["product_name"] + "," +
            product["product_price"] + "," +
            product["product_quantity"] + "\n"
        )
        lines.append(line)

    write_file(PRODUCT_FILE, lines)
