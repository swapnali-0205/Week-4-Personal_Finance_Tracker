import unittest
import os
from expenses import Expense, ExpenseManager
from file_handler import save_to_json, load_from_json

TEST_FILE = "data/expenses.json"


class TestFileHandler(unittest.TestCase):

    def setUp(self):
        self.manager = ExpenseManager()
        self.manager.add_expense(
            Expense("2024-01-10", 100, "Food", "Lunch")
        )

    def test_save_and_load(self):
        save_to_json(self.manager)
        new_manager = ExpenseManager()
        load_from_json(new_manager)
        self.assertEqual(len(new_manager.expenses), 1)

    def tearDown(self):
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)


if __name__ == "__main__":
    unittest.main()
