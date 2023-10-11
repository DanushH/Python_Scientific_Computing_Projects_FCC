class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, budget_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget_category.category}")
            budget_category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.category:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            description = item["description"][:23].ljust(23)
            amount = "{:.2f}".format(item["amount"]).rjust(30 - len(description))
            items += f"{description}{amount}\n"
            total += item["amount"]
        output = title + items + f"Total: {total:.2f}"
        return output


def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    spendings = [
        sum(item["amount"] for item in category.ledger if item["amount"] < 0)
        for category in categories
    ]
    total_spent = sum(spendings)
    percentages = [
        (spending / total_spent) * 100 if total_spent != 0 else 0
        for spending in spendings
    ]

    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for percentage in percentages:
            chart += "o  " if percentage >= i else "   "
        chart += "\n"

    chart += "    ----------\n     "
    category_names = [category.category for category in categories]
    max_name_length = max(len(name) for name in category_names)
    for i in range(max_name_length + 1):
        for name in category_names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        chart += "\n     "

    chart = chart.rstrip()
    chart += "  "
    return chart
