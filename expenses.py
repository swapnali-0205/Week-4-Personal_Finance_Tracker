from datetime import datetime


class Expense:
    def __init__(self, date, amount, category, description):
        self.date = self.validate_date(date)
        self.amount = self.validate_amount(amount)
        self.category = category.strip().title()
        self.description = description.strip()

    def validate_date(self, date_str):
        try:
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Date must be YYYY-MM-DD")

    def validate_amount(self, amount):
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Amount must be positive")
        return amount

    def to_dict(self):
        return {
            "date": self.date.isoformat(),
            "amount": self.amount,
            "category": self.category,
            "description": self.description
        }


class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            self.expenses.pop(index)
        else:
            raise IndexError("Invalid expense index")

    def search_by_category(self, category):
        return [e for e in self.expenses if e.category == category.title()]

    def search_by_month(self, year, month):
        return [
            e for e in self.expenses
            if e.date.year == year and e.date.month == month
        ]
