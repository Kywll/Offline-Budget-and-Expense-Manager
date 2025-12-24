import json
from datetime import datetime 
from utils import Util

class Manager():
    def __init__(self, profile):
            self.profile = profile
            self.util = Util()
            self.current_time = datetime.datetime.now()
           
    def collect_income(self):
        self.current_time = datetime.datetime.now()
        for i in range(len(self.profile.income)):
            expected = datetime.fromisoformat(self.profile.income[i]["expected_date"])

            if expected <= self.current_time and self.profile.income[i]["collected"] == False:
                self.profile.budget += self.profile.income[i]["amount"]
                self.profile.income[i]["collected"] = True

                action = f"Collected income id {self.profile.income[i]['id']}. Added {self.profile.income[i]['amount']} to budget."
                self.record_transaction(action)
                
                with open("profile.json", "w") as f:
                    json.dump({"profile": self.profile.profile}, f, indent=4)


    def update_savings(self, amount):
        self.profile.savings = amount

    def pay_expense(self):
        for i in range(len(self.profile.expenses)):
            if self.profile.expenses[i]["paid"] == False:
                self.profile.expenses[i]["paid"] = True
                self.profile.budget -= self.profile.expenses[i]["price"]

                with open("profile.json", "w") as f:
                    json.dump({"profile": self.profile.profile}, f, indent=4)

    def record_transaction(self, action):
        most_id = self.util.most(self.profile.transactions, "id")
        self.profile.transactions.append({
            "id": most_id["id"] +1,
            "date": str(self.current_time),
            "action": action

        })

        with open("transactions.json", "w") as f:
            json.dump({"transactions": self.profile.transactions}, f, indent=4)

    def add_expense(self, name, price, deadline, is_paid=False):
        most_id = self.util.most(self.profile.expenses, "id")
        self.profile.expenses.append({ 
            "id": most_id["id"] +1,
            "name": name,
            "date": str(self.current_time),
            "price": price,
            "deadline": deadline,
            "paid": is_paid,
        })

        with open("expenses.json", "w") as f:
            json.dump({"expenses": self.profile.expenses}, f, indent= 4)

    def add_income(self, amount, name):
        most_id = self.util.most(self.profile.income, "id")
        self.profile.income.append({
            "id": most_id["id"] +1, 
            "name": name,
            "expected_date": str(self.current_time), 
            "amount": amount, 
            "collected": False
        })

        with open("income.json", "w") as f:
            json.dump({"income": self.profile.income}, f, indent=4)
    
    def delete_income(self, object, data, target):
        self.util.delete(object, data, target)

    def record_log(self, action):
        most_id = self.util.most(self.profile.logs, "id")
        self.profile.logs.append({
            "id": most_id["id"] +1, 
            "date": str(self.current_time),
            "action": action
        })

        with open("logs.json", "w") as f:
            json.dump({"logs": self.profile.logs}, f, indent=4)







