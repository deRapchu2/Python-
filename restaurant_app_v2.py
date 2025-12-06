# Restaurant Ordering + Customer Management + Menu Management (No JSON version)

import os
import csv
from datetime import datetime
import sys

CUSTOMERS_FILE = "customers.csv"
ORDERS_FILE = "orders.csv"
MENU_FILE = "menu.csv"

def ensure_files():
    if not os.path.exists(CUSTOMERS_FILE):
        with open(CUSTOMERS_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["customer_id", "name", "phone", "address"])
    if not os.path.exists(ORDERS_FILE):
        with open(ORDERS_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["order_id", "customer_id", "items", "total", "timestamp"])
    if not os.path.exists(MENU_FILE):
        default_menu = [
            ["Nadur Yakhni", 300.0],
            ["Rogan Josh", 450.0],
            ["Yakhni", 250.0],
            ["Modur Pulao", 350.0],
            ["Seekh Kebab", 400.0],
            ["Haak Saag", 180.0],
            ["Sheer Chai", 100.0],
            ["Kahwa", 120.0],
            ["Dum Aloo", 250.0],
        ]
        with open(MENU_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["item", "price"])
            writer.writerows(default_menu)

def load_menu():
    menu = {}
    with open(MENU_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            menu[row["item"]] = float(row["price"])
    return menu

def save_menu(menu):
    with open(MENU_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["item", "price"])
        for item, price in menu.items():
            writer.writerow([item, price])

def load_customers():
    rows = []
    with open(CUSTOMERS_FILE, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows.extend(reader)
    return rows

def save_customers(customers):
    with open(CUSTOMERS_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["customer_id","name","phone","address"])
        for c in customers:
            writer.writerow([c["customer_id"], c["name"], c["phone"], c["address"]])

def load_orders():
    rows = []
    with open(ORDERS_FILE, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows.extend(reader)
    return rows

def save_orders(orders):
    with open(ORDERS_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["order_id","customer_id","items","total","timestamp"])
        for o in orders:
            writer.writerow([o["order_id"], o["customer_id"], o["items"], o["total"], o["timestamp"]])

def show_menu(menu):
    print("\n{:<5} {:<25} {:>10}".format("No.", "Item", "Price (₹)"))
    print("-"*45)
    for idx, (item, price) in enumerate(menu.items(), start=1):
        print("{:<5} {:<25} {:>10.2f}".format(idx, item, price))
    print("-"*45)

def generate_customer_id(customers):
    ids = [int(c["customer_id"]) for c in customers if c["customer_id"].isdigit()]
    return str(max(ids) + 1) if ids else "1"

def generate_order_id(orders):
    ids = [int(o["order_id"]) for o in orders if o["order_id"].isdigit()]
    return str(max(ids) + 1) if ids else "1"

def find_customer_by_id(customers, cid):
    for c in customers:
        if c["customer_id"] == cid:
            return c
    return None

def list_customers(customers):
    if not customers:
        print("No customers yet.")
        return
    print("\n{:<5} {:<15} {:<12} {:<20}".format("ID","Name","Phone","Address"))
    print("-"*55)
    for c in customers:
        print("{:<5} {:<15} {:<12} {:<20}".format(c["customer_id"], c["name"], c["phone"], c["address"]))

def add_customer(customers):
    print("\nAdd New Customer")
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    address = input("Address: ").strip()
    cid = generate_customer_id(customers)
    customers.append({"customer_id": cid, "name": name, "phone": phone, "address": address})
    save_customers(customers)
    print(f"Customer added with ID {cid}")
    return cid

def edit_customer(customers):
    cid = input("Enter Customer ID to edit: ").strip()
    c = find_customer_by_id(customers, cid)
    if not c:
        print("Customer not found.")
        return
    name = input(f'Name ({c["name"]}): ').strip() or c["name"]
    phone = input(f'Phone ({c["phone"]}): ').strip() or c["phone"]
    address = input(f'Address ({c["address"]}): ').strip() or c["address"]
    c["name"], c["phone"], c["address"] = name, phone, address
    save_customers(customers)
    print("Customer updated.")

def delete_customer(customers):
    cid = input("Enter Customer ID to delete: ").strip()
    new_list = [c for c in customers if c["customer_id"] != cid]
    if len(new_list) == len(customers):
        print("Customer not found.")
    else:
        save_customers(new_list)
        customers[:] = new_list
        print("Customer deleted.")

def customer_login_or_signup():
    customers = load_customers()
    cid = input("Enter your Customer ID (or leave blank to create new): ").strip()
    if cid:
        if find_customer_by_id(customers, cid):
            print("Login successful.")
            return cid
        else:
            print("Customer ID not found. Please create an account.")
    return add_customer(customers)

def add_item_to_cart(cart, menu):
    show_menu(menu)
    try:
        choice = int(input("Enter item number: ").strip())
        if not (1 <= choice <= len(menu)):
            print("Invalid choice.")
            return
        item_name = list(menu.keys())[choice - 1]
    except ValueError:
        print("Invalid input.")
        return

    try:
        qty = int(input("Quantity: ").strip())
    except ValueError:
        print("Invalid quantity.")
        return
    if qty <= 0:
        print("Quantity must be > 0.")
        return

    price = menu[item_name]
    for it in cart:
        if it["item"] == item_name:
            it["qty"] += qty
            return
    cart.append({"item": item_name, "qty": qty, "price": price})

def remove_item_from_cart(cart):
    if not cart:
        print("Cart empty.")
        return
    print("\nYour Cart:")
    print("{:<5} {:<25} {:>5}".format("No.", "Item", "Qty"))
    print("-"*40)
    for i, it in enumerate(cart, start=1):
        print("{:<5} {:<25} {:>5}".format(i, it['item'], it['qty']))
    print("-"*40)

    try:
        idx = int(input("Enter item number to remove: ").strip())
        if 1 <= idx <= len(cart):
            removed = cart.pop(idx - 1)
            print(f"Removed {removed['item']}.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input.")

def show_cart_and_total(cart):
    if not cart:
        print("\nCart is empty.")
        return 0
    print("\n{:<5} {:<25} {:>5} {:>10}".format("No.", "Item", "Qty", "Line Total"))
    print("-"*50)
    total = 0
    for i, it in enumerate(cart, start=1):
        line = it["qty"] * it["price"]
        total += line
        print("{:<5} {:<25} {:>5} {:>10.2f}".format(i, it["item"], it["qty"], line))
    print("-"*50)
    print("{:<5} {:<25} {:>5} {:>10.2f}".format("", "TOTAL", "", total))
    return total

def checkout(cart, cid):
    if not cart:
        print("Cart empty.")
        return
    orders = load_orders()
    total = show_cart_and_total(cart)
    confirm = input("Checkout? (y/n): ").strip().lower()
    if confirm != "y":
        return
    order_id = generate_order_id(orders)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # store items as "Item1:2; Item2:3"
    items_str = "; ".join([f"{it['item']}:{it['qty']}" for it in cart])

    order_row = {
        "order_id": order_id,
        "customer_id": cid,
        "items": items_str,
        "total": f"{total:.2f}",
        "timestamp": timestamp
    }
    orders.append(order_row)
    save_orders(orders)
    print(f"Order placed! ID: {order_id}, Time: {timestamp}")
    cart.clear()

def take_order_flow(cid):
    cart = []
    menu = load_menu()
    while True:
        print("\n1) Show Menu\n2) Add Item\n3) Remove Item\n4) Show Cart\n5) Checkout\n6) Cancel Order")
        choice = input("Select: ").strip()
        if choice=="1": show_menu(menu)
        elif choice=="2": add_item_to_cart(cart,menu)
        elif choice=="3": remove_item_from_cart(cart)
        elif choice=="4": show_cart_and_total(cart)
        elif choice=="5":
            checkout(cart,cid)
            return
        elif choice=="6": return

def manage_customers_flow():
    while True:
        customers = load_customers()
        print("\n1) List\n2) Add\n3) Edit\n4) Delete\n5) Back")
        ch=input("Select: ")
        if ch=="1": list_customers(customers)
        elif ch=="2": add_customer(customers)
        elif ch=="3": edit_customer(customers)
        elif ch=="4": delete_customer(customers)
        elif ch=="5": return

def manage_menu_flow():
    while True:
        menu = load_menu()
        print("\nMenu Management:")
        print("1) Show Menu\n2) Add Item\n3) Delete Item\n4) Change Price\n5) Back")
        ch = input("Select: ").strip()
        if ch=="1":
            show_menu(menu)
        elif ch=="2":
            name = input("New Item Name: ").strip()
            try: price = float(input("Price: ").strip())
            except: 
                print("Invalid price"); continue
            menu[name] = price
            save_menu(menu)
            print("Item added.")
        elif ch=="3":
            name = input("Item to delete: ").strip()
            if name in menu:
                del menu[name]
                save_menu(menu)
                print("Deleted.")
            else: print("Not found.")
        elif ch=="4":
            name = input("Item to change price: ").strip()
            if name in menu:
                try: price = float(input("New Price: ").strip())
                except: print("Invalid price"); continue
                menu[name] = price
                save_menu(menu)
                print("Price updated.")
            else: print("Not found.")
        elif ch=="5": return

def main_menu():
    ensure_files()
    while True:
        print("\n=== Restaurant App ===")
        print("1) Customer Login & Take Order")
        print("2) Manage Customers")
        print("3) Manage Menu")
        print("4) Exit")
        choice=input("Select: ").strip()
        if choice=="1":
            cid=customer_login_or_signup()
            take_order_flow(cid)
        elif choice=="2": manage_customers_flow()
        elif choice=="3": manage_menu_flow()
        elif choice=="4": break

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
