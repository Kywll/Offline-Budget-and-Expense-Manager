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
    print("Choose an action")
    print("1.View Summary")
    print("2.Manage Expenses")
    print("3.Manage Income")
    print("4.Transaction & Reports")
    print("5.Analytics & Insights")
    print("6.Settings & Utilities")
    print("0.Exit")



cli()


manager = Manager()
