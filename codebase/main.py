import csv
import os

FILE = "medicines.csv"


# Load medicines
def load():
    medicines = []

    if os.path.exists(FILE):
        with open(FILE, "r", newline="") as f:
            reader = csv.DictReader(f)

            for row in reader:
                medicines.append(row)

    return medicines


# Save medicines
def save(medicines):
    with open(FILE, "w", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=["ID", "Name", "Quantity", "Price"]
        )

        writer.writeheader()
        writer.writerows(medicines)


# Add medicine
def add():
    medicines = load()

    name = input("Enter medicine name: ")

    try:
        qty = int(input("Enter quantity: "))
        price = float(input("Enter price: "))

        if qty < 0 or price < 0:
            print("Negative values are not allowed!")
            return

        if qty == 0:
            print("Quantity must be greater than 0!")
            return

    except ValueError:
        print("Invalid input!")
        return

    number = 0

    for m in medicines:
        n = int(m["ID"][1:])
        if n > number:
            number = n

    med_id = "M" + str(number + 1)

    medicine = {
        "ID": med_id,
        "Name": name,
        "Quantity": str(qty),
        "Price": str(price)
    }

    medicines.append(medicine)
    save(medicines)

    print("Medicine added.")
    print("ID:", med_id, "|", name,
          "| Qty:", qty, "| Price:", format(price, ".2f"))


# View medicines
def view():
    medicines = load()

    if not medicines:
        print("No medicines available!")
        return

    for m in medicines:
        print(m["ID"], m["Name"],
              "Qty:", m["Quantity"],
              "Price:", m["Price"])


# Sell medicine
def sell():
    medicines = load()

    med_id = input("Enter medicine ID: ")

    try:
        qty = int(input("Enter quantity to sell: "))

        if qty <= 0:
            print("Invalid quantity!")
            return

    except ValueError:
        print("Invalid input!")
        return

    for m in medicines:
        if m["ID"] == med_id:

            available = int(m["Quantity"])

            if qty > available:
                print("Insufficient stock. Available:", available)
                return

            bill = qty * float(m["Price"])
            available = available - qty

            m["Quantity"] = str(available)

            save(medicines)

            print("Sold", qty, "units. Bill:", format(bill, ".2f"))

            if available == 0:
                print("Stock left: 0 | Out of stock!")
            else:
                print("Stock left:", available)

            return

    print("Medicine not found!")


# Delete medicine
def delete():
    medicines = load()

    med_id = input("Enter medicine ID to delete: ")

    for m in medicines:
        if m["ID"] == med_id:
            medicines.remove(m)
            save(medicines)
            print("Medicine", med_id, "deleted.")
            return

    print("Medicine not found!")


# Low stock report
def low_stock():
    medicines = load()
    found = False

    for m in medicines:
        if int(m["Quantity"]) < 10:
            print(m["ID"], "|", m["Name"],
                  "| Qty:", m["Quantity"], "(Low stock)")
            found = True

    if not found:
        print("No low stock medicines!")


# Inventory value
def inventory_value():
    medicines = load()
    total = 0

    for m in medicines:
        total += int(m["Quantity"]) * float(m["Price"])

    print("Total inventory value:", format(total, ".2f"))


# Main menu
while True:

    print("\n===== PHARMACY INVENTORY SYSTEM =====")
    print("1. Add Medicine")
    print("2. View Stock")
    print("3. Sell Medicine")
    print("4. Delete Medicine")
    print("5. Low Stock Report")
    print("6. Inventory Value")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add()

    elif choice == "2":
        view()

    elif choice == "3":
        sell()

    elif choice == "4":
        delete()

    elif choice == "5":
        low_stock()

    elif choice == "6":
        inventory_value()

    elif choice == "7":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")