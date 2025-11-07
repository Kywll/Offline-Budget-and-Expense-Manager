'''
Features:
Budget Tracker, Pending expenses, expense priorities, savings recommended, savings goal, 
transactions, search_sort, summary, reports, cli, utils(helper module), Analytics 

'''


from profile import Profile
from manager import Manager
import json

MyProfile = Profile()

MyProfile.show_details()

manager = Manager()