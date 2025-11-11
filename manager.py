import datetime
from profile import Profile
from utils import Util

class Manager():
    profile = Profile()
    util = Util()
    current_time = datetime.datetime.now()

    def collect_income(self, profile, current_time):
        for i in range(len(profile.income)):
            if profile.income[i]["date"] > current_time and profile.income[i]["collected"] == False:
                profile.income["budget"] += profile.income[i]["amount"]
                profile.income["collected"] = True

    def insert_savings(self, profile, amount):
        profile.savings = amount

    def pay_expense(self, profile, index):
        if profile.expense[index]["paid"] == False:
            profile.expense[index]["paid"] = True
            budget -= profile.expense[index]["price"]

    def record_transaction(self, profile, data):
        pass

    def priorty_expense(self):
        pass
    def recommended_savings(self):
        pass
    def recommended_action(self):
        pass









