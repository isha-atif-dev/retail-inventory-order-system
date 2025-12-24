from utils import read_file

PRODUCT_FILE = "inventory/data/products.csv"

def load_products():
    file_content = read_file(PRODUCT_FILE)
    file_data = file_content[1:]
    products = []
    for item in file_data:
        parts = item.strip().split(',')
        product = {
            "product_id" : parts[0],
            "product_name" : parts[1],
            "product_price" : parts[2],
            "product_quantity" : parts[3]
        }
        products.append(product)
    return products

print(load_products())