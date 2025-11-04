import argparse
from expense_tracker.tracker import ExpenseTracker

def main():
    parser = argparse.ArgumentParser(description="CLI Expense Tracker")
    subparsers = parser.add_subparsers(dest="command")

    tracker = ExpenseTracker()

    add_parser = subparsers.add_parser("add",help="add an expense")
    add_parser.add_argument("amount", type=float, help="enter the dollar amount of the expense as a float")
    add_parser.add_argument("--desc", type=str, help="add a description for this expense (optional)")

    add_parser.set_defaults(func=lambda args: tracker.add_expense(
        amount = args.amount,
        description = args.desc # i guess the -- is just ignored here
        ))

    edit_parser = subparsers.add_parser("edit",help="modify an existing expense")
    edit_parser.add_argument("expense_id", type=int, help="enter the id of the existing expense to edit it")
    edit_parser.add_argument("new_amount", type=float, help="edit the existing amount for this expense as a float")
    edit_parser.add_argument("--new_desc", type=str, help="enter a new description for this expense (optional)")

    edit_parser.set_defaults(func=lambda args: tracker.edit_expense(
        expense_id = args.expense_id,
        new_amount = args.new_amount,
        new_desc = args.new_desc
    ))

    delete_parser = subparsers.add_parser("delete",help="delete an existing expense")
    delete_parser.add_argument("expense_id", type=int, help="enter the expense id to delete this expense")

    delete_parser.set_defaults(func=lambda args: tracker.delete_expense(
        expense_id = args.expense_id
    ))

    list_expense_parser = subparsers.add_parser("list",help="list all expenses")
    list_expense_parser.set_defaults(func=lambda args: tracker.list_expenses())


    summary_parser = subparsers.add_parser("summary",help="give a summary of all expenses")
    summary_parser.add_argument("--month", type=int, help="list a summary of all expenses from a specified month of the current year")

    summary_parser.set_defaults(func=lambda args: tracker.summary(
        month = args.month
    ))

    args = parser.parse_args()
    
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
    
    
