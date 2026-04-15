# 🛒 Retail Inventory & Order Management System

> Backend-focused Python system that simulates real retail logic — stock validation, inventory updates, and persistent order history logging using CSV-based storage.

![Python](https://img.shields.io/badge/python-3.x-blue)
![Storage](https://img.shields.io/badge/storage-CSV-green)
![Type](https://img.shields.io/badge/type-portfolio%20project-orange)

---

## Overview

This project simulates how real retail systems handle product stock, order validation, and order history logging using file-based persistent storage. It ensures that:

- Orders are only completed when sufficient stock exists
- Inventory is updated reliably after each transaction
- All order attempts — successful or rejected — are permanently recorded

---

## Key Features

- Load and manage product inventory from CSV files
- Validate orders against available stock
- Automatically update inventory for completed orders
- Persist full order history (COMPLETED and REJECTED)
- Generate unique order IDs
- Clear separation of concerns across modules

---

## Repository Structure
retail-inventory-order-system/
│
├── main.py                  # Application entry point
│
├── inventory/
│   ├── inventory.py         # Load & update stock
│   ├── orders.py            # Order validation & logging
│   ├── utils.py             # File handling utilities
│   └── data/
│       ├── products.csv     # Product inventory
│       └── orders.csv       # Order history log
│
└── README.md

---

## System Flow

1. User enters a product ID and quantity
2. System checks product existence and stock availability
3. **If valid** → stock is reduced, order saved as `COMPLETED`
4. **If invalid** → inventory unchanged, order saved as `REJECTED`
5. All attempts permanently recorded in `orders.csv`

---

## Example Data

**products.csv**
```csv
product_id,name,price,stock
101,Milk,1.50,50
102,Bread,1.00,30
103,Eggs,2.20,20
```

**orders.csv**
```csv
order_id,product_id,quantity,status
5001,101,2,COMPLETED
5002,103,25,REJECTED
```

---

## How to Run

```bash
# 1. Clone the repository
git clone https://github.com/isha-atif-dev/retail-inventory-order-system.git

# 2. Navigate into the project folder
cd retail-inventory-order-system

# 3. Run the application
python main.py
```

Follow the prompts to place an order.

---

## Error Handling & Edge Cases

| Scenario | Behaviour |
|---|---|
| Invalid product ID | Safely rejected |
| Order exceeds stock | Rejected, inventory unchanged |
| Rejected orders | Still logged for audit |
| All transactions | Inventory consistency preserved |

---

## Concepts Demonstrated

`Backend logic design` · `Separation of concerns` · `File-based persistence` · `Defensive programming` · `Retail system workflows`

---

## Possible Enhancements

- Replace CSV storage with a database (SQLite or PostgreSQL)
- Add REST API endpoints
- Implement user authentication
- Introduce automated tests
- Add comprehensive input validation and exception handling

---

## Author

**Isha Atif**  
MRes Applied Artificial Intelligence · University of Bolton (UoGM)