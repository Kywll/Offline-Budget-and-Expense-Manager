import json

class Profile:
    def __init__(self):
        
        with open("profile.json", "r") as f:
            profile_data = json.load(f)
        with open("transactions.json", "r") as g:
            transactions_data = json.load(g)
        with open("income.json", "r") as h:
            income_data = json.load(h)
        with open("expenses.json", "r") as j:
            expense_data = json.load(j)
        with open("logs.json", "r") as k:
            logs_data = json.load(k)

        self.budget = profile_data["profile"]["budget"]
        self.savings = profile_data["profile"]["savings"]
        self.goal = profile_data["profile"]["goal"]

        self.profile = profile_data["profile"]
        self.transactions = transactions_data["transactions"]
        self.expenses = expense_data["expenses"]
        self.income = income_data["income"]
        self.logs = logs_data["logs"]

    def show_details(self):
        print("Budget: ", self.budget)
        print("Savings: ", self.savings)
        print("Goal: ", self.goal)

    def show_transactions(self):
        print("Transactions: ", self.transactions)

    def show_income(self):
        result = 0
        for i in range(len(self.income)):
            if self.income[i]["collected"] == False:
                result += self.income[i]["amount"]
        print("Expected Income: ", result)
    
    def show_expenses(self):
        print("Expenses", self.expenses)

    def show_total_expenses(self):
        result = 0
        for i in range(len(self.expenses)):
            result += self.expenses[i]["price"]
        print("Total Expenses: ", result)
    
    def show_logs(self):
        print("Logs: ", self.logs)
