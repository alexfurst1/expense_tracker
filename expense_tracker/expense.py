from datetime import date
class Expense:

    def __init__(self, amount: float = 0.0, description: str | None = None):
        self.amount: float = amount
        self.description: str | None = description
        self.date = date.today()
        # id is assigned by ExpenseTracker when the expense is added
        self.id: int | None = None

    def show(self) -> None:
        print(f"ID: {self.id}  Date: {self.date}  Description: {self.description}  Amount: {self.amount}")
