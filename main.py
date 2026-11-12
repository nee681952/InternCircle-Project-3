import csv
from datetime import datetime
from collections import defaultdict

FILE = "expenses.csv"

FIELDS = ["date", "category", "description", "amount"]

# Personal Expense Tracker

# Available expense categories

categories = [
    "Food",
    "Travel",
    "Study",
    "Bills",
    "Fun"
]

print("PERSONAL EXPENSE TRACKER")

print("\nAvailable Categories:")

for category in categories:
    print("-", category)


def save_expense(row):

    try:
        open(FILE).close()

    except FileNotFoundError:
        with open(FILE, "w", newline="", encoding="utf-8") as f:
            csv.DictWriter(f, FIELDS).writeheader()

    with open(FILE, "a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, FIELDS).writerow(row)


def load_expenses():

    try:
        with open(FILE, newline="", encoding="utf-8") as f:
            return list(csv.DictReader(f))

    except FileNotFoundError:
        return []

def add_expense():

    print("\n===== ADD NEW EXPENSE =====")

    # Get expense date
    date = input("Enter date (YYYY-MM-DD): ")

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date! Please use YYYY-MM-DD.")
        return

    # Get category
    category = input("Enter category: ").strip().title()

    if category not in categories:
        print("Invalid category!")
        return

    # Get description
    description = input("Enter description: ").strip()

    # Get amount
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount! Please enter a number.")
        return

    if amount < 0:
        print("Amount cannot be negative!")
        return

    # Create expense record
    expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": str(amount)
    }

    save_expense(expense)

    print("Expense added successfully!")



def view_expenses():

    expenses = load_expenses()

    print("\n===== ALL EXPENSES =====")

    if not expenses:
        print("No expenses found!")
        return

    print("-" * 65)
    print(f"{'Date':<15}{'Category':<15}{'Description':<20}{'Amount':>10}")
    print("-" * 65)

    for expense in expenses:
        print(
            f"{expense['date']:<15}"
            f"{expense['category']:<15}"
            f"{expense['description']:<20}"
            f"{expense['amount']:>10}"
        )

    print("-" * 65)

def filter_by_category():

    expenses = load_expenses()

    category = input("Enter category to filter: ").strip().title()

    filtered = []

    for expense in expenses:
        if expense["category"] == category:
            filtered.append(expense)

    print("\n===== FILTERED EXPENSES =====")

    if not filtered:
        print("No expenses found in this category!")
        return

    for expense in filtered:
        print(expense)

def filter_by_month():

    expenses = load_expenses()

    month = input("Enter month (YYYY-MM): ").strip()

    filtered = []

    for expense in expenses:
        if expense["date"][:7] == month:
            filtered.append(expense)

    print("\n===== MONTHLY EXPENSES =====")

    if not filtered:
        print("No expenses found for this month!")
        return

    for expense in filtered:
        print(expense)

def expense_summary():

    expenses = load_expenses()

    if not expenses:
        print("No expenses available for summary!")
        return

    category_totals = defaultdict(float)

    grand_total = 0
    biggest_expense = 0
    biggest_description = ""

    for expense in expenses:

        category = expense["category"]
        amount = float(expense["amount"])

        # Calculate category total
        category_totals[category] += amount

        # Calculate grand total
        grand_total += amount

        # Find biggest expense
        if amount > biggest_expense:
            biggest_expense = amount
            biggest_description = expense["description"]

    print("\n===== EXPENSE SUMMARY =====")

    print("\nCategory-wise Spending:")

    for category, total in category_totals.items():
        print(f"{category}: ₹{total:.2f}")

    print("\nGrand Total: ₹{:.2f}".format(grand_total))

    print("Biggest Expense: ₹{:.2f}".format(biggest_expense))

    print("Description:", biggest_description)


def main():

    while True:

        print("\n===== PERSONAL EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter Expenses")
        print("4. Expense Summary")
        print("5. Quit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":

            print("\n===== FILTER EXPENSES =====")
            print("1. Filter by Category")
            print("2. Filter by Month")

            filter_choice = input("Enter your choice: ").strip()

            if filter_choice == "1":
                filter_by_category()

            elif filter_choice == "2":
                filter_by_month()

            else:
                print("Invalid filter choice!")

        elif choice == "4":
            expense_summary()

        elif choice == "5":
            print("Thank you for using Personal Expense Tracker!")
            break

        else:
            print("Invalid choice! Please select 1 to 5.")


if __name__ == "__main__":
    main()


