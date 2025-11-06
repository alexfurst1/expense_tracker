from datetime import date
import json
import os


class ExpenseTracker:
    """Expense tracker that can save/load from JSON file."""
    
    DEFAULT_SAVE_PATH = "expenses.json"
    
    try:
        with open(DEFAULT_SAVE_PATH,"r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("File does not exist")
        data = []
    except json.JSONDecodeError:
        print("File exists but is empty or corrupted")
        data = []
    


    def add_expense(self, amount: float, desc: str | None = None) -> None:
        new = {"amount":amount,"desc":desc,"id":None}
        new["id"] = len(self.data)
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
            data = [item for item in data if item["id"] != expense_id]
            with open(self.DEFAULT_SAVE_PATH,"w") as f:
                json.dump(data,f,indent=4)
        except FileNotFoundError, json.JSONDecodeError:
            print("error")

    
    
    def list_expenses(self) -> None:
        try:
            with open(self.DEFAULT_SAVE_PATH,"r") as f:
                self.data = json.load(f)
                print(f"ID  Date    Description    Amount")
                for dict in self.data:
                    print(f"{dict["id"]}  {dict["date"]}    {dict["desc"]}     {dict["amount"]}")
        except FileNotFoundError, json.JSONDecodeError:
            print("error whoops!")

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

    def save(self, filepath: str = DEFAULT_SAVE_PATH) -> None:
        """Save expenses to a JSON file."""
        expenses_data = []
        for exp in self.expenses:
            expenses_data.append({
                'amount': exp.amount,
                'description': exp.description,
                'date': exp.date.isoformat(),
                'id': exp.id
            })
        
        with open(filepath, 'w') as f:
            json.dump(expenses_data, f, indent=2)
        print(f"Saved {len(self.expenses)} expenses to {filepath}")

    def load(self, filepath: str = DEFAULT_SAVE_PATH) -> None:
        """Load expenses from a JSON file."""
        if not os.path.exists(filepath):
            print(f"No saved expenses found at {filepath}")
            return

        try:
            with open(filepath, 'r') as f:
                expenses_data = json.load(f)

            self.expenses = []
            for data in expenses_data:
                exp = Expense(data['amount'], data['description'])
                exp.date = date.fromisoformat(data['date'])
                exp.id = data['id']
                self.expenses.append(exp)
            print(f"Loaded {len(self.expenses)} expenses from {filepath}")
        except Exception as e:
            print(f"Error loading expenses: {e}")