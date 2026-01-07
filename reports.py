from collections import defaultdict


def monthly_report(expenses):
    total = sum(e.amount for e in expenses)
    print(f"\n📅 Monthly Total: ${total}")

    for e in expenses:
        print(f"{e.date} | {e.category} | ${e.amount} | {e.description}")


def category_breakdown(expenses):
    categories = defaultdict(float)
    for e in expenses:
        categories[e.category] += e.amount

    print("\n📊 Category Breakdown:")
    for cat, amt in categories.items():
        print(f"{cat}: ${amt}")
