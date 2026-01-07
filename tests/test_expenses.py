import unittest
from expenses import Expense, ExpenseManager


class TestExpense(unittest.TestCase):

    def test_expense_creation(self):
        e = Expense("2024-01-10", 100, "Food", "Lunch")
        self.assertEqual(e.amount, 100.0)
        self.assertEqual(e.category, "Food")

    def test_invalid_date(self):
        with self.assertRaises(ValueError):
            Expense("10-01-2024", 50, "Food", "Lunch")

    def test_manager_add(self):
        manager = ExpenseManager()
        e = Expense("2024-01-10", 50, "Transport", "Bus")
        manager.add_expense(e)
        self.assertEqual(len(manager.expenses), 1)


if __name__ == "__main__":
    unittest.main()
