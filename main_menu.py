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

def cli():
    while True:
        cli()
        print("\n=== MAIN MENU ===")
        print("1. View Summary")
        print("2. Manage Expenses")
        print("3. Manage Income")
        print("4. Transactions & Reports")
        print("5. Analytics & Insights")
        print("6. Settings & Utilities")
        print("0. Exit")

        choice = input("Choose an action: ")
        
        if choice == "1":
            print("Viewing summary...")
        elif choice == "2":
            print("Managing expenses...")
        elif choice == "3":
            print("Managing income...")
        elif choice == "4":
            print("Transaction & reports...")
        elif choice == "5":
            print("Analytics & insights...")
        elif choice == "6":
            print("Settings...")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


cli()


manager = Manager()
