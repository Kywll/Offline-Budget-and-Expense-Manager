'''
Features:
Budget Tracker, Pending expenses, expense priorities, savings recommended, savings goal, 
transactions, search_sort, summary, reports, cli, utils(helper module), Analytics 

'''

from profile import Profile
from manager import Manager
import json

profile = Profile()

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


def expenses_menu(profile):
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
            manager.add_expense()
        elif choice == "2":
            print("Listing expenses...")
            profile.show_expenses()
        elif choice == "3":
            print("Editing expense...")
        elif choice == "4":
            print("Deleting expense...")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")

def income_menu(profile):
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
            manager.add_income()
        elif choice == "2":
            print("Viewing income records...")
            profile.show_income()
        elif choice == "3":
            print("Editing income...")
        elif choice == "4":
            print("Deleting income...")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")
            

def transaction_menu(profile):
    while True:
        print("\n=== TRANSACTIONS & REPORTS MENU ===")
        print("1. View All Transactions")
        profile.show_transactions()
        print("2. Filter Transactions (by date/category/type)")
        print("3. Monthly Report")
        print("4. Annual Report")
        print("5. Export Report")
        print("0. Back to Main Menu")

        choice = input("Choose an action: ").strip()

        if choice == "1":
            print("Showing all transactions...")
            profile.show_transactions()
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

def analytics_menu(profile):
    while True:
        print("\n=== ANALYTICS & INSIGHTS MENU ===")
        print("1. Expense Breakdown (by category)")
        print("2. Income vs Expense Comparison")
        print("3. Monthly Trends")
        print("4. Highest/Lowest Spending")
        print("5. Savings Insights")
        print("0. Back to Main Menu")

        choice = input("Choose an action: ").strip()

        if choice == "1":
            print("Showing expense breakdown by category...")
        elif choice == "2":
            print("Comparing income vs expenses...")
        elif choice == "3":
            print("Generating monthly trends...")
        elif choice == "4":
            print("Analyzing highest/lowest spending...")
        elif choice == "5":
            print("Showing savings insights...")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")

def view_summary(profile):
    print("\n=== SUMMARY OVERVIEW ===")

    profile.show_details()
    profile.show_transactions()
    profile.show_income()
    profile.show_expenses()
 
    #savings = total_income - total_expenses

    input("\nPress Enter to return to the main menu...")

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
