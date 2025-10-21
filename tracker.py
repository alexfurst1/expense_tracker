class Expense:
    
    expenses = []

    def __init__(self,amount: int, description: str, date: str):
        self.amount = amount
        self.description = description
        self.date = date
        self.id: int
        
        if not Expense.expenses:
            self.id = 1
        else:
            self.id = getattr(Expense.expenses[-1],"id")
        
        Expense.expenses.append(self)

    def delete(self):
        print(f"Manually deleting expense {self.id}")
        Expense.expenses.remove(self)

    def show(self):
        print(f"ID: {self.id} ")

class ExpenseTracker:
    expenses = []

    def __init__(self,expenses: list):
        self.expenses = Expense.expenses

    def add_expense(self):
        expense = Expense()
        expense.id = self.expenses[-1].id + 1
        complete = False
        while not complete:
            try:
                expense.amount = int(input("Enter expense amount: "))
                expense.description = input("Enter a description for this expense: ")
                expense.date = input("Enter a date for this expense in the format YYYY-MM-DD: ")
            except ValueError, TypeError:
                print("You may have entered something with the wrong format. Please try again")
                continue
            complete = True

        
