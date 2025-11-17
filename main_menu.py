'''
Features:
Budget Tracker, Pending expenses, expense priorities, savings recommended, savings goal, 
transactions, search_sort, summary, reports, cli, utils(helper module), Analytics 

'''

from profile import Profile
from manager import Manager
import json

profile = Profile()

profile.show_details()

def settings_menu():
    while True:
        print("\n=== SETTINGS MENU ===")
        print("1. Change Currency")
        print("2. Toggle Dark Mode")
        print("3. Reset Data")
        print("0. Back to Main Menu")

        choice = input("Choose an action: ").strip()

        if choice == "1":
            print("Changing currency...")
        elif choice == "2":
            print("Dark mode toggled!")
        elif choice == "3":
            print("Resetting data...")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")


def expenses_menu():
    while True:
        print("\n=== EXPENSES MENU ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Edit Expense")
        print("4. Delete Expense")
        print("0. Back to Main Menu")

        choice = input("Choose an action: ").strip()

        if choice == "1":
            print("Adding expense...")
        elif choice == "2":
            print("Listing expenses...")
        elif choice == "3":
            print("Editing expense...")
        elif choice == "4":
            print("Deleting expense...")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")

def income_menu():
    while True:
        print("\n=== INCOME MENU ===")
        print("1. Add Income")
        print("2. View Income Records")
        print("3. Edit Income")
        print("4. Delete Income")
        print("0. Back to Main Menu")

        choice = input("Choose an action: ").strip()

        if choice == "1":
            print("Adding income...")
        elif choice == "2":
            print("Viewing income records...")
        elif choice == "3":
            print("Editing income...")
        elif choice == "4":
            print("Deleting income...")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")

def transaction_menu():
    while True:
        print("\n=== TRANSACTIONS & REPORTS MENU ===")
        print("1. View All Transactions")
        print("2. Filter Transactions (by date/category/type)")
        print("3. Monthly Report")
        print("4. Annual Report")
        print("5. Export Report")
        print("0. Back to Main Menu")

        choice = input("Choose an action: ").strip()

        if choice == "1":
            print("Showing all transactions...")
        elif choice == "2":
            print("Filtering transactions...")
        elif choice == "3":
            print("Generating monthly report...")
        elif choice == "4":
            print("Generating annual report...")
        elif choice == "5":
            print("Exporting report...")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")


def main_menu():
    while True:
        print("\n=== MAIN MENU ===")
        print("1. View Summary")
        print("2. Manage Expenses")
        print("3. Manage Income")
        print("4. Transactions & Reports")
        print("5. Analytics & Insights")
        print("6. Settings & Utilities")
        print("0. Exit")

        choice = input("Choose an action: ").strip()
        '''
        if choice == "1":
            view_summary()
        elif choice == "2":
            expenses_menu()
        elif choice == "3":
            income_menu()
        elif choice == "4":
            transaction_menu()
        elif choice == "5":
            analytics_menu()
        elif choice == "6":
            settings_menu()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
        '''

main_menu()


manager = Manager()
