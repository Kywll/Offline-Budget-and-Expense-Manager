

import json

class Profile:
    with open("profile.json", "r") as f:
        new_data = json.load(f)
    budget = new_data["profile"]["budget"]
    income = new_data["profile"]["income"]
    savings = new_data["profile"]["savings"]
    expenses = new_data["profile"]["expenses"]
    goal = new_data["profile"]["goal"]

    def show_details(self):
        print("Budget: ", self.budget)
        print("Income: ", self.income)
        print("Savings: ", self.savings)
        print("Expenses: ", self.expenses)
        print("Goal: ", self.goal)

