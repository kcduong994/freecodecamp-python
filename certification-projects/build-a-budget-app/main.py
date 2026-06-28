"""
Build a Budget App

freeCodeCamp Python Certification Project

This module implements:
- Budget categories
- Deposits and withdrawals
- Balance calculations
- Transfers between categories
- Fund validation
- Formatted ledger summaries
- Percentage-spent charts
"""


class Category:
    """Represent a budget category and its transaction ledger."""

    # Tests 1–2:
    # Create a category with a name and an empty ledger.
    def __init__(self, name):
        self.name = name
        self.ledger = []

    # Tests 1–2:
    # Store a deposit in the ledger.
    # The description defaults to an empty string.
    def deposit(self, amount, description=""):
        self.ledger.append(
            {
                "amount": amount,
                "description": description,
            }
        )

    # Tests 3–5 and 14:
    # Store a successful withdrawal as a negative amount.
    # Return False without changing the ledger when funds are insufficient.
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append(
                {
                    "amount": -amount,
                    "description": description,
                }
            )
            return True

        return False

    # Test 6:
    # Calculate the current balance from all ledger entries.
    def get_balance(self):
        balance = 0

        for transaction in self.ledger:
            balance += transaction["amount"]

        return balance

    # Tests 7–11 and 15:
    # Transfer funds from this category to another category.
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(
                amount,
                f"Transfer to {category.name}",
            )

            category.deposit(
                amount,
                f"Transfer from {self.name}",
            )

            return True

        return False

    # Tests 12–13:
    # Check whether the requested amount is available.
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False

        return True

    # Test 16:
    # Return the required formatted category representation.
    def __str__(self):
        output = self.name.center(30, "*") + "\n"

        for transaction in self.ledger:
            description = transaction["description"][:23]
            amount = transaction["amount"]

            output += f"{description:<23}{amount:>7.2f}\n"

        output += f"Total: {self.get_balance()}"

        return output


# Tests 17–24:
# Generate a chart showing the percentage spent by category.
def create_spend_chart(categories):
    # Test 17:
    # Add the required chart title.
    chart = "Percentage spent by category\n"

    spent_amounts = []

    # Calculate spending from withdrawals only.
    for category in categories:
        spent = 0

        for transaction in category.ledger:
            if transaction["amount"] < 0:
                spent += -transaction["amount"]

        spent_amounts.append(spent)

    total_spent = sum(spent_amounts)
    percentages = []

    # Tests 18–19:
    # Calculate percentages and round down to the nearest 10.
    for spent in spent_amounts:
        percentage = int(spent / total_spent * 100)
        percentage = percentage // 10 * 10
        percentages.append(percentage)

    # Tests 18–20:
    # Build the vertical percentage axis and category bars.
    for level in range(100, -1, -10):
        chart += f"{level:>3}| "

        for percentage in percentages:
            if percentage >= level:
                chart += "o  "
            else:
                chart += "   "

        chart += "\n"

    # Test 21:
    # Add the horizontal line below the bars.
    chart += "    "
    chart += "-" * (len(categories) * 3 + 1)
    chart += "\n"

    # Test 23:
    # Find the longest category name.
    max_name_length = max(
        len(category.name) for category in categories
    )

    # Tests 22–24:
    # Write category names vertically with exact spacing.
    # Do not add a newline after the final row.
    for index in range(max_name_length):
        chart += "     "

        for category in categories:
            if index < len(category.name):
                chart += category.name[index] + "  "
            else:
                chart += "   "

        if index < max_name_length - 1:
            chart += "\n"

    return chart
