import unittest
from expenses import Expense
from reports import category_breakdown, monthly_report


class TestReports(unittest.TestCase):

    def setUp(self):
        self.expenses = [
            Expense("2024-01-10", 100, "Food", "Lunch"),
            Expense("2024-01-12", 50, "Food", "Dinner"),
            Expense("2024-01-15", 200, "Rent", "January Rent")
        ]

    def test_category_breakdown(self):
        # Just checking it runs without error
        category_breakdown(self.expenses)

    def test_monthly_report(self):
        monthly_report(self.expenses)


if __name__ == "__main__":
    unittest.main()
