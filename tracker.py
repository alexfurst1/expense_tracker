class Expense:
    
    expenses = []

    def __init__(self,amount: int, description: str, date: str):
        self.amount = amount
        self.description = description
        self.date = date
        
        if not Expense.expenses:
            self.id = 1
        else:
            self.id = getattr(Expense.expenses[-1],"id")
        
        Expense.expenses.append(self)



    def update_expense(self,new_amount: int, new_desc: str, new_date: str):
        self.amount = new_amount
        self.description = new_desc

    def delete(self):
        print(f"Manually deleting expense {self.id}")
        Expense.expenses.remove(self)

    def show(self):
        print(f"ID: {self.id} ")

class ExpenseTracker:

    def __init__(self,expenses: list):
        self.expenses = Expense.expenses

expense1 = Expense(30, "lunch","2025-09-13")
print(expense1.id)