from datetime import date
class Expense:

    def __init__(self,amount: int, description: str):
        self.amount = amount
        self.description = description
        self.date = date.today()
        self.id: int

    def show(self):
        print(f"ID: {self.id} ")
