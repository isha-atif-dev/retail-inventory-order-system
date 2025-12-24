# main.py
# Entry point of the application.
# This file is responsible for taking user input and triggering the order flow.
# It does NOT contain business logic or file operations.

from orders import validate_order

def main():
    
    """
    Main function that runs when the program starts.
    It collects user input and calls the order validation logic.
    """
    try: 
        product_id = int(input("Enter Product ID:"))
        product_quantity = int(input("Enter product quantity:"))
        results = validate_order(product_id, product_quantity)

        print("Order status: ", results)
    except ValueError:
        # Handles non-numeric input
        print("Error: Please enter numeric values only.")


# This ensures that the main() function runs only
# It prevents automatic execution when imported by other files.

if __name__ == "__main__":
    main()
