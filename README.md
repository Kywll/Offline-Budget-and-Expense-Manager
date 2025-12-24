Personal Finance Manager

A Python-based personal finance management system that allows you to track expenses, income, and logs in a structured and automated way. The project helps you manage your budget, savings, and transactions, providing detailed summaries and transaction logs.

Features

Expense Management

Add, edit, delete, and view expenses

Track payment status (paid / unpaid)

Automatic logging of expense actions

Support for priorities and deadlines

Income Management

Add, edit, delete, and view income sources

Track collection status (collected / uncollected)

Automatically collect income when due

Logs collection events

Budget & Savings

Tracks your current budget

Update savings manually

Transaction Logging

Every income collection and expense payment is logged

Complete history of actions for auditing

Summary Overview

View detailed budget, savings, income, and expenses

See total expected income and total expenses

File-Based Persistence

Data is stored in JSON files:

profile.json, expenses.json, income.json, transactions.json, logs.json

Changes are automatically saved and loaded across sessions

Project Structure
personal-finance-manager/
│
├── main.py              # Main program with menu interface
├── profile.py           # Profile class for user data and display methods
├── manager.py           # Manager class handling logic: income, expenses, transactions
├── utils.py             # Utility functions: search, update, delete, filter, most
├── profile.json         # Stores budget, savings, goal
├── expenses.json        # Stores list of expenses
├── income.json          # Stores list of income sources
├── transactions.json    # Stores transaction history
└── logs.json            # Stores logs of actions
