import csv
from datetime import datetime

# File to store expenses
FILE_NAME = "expenses.csv"


# Function to add an expense
def add_expense():
    amount = float(input("Enter the amount: $"))
    category = input("Enter the category (e.g., Food, Rent, Entertainment): ")
    date = input("Enter the date (YYYY-MM-DD) or press Enter for today: ")
    date = date if date else datetime.now().strftime('%Y-%m-%d')

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category])

    print("Expense added successfully!")


# Function to view a summary of expenses
def view_summary():
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            expenses = list(reader)
            if not expenses:
                print("No expenses recorded yet!")
                return

            print("\nExpenses:")
            total = 0
            for row in expenses:
                print(f"Date: {row[0]}, Amount: ${row[1]}, Category: {row[2]}")
                total += float(row[1])
            print(f"\nTotal Expense: ${total:.2f}")
    except FileNotFoundError:
        print("No expenses recorded yet!")


# Function to check if spending is within budget
def check_budget():
    budget = float(input("Enter your budget: $"))
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            total = sum(float(row[1]) for row in reader)
            if total > budget:
                print(f"You've exceeded your budget by ${total - budget:.2f}")
            else:
                print(f"You are within budget. Remaining: ${budget - total:.2f}")
    except FileNotFoundError:
        print("No expenses recorded yet!")


# Main program
def main():
    print("Welcome to Personal Expense Tracker!")
    while True:
        print("\nMenu:")
        print("1. Add an Expense")
        print("2. View Summary")
        print("3. Check Budget")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            check_budget()
        elif choice == "4":
            print("Thank you for using the Personal Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")


# Run the main program
if __name__ == "__main__":
    main()

