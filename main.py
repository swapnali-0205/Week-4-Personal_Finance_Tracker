from expenses import Expense, ExpenseManager
from file_handler import save_to_json, load_from_json, export_to_csv, create_backup
from reports import monthly_report, category_breakdown


def show_menu():
    print("""
💰 PERSONAL FINANCE TRACKER
1. Add New Expense
2. View All Expenses
3. Search Expenses
4. Generate Monthly Report
5. View Category Breakdown
6. Set/Update Budget
7. Export Data to CSV
8. View Statistics
9. Backup/Restore Data
0. Exit
""")


def main():
    manager = ExpenseManager()
    load_from_json(manager)
    budget = None

    while True:
        show_menu()
        choice = input("Choose an option: ")

        try:
            # 1. Add Expense
            if choice == "1":
                date = input("Date (YYYY-MM-DD): ")
                amount = input("Amount: ")
                category = input("Category: ")
                desc = input("Description: ")

                expense = Expense(date, amount, category, desc)
                manager.add_expense(expense)
                save_to_json(manager)
                print("✅ Expense added successfully!")

            # 2. View All Expenses
            elif choice == "2":
                if not manager.expenses:
                    print("No expenses recorded.")
                for i, e in enumerate(manager.expenses):
                    print(f"{i+1}. {e.date} | {e.category} | ${e.amount} | {e.description}")

            # 3. Search Expenses
            elif choice == "3":
                keyword = input("Enter category or description keyword: ").lower()
                results = [
                    e for e in manager.expenses
                    if keyword in e.category.lower() or keyword in e.description.lower()
                ]
                for e in results:
                    print(f"{e.date} | {e.category} | ${e.amount} | {e.description}")

            # 4. Monthly Report
            elif choice == "4":
                year = int(input("Year (YYYY): "))
                month = int(input("Month (1-12): "))
                monthly = manager.search_by_month(year, month)
                monthly_report(monthly)

            # 5. Category Breakdown
            elif choice == "5":
                category_breakdown(manager.expenses)

            # 6. Set/Update Budget
            elif choice == "6":
                budget = float(input("Enter monthly budget: "))
                print(f"💵 Budget set to ${budget}")

            # 7. Export CSV
            elif choice == "7":
                export_to_csv(manager)
                print("📁 Data exported to CSV.")

            # 8. View Statistics
            elif choice == "8":
                total = sum(e.amount for e in manager.expenses)
                print(f"📊 Total Expenses: ${total}")
                print(f"📦 Number of Expenses: {len(manager.expenses)}")

            # 9. Backup / Restore
            elif choice == "9":
                create_backup()
                print("🔒 Backup created successfully.")

            # 0. Exit
            elif choice == "0":
                save_to_json(manager)
                print("👋 Goodbye!")
                break

            else:
                print("❌ Invalid option. Try again.")

        except Exception as e:
            print("⚠️ Error:", e)


if __name__ == "__main__":
    main()
