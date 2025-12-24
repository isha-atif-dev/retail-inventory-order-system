🛒 Retail Inventory & Order Management System (Python)
📌 Project Overview

This project is a backend-focused retail inventory and order management system built using Python.
It simulates how real retail systems handle product stock, order validation, and order history logging using persistent storage.

The system ensures that:

Orders are only completed when sufficient stock exists
Inventory is updated reliably
All order attempts (successful or rejected) are recorded
This project was designed to reflect real-world retail backend logic, similar to systems used in large retailers.

🎯 Key Features

Load and manage product inventory from CSV files
Validate orders against available stock
Automatically update inventory for completed orders
Persist order history (COMPLETED and REJECTED orders)
Generate unique order IDs
Clear separation of concerns across modules

🗂 Project Structure
retail-inventory-order-system/
│
├── main.py                  # Application entry point
│
├── inventory/
│   ├── inventory.py         # Inventory logic (load & update stock)
│   ├── orders.py            # Order validation & order logging
│   ├── utils.py             # File handling utilities
│   └── data/
│       ├── products.csv     # Product inventory data
│       └── orders.csv       # Order history log
│
└── README.md

🔁 System Flow (How It Works)

User enters a product ID and quantity
Order is validated:
Product existence is checked
Stock availability is verified

If valid:
Inventory stock is reduced
Order is saved as COMPLETED

If invalid:
Inventory remains unchanged
Order is saved as REJECTED
Order history is permanently recorded in orders.csv

📄 Example Data
products.csv
product_id,name,price,stock
101,Milk,1.50,50
102,Bread,1.00,30
103,Eggs,2.20,20

orders.csv
order_id,product_id,quantity,status
5001,101,2,COMPLETED
5002,103,25,REJECTED

▶️ How to Run the Project
Clone the repository:

git clone https://github.com/your-username/retail-inventory-order-system.git

Navigate into the project folder:
cd retail-inventory-order-system

Run the application:
python main.py

Follow the prompts to place an order.

🛡 Error Handling & Edge Cases
❌ Invalid product IDs are safely rejected
❌ Orders exceeding available stock are rejected
✅ Rejected orders are still logged for audit and analysis
✅ Inventory consistency is preserved at all times

🧠 Key Concepts Demonstrated

Backend logic design
Separation of concerns
File-based persistence
Defensive programming
Realistic retail system workflows

🚀 Possible Enhancements

Replace CSV storage with a database (SQLite / PostgreSQL)
Add user authentication
Implement REST API endpoints
Add input validation and exception handling
Introduce automated tests

📌 Why This Project Matters

This project mirrors the core logic used in retail backend systems, making it directly relevant to software engineering and technology internships.
It demonstrates practical problem-solving, clean code structure, and real-world system thinking.

👤 Author

Isha Atif
MRes Applied Artificial Intelligence
University of Bolton (UoGM)
