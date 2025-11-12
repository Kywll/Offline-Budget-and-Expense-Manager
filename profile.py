

import json

class Profile:
    with open("profile.json", "r") as f:
        profile_data = json.load(f)
    with open("transactions.json", "r") as g:
        transactions_data = json.load(g)
    with open("income.json", "r") as h:
        income_data = json.load(h)
    with open("expenses.json", "r") as j:
        expense_data = json.load(j)

    budget = profile_data["profile"]["budget"]
    savings = profile_data["profile"]["savings"]
    goal = profile_data["profile"]["goal"]

    transactions = transactions_data["transactions"]
    expenses = expense_data["expenses"]
    income = income_data["income"]


    def show_details(self):
        print("Budget: ", self.budget)
        print("Savings: ", self.savings)
        print("Goal: ", self.goal)

    def show_transactions(self):
        print("Transactions: ", self.transactions)

    
    def show_income(self):
        result = 0
        for i in range(self.income):
            result += self.income[i]
        print("Expected Income: ", result)

    
    def show_expenses(self):
        print("Expenses", self.expenses)

