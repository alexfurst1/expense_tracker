from .expense import Expense
from datetime import date


class ExpenseTracker:
    """In-memory tracker for Expense objects."""

    def __init__(self, expenses: list[Expense] | None = None):
        # Use an instance list to avoid shared mutable class state
        self.expenses: list[Expense] = expenses if expenses is not None else []

    def add_expense(self, amount: float, description: str | None = None) -> None:
        expense = Expense(amount, description)
        expense.id = len(self.expenses)
        self.expenses.append(expense)

    def edit_expense(self, expense_id: int, new_amount: float, new_desc: str | None = None) -> None:
        try:
            exp = self.expenses[expense_id]
            exp.amount = new_amount
            if new_desc is not None:
                exp.description = new_desc
        except (IndexError, ValueError, TypeError):
            print("Invalid ID, amount, or description.")

    def delete_expense(self, expense_id: int) -> None:
        if expense_id < 0 or expense_id >= len(self.expenses):
            print('Invalid ID')
            return

        del self.expenses[expense_id]

        # reassign ids to keep them contiguous
        for i, exp in enumerate(self.expenses):
            exp.id = i

    def list_expenses(self) -> None:
        print(f"ID  Date    Description    Amount")
        for exp in self.expenses:
            print(f"{exp.id}  {exp.date}    {exp.description}     {exp.amount}")

    def summary(self, month_int: int | None = None) -> None:
        current_year = date.today().year
        total = 0.0

        if not month_int:
            for exp in self.expenses:
                total += exp.amount
            print(f"Total expenses: ${total}")
            return

        try:
            month_name = date(1900, month_int, 1).strftime('%B')
        except Exception:
            print("Invalid month number")
            return

        for exp in self.expenses:
            if exp.date.month == month_int and exp.date.year == current_year:
                total += exp.amount

        print(f"Total expenses for {month_name}: ${total}")





