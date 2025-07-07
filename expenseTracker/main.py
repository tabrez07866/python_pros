import csv
import os
from collections import defaultdict
import matplotlib.pyplot as plt

DATA_FILE = "expenses.csv"

# Write header if file doesn't exist
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Amount", "Category", "Date"])

def add_expense(amount, category, date):
    with open(DATA_FILE, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([amount, category, date])
    print("✅ Expense added.")

def view_expenses():
    if not os.path.exists(DATA_FILE):
        print("No data found.")
        return
    with open(DATA_FILE, "r") as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        print("\n📋 Expense History:")
        for row in reader:
            print(f"💸 ₹{row[0]} - {row[1]} on {row[2]}")

def show_chart():
    category_totals = defaultdict(float)
    with open(DATA_FILE, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for amount, category, _ in reader:
            category_totals[category] += float(amount)

    if not category_totals:
        print("No data to show.")
        return

    categories = list(category_totals.keys())
    totals = list(category_totals.values())

    plt.figure(figsize=(6,6))
    plt.pie(totals, labels=categories, autopct="%1.1f%%")
    plt.title("💰 Expense Breakdown by Category")
    plt.show()

# === CLI App ===
def main():
    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. Show Chart\n4. Exit")
        choice = input("Choose: ")
        if choice == "1":
            try:
                amount = float(input("Amount (₹): "))
                category = input("Category: ").capitalize()
                date = input("Date (YYYY-MM-DD): ")
                add_expense(amount, category, date)
            except:
                print("❌ Invalid input.")
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_chart()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
