'''
Features:
Budget Tracker, Pending expenses, expense priorities, savings recommended, savings goal, 
transactions, search_sort, summary, reports, cli, utils(helper module), Analytics 

'''

from profile import Profile
from manager import Manager

profile = Profile()
manager = Manager()



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
            name = input("Enter Expense Name: ").strip()
            price = input("Enter Expense Price: ").strip()
            deadline = input("Enter Expense Date: ").strip()
            priority = input("Enter Expense Priority: ").strip()
            frequency = input("Enter Expense Frequency: ").strip()

            manager.add_expense(name, price, deadline, priority, frequency)

        elif choice == "2":
            print("Listing expenses...")
            profile.show_expenses()
        elif choice == "3":
            print("Editing expense...")
            data = input("Enter Expense Data to Change: ").strip()
            new_data = input("Enter New Expense Data to Insert: ").strip()
            target = input("Enter Data Target of the expense that will be updated: ").strip()
            
            manager.util.update(profile.expenses, data, new_data, target)
        elif choice == "4":
            print("Deleting expense...")
            data = input("Enter Expense Data to Delete: ").strip()
            target = input("Enter Data Target of the expense that will be deleted: ").strip()

            manager.util.delete(profile.expenses, data, target)
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

            name = input("Enter Income Name: ").strip()
            amount = int(input("Enter Income Amount: ").strip())

            manager.add_income(amount, name)
        elif choice == "2":
            print("Viewing income records...")
            profile.show_income()
        elif choice == "3":
            print("Editing income...")

            data = input("Enter Income Data to Change: ").strip()
            new_data = input("Enter New Income Data to Insert: ").strip()
            target = input("Enter Data Target of the Income that will be updated: ").strip()
            
            manager.util.update(profile.income, data, new_data, target)
        elif choice == "4":
            print("Deleting income...")

            data = input("Enter Income Data to Delete: ").strip()
            target = input("Enter Data Target of the Income that will be deleted: ").strip()

            manager.util.delete(profile.income, data, target)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")
            

def transaction_menu(profile):
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
            profile.show_transactions()

            print("Adding expense...")
            name = input("Enter Expense Name: ").strip()
            price = input("Enter Expense Price: ").strip()
            deadline = input("Enter Expense Date: ").strip()
            priority = input("Enter Expense Priority: ").strip()
            frequency = input("Enter Expense Frequency: ").strip()

            manager.add_expense(name, price, deadline, priority, frequency)


        elif choice == "2":
            manager.util.filter()
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
        
        if choice == "1":
            view_summary(profile)
        elif choice == "2":
            expenses_menu(profile)
        elif choice == "3":
            income_menu(profile)
        elif choice == "4":
            transaction_menu(profile)
        elif choice == "5":
            analytics_menu(profile)
        elif choice == "6":
            settings_menu(profile)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
        

main_menu()


manager = Manager()
