from expense import Expense
from datetime import date

class ExpenseTracker:
    expenses = []

    def __init__(self,expenses: list):
        self.expenses = Expense.expenses

    def add_expense(self,amount,description: str):
        expense = Expense()
        expense.amount = amount
        expense.description = description
        expense.id = len(self.expenses)
        self.expenses.append(self.expense)
            

    def edit_expense(self,expense_id: int):
        complete = False
        while not complete:
            try:
                self.expenses[expense_id].amount = int(input("Enter new amount: "))
                temp_desc = input("Edit description (Press enter to skip): ")
                if temp_desc != "":
                    self.expenses[expense_id].description = temp_desc
            except ValueError, TypeError:
                print("You may have entered something with the wrong format. Please try again")
                continue
            complete = True
    
    def delete_expense(self, expense_id: int):
        if expense_id < 0 or expense_id >= len(self.expenses):
            print('Invalid ID')
            return 
        
        del self.expenses[expense_id]

        for i, exp in enumerate(self.expenses):
            exp.id = i

    def list_expenses(self):
        print(f"ID  Date    Description    Amount")
        for i in self.expenses:
            print(f"{i.id}  {i.date}    {i.description}     {i.amount}")

    def summary(self, month_int=None):
        current_year = date.today().year
        res = 0
        month_name = date(1900, month_int, 1).strftime('%B')

        
        if not month_int:
            for i in self.expenses:
                res += i.amount
            print(f"Total expenses: ${res}")
            return
        
        for i in self.expenses:
            if i.date.month == month_int and i.date.year == current_year:
                res += i.amount
        print(f"Total expenses for {month_name}: {res}")




        
