import json
import datetime
from profile import Profile
from utils import Util

class Manager():
    profile = Profile()
    util = Util()
    current_time = datetime.datetime.now()

    def collect_income(self, income, current_time, profile):
        for i in range(len(income)):
            if income[i]["expected_date"] > current_time and income[i]["collected"] == False:
                profile.budget += income[i]["amount"]
                income[i]["collected"] = True

    def update_savings(self, profile, amount):
        profile.savings = amount

    def pay_expense(self, expense, profile):
        if expense["paid"] == False:
            expense["paid"] = True
            profile.budget -= expense["price"]

    def record_transaction(self, data, transactions):
        
        transactions["data"] = data

    def add_expense(self, name, price, deadline, priority, frequency, is_paid=False):
        most_id = self.util.most(self.profile.expenses, "id")
        self.profile.expenses.append({ 
            "id": most_id["id"] +1,
            "name": name,
            "date": self.current_time,
            "price": price,
            "deadline": deadline,
            "priority": priority,
            "paid": is_paid,
            "frequency": frequency
        })

    def add_income(self, amount):
        most_id = self.util.most(self.profile.income, "id")
        self.profile.income.append({
            "id": most_id["id"] +1, 
            "expected_date": self.current_time, 
            "amount": amount, 
            "collected": False
        })
    
    def delete_income(self, object, data, target):
        self.util.delete(object, data, target)


    def priorty_expense(self):
        pass
    def recommended_savings(self):
        pass
    def recommended_action(self):
        pass









