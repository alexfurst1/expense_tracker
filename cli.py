import argparse
from expense_tracker.tracker import ExpenseTracker

def main():
    parser = argparse.ArgumentParser(description="CLI Expense Tracker")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add",help="add an expense")
    add_parser.add_argument()

    edit_parser = subparsers.add_parser("edit",help="modify an existing expense")
    delete_parser = subparsers.add_parser("delete",help="delete an existing expense")
    list_expense_parser = subparsers.add_parser("list",help="list all expenses")
    summary_parser = subparsers.add_parser("summary",help="give a summary of all expenses")
    summary_parser.add_argument("--month",help="list a summary of all expenses from a specified month of the current year")

    args = parser.parse_args()
    tracker = ExpenseTracker()
    
    if args.command == "add":
        tracker.add_expense
