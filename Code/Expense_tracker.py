# Import the random module for generating random values
import random

# Import the datetime module for working with dates and times
from datetime import datetime

# Import the tabulate module for formatting data into a table
from tabulate import tabulate

class ExpenseTracker:
    def __init__(self):
        # Initialize expense categories and generate initial expenses
        self.expense_categories = ["Groceries", "Entertainment", "Utilities", "Transportation", "Dining"]
        self.expenses = self.generate_expense_records(self.expense_categories)

    def generate_realistic_name(self):
        # Generate a realistic name for an expense by combining adjectives and nouns
        adjectives = ["Grocery", "Entertainment", "Utility", "Transportation", "Dining"]
        nouns = ["Shopping", "Rent", "Gas", "Dinner", "Subscription"]
        return f"{random.choice(adjectives)} {random.choice(nouns)}"

    def generate_random_amount(self):
        # Generate a random amount for an expense
        return round(random.uniform(10.0, 100.0), 2)

    def generate_random_date(self):
        # Generate a random date within the year 2022 for an expense
        start_date = datetime(2022, 1, 1)
        end_date = datetime(2022, 12, 31)
        random_date = start_date + (end_date - start_date) * random.random()
        return random_date.strftime("%Y-%m-%d")

    def generate_random_payment_method(self):
        # Generate a random payment method for an expense
        payment_methods = ["Cash", "Credit Card", "Debit Card"]
        return random.choice(payment_methods)

    def generate_expense_records(self, categories):
        # Generate a list of realistic expense records with random details
        records = []
        for _ in range(20):
            expense = {
                'name': self.generate_realistic_name(),
                'amount': self.generate_random_amount(),
                'category': random.choice(categories),
                'date': self.generate_random_date(),
                'payment_method': self.generate_random_payment_method()
            }
            records.append(expense)
        return records

    def display_expense_info(self, expense):
        # Display details of a single expense
        print(f"Name: {expense['name']}")
        print(f"Amount: ${expense['amount']}")
        print(f"Category: {expense['category']}")
        print(f"Date: {expense['date']}")
        print(f"Payment Method: {expense['payment_method']}")
        print("\n" + "="*30 + "\n")

    def display_all_expenses(self, expenses=None):
        # Display details of all expenses (default to the instance's expenses)
        if expenses is None:
            expenses = self.expenses
        for expense in expenses:
            self.display_expense_info(expense)

    def display_all_expenses_table(self, expenses=None):
        # Display expenses in tabular format
        if expenses is None:
            expenses = self.expenses
        table_data = []
        for i, expense in enumerate(expenses, start=1):
            table_data.append([i, expense['name'], f"${expense['amount']:.2f}", expense['category'], expense['date'], expense['payment_method']])
        print(f"\nNumber of Expenses: {len(expenses)}\n")
        if expenses:
            # Use tabulate to format the table and print it
            print(tabulate(table_data, headers=["#", "Name", "Amount", "Category", "Date", "Payment Method"], tablefmt="fancy_grid"))
        else:
            print("No expenses found for the selected category.")
        print("\n" + "="*80 + "\n")

    def display_all_categories(self):
        # Display all expense categories
        print("All Expense Categories:", ', '.join(self.expense_categories))
        print("="*30)

    def filter_expenses_by_category(self, category):
        # Filter expenses based on a given category
        filtered_expenses = [expense for expense in self.expenses if expense['category'] == category]
        return filtered_expenses

    def calculate_total_expenses(self):
        # Calculate the total amount of all expenses
        return sum(expense['amount'] for expense in self.expenses)

    def calculate_expenses_by_category(self):
        # Calculate total expenses for each category
        category_totals = {}
        for category in self.expense_categories:
            category_expenses = [expense['amount'] for expense in self.expenses if expense['category'] == category]
            category_totals[category] = sum(category_expenses)
        return category_totals

    def add_user_expense(self):
        # Allow the user to input a new expense
        name = input("Enter expense name: ")
        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category: ")
        while category not in self.expense_categories:
            print(f"Invalid category. Available categories: {', '.join(self.expense_categories)}")
            category = input("Enter expense category: ")
        date = input("Enter expense date (YYYY-MM-DD): ")
        payment_method = input("Enter payment method: ")

        new_expense = {
            'name': name,
            'amount': amount,
            'category': category,
            'date': date,
            'payment_method': payment_method
        }

        self.expenses.append(new_expense)

    def delete_expense(self, expense):
        # Delete a specified expense from the list
        self.expenses.remove(expense)

    def update_category_in_expenses(self, old_category, new_category):
        # Update the category in all expenses when a category is edited
        for expense in self.expenses:
            if expense['category'] == old_category:
                expense['category'] = new_category

    def manage_categories(self):
        # Allow the user to manage expense categories
        while True:
            print("\nExpense Categories Management:")
            self.display_all_categories()
            print("1. Add Category")
            print("2. Edit Category")
            print("3. Delete Category")
            print("4. Return to Main Menu")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                new_category = input("Enter new category: ")
                self.expense_categories.append(new_category)
                print(f"Category '{new_category}' added successfully.")
            elif choice == "2":
                print("Current Categories:", self.expense_categories)
                old_category = input("Enter category to edit: ")
                if old_category in self.expense_categories:
                    index = self.expense_categories.index(old_category)
                    new_category = input("Enter new category: ")
                    self.expense_categories[index] = new_category
                    self.update_category_in_expenses(old_category, new_category)
                    print(f"Category '{old_category}' edited to '{new_category}' successfully.")
                else:
                    print("Invalid category.")
            elif choice == "3":
                print("Current Categories:", self.expense_categories)
                category_to_delete = input("Enter category to delete: ")
                if category_to_delete in self.expense_categories:
                    # Warning prompt before deleting a category
                    confirm_delete = input(f"Are you sure you want to delete '{category_to_delete}'? (y/n): ")
                    if confirm_delete.lower() == 'y':
                        # Delete category and associated expenses
                        self.expense_categories.remove(category_to_delete)
                        self.expenses = [expense for expense in self.expenses if expense['category'] != category_to_delete]
                        print(f"Category '{category_to_delete}' deleted successfully.")
                else:
                    print("Invalid category.")
            elif choice == "4":
                print("Returning to Main Menu.")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 4.")

    def delete_expense_menu(self):
        # Allow the user to select and delete an expense
        print("\nDelete Expense Menu:")
        self.display_all_expenses_table()
        print("Select an expense to delete:")

        try:
            choice = int(input("Enter the number of the expense to delete (0 to cancel): ")) - 1
            if 0 <= choice < len(self.expenses):
                # Warning prompt before deleting an expense
                confirm_delete = input(f"Are you sure you want to delete '{self.expenses[choice]['name']}'? (y/n): ")
                if confirm_delete.lower() == 'y':
                    deleted_expense = self.expenses[choice]
                    self.delete_expense(deleted_expense)
                    print(f"Expense '{deleted_expense['name']}' deleted successfully.")
            elif choice == -1:
                print("Cancelled deletion.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def calculate_expenses_by_category_menu(self):
        # Calculate and display expenses by category
        print("\nCalculate Expenses by Category:")
        category_totals = self.calculate_expenses_by_category()
        if category_totals:
            print("Total Expenses by Category:")
            for category, total in category_totals.items():
                print(f"{category}: ${total:.2f}")
        else:
            print("No expenses found.")
        print("\n" + "="*80 + "\n")

    def main_menu(self):
        # Main menu for user interaction
        while True:
            print("\nExpense Tracker Menu:")
            self.display_all_categories()
            print("1. Add Expense")
            print("2. Manage Expense Categories")
            print("3. Display All Expenses")
            print("4. Filter Expenses by Category")
            print("5. Calculate Total Expenses")
            print("6. Calculate Expenses by Category")
            print("7. Delete Expense")
            print("8. Exit")

            choice = input("Enter your choice (1-8): ")

            if choice == "1":
                self.add_user_expense()
            elif choice == "2":
                self.manage_categories()
            elif choice == "3":
                self.display_all_expenses_table()
            elif choice == "4":
                self.display_all_categories()
                chosen_category = input("Enter a category to filter expenses: ")
                filtered_expenses = self.filter_expenses_by_category(chosen_category)
                print(f"\nExpenses in Category '{chosen_category}':")
                self.display_all_expenses_table(filtered_expenses)
            elif choice == "5":
                total_expenses = self.calculate_total_expenses()
                print(f"Total Expenses: ${total_expenses:.2f}")
            elif choice == "6":
                self.calculate_expenses_by_category_menu()
            elif choice == "7":
                self.delete_expense_menu()
            elif choice == "8":
                print("Exiting. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 8.")

if __name__ == "__main__":
    # Create an instance of the ExpenseTracker class and start the main menu
    expense_tracker = ExpenseTracker()
    expense_tracker.main_menu()
