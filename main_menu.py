from profile import Profile
from manager import Manager

profile = Profile()
manager = Manager(profile)

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
            name = input("Enter Expense Name: ").strip()
            price = float(input("Enter Expense Price: "))
            deadline = input("Enter Expense Date: ").strip()
            
            print("Adding expense...")
            manager.add_expense(name, price, deadline)

        elif choice == "2":
            print("Listing expenses...")
            profile.show_expenses()
        elif choice == "3":
            
            print(profile.expenses)
            id = int(input("Enter Expense ID to Change: "))
            data = input("Enter Expense Data to Change: ").strip()
            new_data = input("Enter New Expense Data to Insert: ").strip()
            
            print("Editing expense...")
            manager.util.update(profile.expenses, "expenses.json", "expenses", data, new_data, id)

            print(manager.util.search(profile.expenses, "id", id))

            action = f"Edited expenses with id {id}. Changed {data} value into {new_data}."
            manager.record_log(action)

        elif choice == "4":

            print(profile.expenses)
            id = int(input("Enter Expense ID to Delete: "))

            print("Deleting expense...")
            manager.util.delete(profile.expenses, "expenses.json", "expenses", id)

            print(manager.util.search(profile.expenses, "id", id))

            action = f"Deleted expenses with id {id}."
            manager.record_log(action)

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

            name = input("Enter Income Name: ").strip()
            amount = float(input("Enter Income Amount: "))

            print("Adding income...")
            manager.add_income(amount, name)
        elif choice == "2":
            print("Viewing income records...")
            profile.show_income()
        elif choice == "3":
            print(profile.income)
            id = int(input("Enter Income ID to Change: "))
            data = input("Enter Income Data to Change: ").strip()
            new_data = input("Enter New Income Data to Insert: ").strip()
            
            manager.util.update(profile.income, "income.json", "income", data, new_data, id)

            print("Editing income...")

            print(manager.util.search(profile.income, "id", id))

            action = f"Edited income with id {id}. Changed {data} value into {new_data}."
            manager.record_log(action)
        elif choice == "4":
            print(profile.income)
            id = int(input("Enter Income ID to Delete: "))
            manager.util.delete(profile.income, "income.json", "income", id)

            print("Deleting income...")
            print(manager.util.search(profile.income, "id", id))

            action = f"Deleted expincome with id {id}."
            manager.record_log(action)
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

def view_logs(profile):
    print("\n=== LOGS OVERVIEW ===")

    profile.show_logs()

    input("\nPress Enter to return to the main menu...")

def main_menu():
    while True:
        manager.collect_income()
        manager.pay_expense()

        print("\n=== MAIN MENU ===")
        print("1. View Summary")
        print("2. Manage Expenses")
        print("3. Manage Income")
        print("4. View Logs")
        print("0. Exit")

        choice = input("Choose an action: ").strip()
        
        if choice == "1":
            view_summary(profile)
        elif choice == "2":
            expenses_menu(profile)
        elif choice == "3":
            income_menu(profile)
        elif choice == "4":
            view_logs(profile)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
        

main_menu()

