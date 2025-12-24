from inventory import load_products, update_stock
from utils import read_file, write_file

ORDER_FILE = "inventory/data/orders.csv"


def validate_order(product_id, product_quantity):
    """
    Validates an order:
    - Checks if product exists
    - Checks stock availability
    - Updates stock if valid
    - Saves order result
    Returns COMPLETED or REJECTED
    """
    products = load_products()

    for product in products:
        # Case 1: Product exists
        if product["product_id"] == str(product_id):

            # Case 1a: Enough stock
            if int(product['product_quantity']) >= product_quantity:
                update_stock(product_id, product_quantity)
                save_order(product_id, product_quantity, "COMPLETED")
                return "Completed"

            # Case 1b: Not enough stock
            else:
                save_order(product_id, product_quantity, "REJECTED")
                return "Rejected"

    # Case 2: Product does NOT exist
    save_order(product_id, product_quantity, "REJECTED")
    return "Rejected"


def get_Order_id():
    """
    Generates the next unique order ID
    Based on the last order saved in orders.csv
    """
    lines = read_file(ORDER_FILE)

    if len(lines) == 1:
        return 5001

    last_line = lines[-1].strip().split(',')
    last_order_id = int(last_line[0])

    return last_order_id + 1


def save_order(product_id, quantity, status):
    """
    Generates the next unique order ID
    Based on the last order saved in orders.csv
    """
    lines = read_file(ORDER_FILE)

    # Ensure proper newline formatting
    if not lines[-1].endswith("\n"):
        lines[-1] += "\n"

    order_id = get_Order_id()

    new_line = f"{order_id},{product_id},{quantity},{status}\n"

    lines.append(new_line)
    write_file(ORDER_FILE, lines)
