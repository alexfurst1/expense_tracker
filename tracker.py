from datetime import date
import json
import os


class ExpenseTracker:
    """Expense tracker that can save/load from JSON file."""
    
    def __init__(self):
        self.DEFAULT_SAVE_PATH = "expenses.json"
        try:
            with open(self.DEFAULT_SAVE_PATH,"r") as f:
                self.data = json.load(f)
        except FileNotFoundError:
            print("File does not exist")
            self.data = []
        except json.JSONDecodeError:
            print("File exists but is empty or corrupted")
            self.data = []
    


    def add_expense(self, amount: float, desc: str | None = None) -> None:
        new = {"amount":amount,"desc":desc,"id":None}
        new["id"] = len(self.data)
        new["date"] = str(date.today()) 
        self.data.append(new)
        
        try:
            with open(self.DEFAULT_SAVE_PATH,"w") as f:
                json.dump(self.data,f,indent=4)
        except FileNotFoundError:
            print("File does not exist")
        except json.JSONDecodeError:
            print("File exists but is empty or corrupted")



    def edit_expense(self, expense_id: int, new_amount: float, new_desc: str | None = None) -> None:
        try:
            with open(self.DEFAULT_SAVE_PATH,"r") as f:
                self.data = json.load(f)
            for expense in self.data:
                if expense["id"] == expense_id:
                    expense["amount"] = new_amount
                    expense["desc"] = new_desc
            with open(self.DEFAULT_SAVE_PATH,"w") as f:
                json.dump(self.data,f,indent=4)
        except FileNotFoundError:
            print("File not found")
        except json.JSONDecodeError:
            print("Error: JSONDecodeError")

    
    
    def delete_expense(self, expense_id: int) -> None:
        try:
            with open(self.DEFAULT_SAVE_PATH,"r") as f:
                self.data = json.load(f)
            self.data = [item for item in self.data if item["id"] != expense_id]
            with open(self.DEFAULT_SAVE_PATH,"w") as f:
                json.dump(self.data,f,indent=4)
        except FileNotFoundError:
            print("File does not exist")
        except json.JSONDecodeError:
            print("File exists but is empty or corrupted")

    
    
    def list_expenses(self) -> None:
        try:
            with open(self.DEFAULT_SAVE_PATH,"r") as f:
                self.data = json.load(f)
                print(f"ID  Date    Description    Amount")
                for dict in self.data:
                    print(f'{dict["id"]}  {dict["date"]}    {dict["desc"]}     {dict["amount"]}')
        except FileNotFoundError:
            print("File does not exist")
        except json.JSONDecodeError:
            print("File exists but is empty or corrupted")

    def summary(self, month: int | None = None) -> None:
        current_year = date.today().year
        total = 0.0

        try:
            with open(self.DEFAULT_SAVE_PATH,"r") as f:
                self.data = json.load(f)
        except FileNotFoundError, json.JSONDecodeError:
            print("error")

        if not month:
            for exp in self.data:
                total += exp["amount"]
            print(f"Total expenses: ${total}")
            return

        try:
            month_name = date(1900, month, 1).strftime('%B')
        except Exception:
            print("Invalid month number")
            return

        for exp in self.data:
            date_ = exp["date"]
            month_ = int(date_[5:7])
            year = int(date_[:4])
            if month_ == month and year == current_year:
                total += exp["amount"]

        print(f"Total expenses for {month_name}: ${total}")

    