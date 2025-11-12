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
    print("Choose the number of the action you want to take")
    print("1.Show Transactions")
    print("2.Show Expenses")
    print("3.Show Full Income")
    print("4.Insert Expense")
    print("5.Insert Income")
    print("6. ")
    print("0.Exit")



cli()


manager = Manager()
