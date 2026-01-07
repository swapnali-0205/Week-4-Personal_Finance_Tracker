import json
import csv
import os
from expenses import Expense


DATA_FILE = "data/expenses.json"
BACKUP_FILE = "data/backup_expenses.json"


def save_to_json(expense_manager):
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump([e.to_dict() for e in expense_manager.expenses], f, indent=4)
    create_backup()


def load_from_json(expense_manager):
    if not os.path.exists(DATA_FILE):
        return
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            for item in data:
                expense_manager.add_expense(
                    Expense(
                        item["date"],
                        item["amount"],
                        item["category"],
                        item["description"]
                    )
                )
    except Exception as e:
        print("Error loading file:", e)


def create_backup():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as src, open(BACKUP_FILE, "w") as dest:
            dest.write(src.read())


def export_to_csv(expense_manager):
    with open("data/expenses.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Amount", "Category", "Description"])
        for e in expense_manager.expenses:
            writer.writerow([e.date, e.amount, e.category, e.description])
            
def create_backup():
    import shutil
    shutil.copy("data/expenses.json", "data/backup_expenses.json")
