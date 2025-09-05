import csv
import os
from datetime import datetime

FILENAME = 'transactions.csv'

# Initialize CSV with headers if it doesn't exist
def init_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Type', 'Category', 'Amount', 'Description'])

# Add a transaction
def add_transaction():
    t_type = input("Type (income/expense): ").strip().lower()
    if t_type not in ['income', 'expense']:
        print("Invalid type.")
        return

    category = input("Category (e.g., food, salary, rent): ").strip()
    amount = input("Amount: ").strip()
    description = input("Description: ").strip()

    try:
        amount = float(amount)
    except ValueError:
        print("Amount must be a number.")
        return

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, t_type, category, amount, description])

    print("Transaction added.")

# Show all transactions
def view_transactions():
    if not os.path.exists(FILENAME):
        print("No transactions yet.")
        return

    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(', '.join(row))

# Calculate current balance
def calculate_balance():
    income = 0
    expense = 0

    if not os.path.exists(FILENAME):
        print("No transactions to calculate.")
        return

    with open(FILENAME, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            amount = float(row['Amount'])
            if row['Type'] == 'income':
                income += amount
            elif row['Type'] == 'expense':
                expense += amount

    print(f"\nTotal Income : ₹{income}")
    print(f"Total Expense: ₹{expense}")
    print(f"Net Balance  : ₹{income - expense}\n")

# Menu
def menu():
    init_file()
    while True:
        print("\n--- Personal Finance Tracker ---")
        print("1. Add transaction")
        print("2. View transactions")
        print("3. Show balance")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            calculate_balance()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()

