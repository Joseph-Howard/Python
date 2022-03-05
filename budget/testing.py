class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = list([])
        self.funds = 0.0

    def __repr__(self):
        Printed_Header = self.name.center(30, "*")+"\n"
        Printed_Ledger =''

        for i in self.ledger:
            Printed_Description = "{:<23}".format(i["name"])
            Printed_Amount = "{:>7.2f}".format(i["amount"])

            Printed_Ledger += "{}{}\n".format(Printed_description[:23], Printed_Amount[:7])
        Printed_total = "Total: {:.2f}".format(self.funds)
        return Printed_Header + Printed_Ledger + Printed_total


    def deposit(self, amount, description=''):
        amount = abs(amount)
        self.ledger.append(f'"amount":{amount},"description":{description}')
        self.funds += amount

        #print(self.ledger)

    def withdraw(self,amount, description = ''):
        amount = -abs(amount)
        if self.check_funds(amount) == True:
           self.ledger.append(f'"amount":{amount},"description":{description}')
           self.funds += amount
           return True
        else:
           return False

    def transfer(self,amount,Second_Self):
        x = Category(Second_Self)
        if  self.withdraw(amount,f'Transfer to {x.name}'):
            x.deposit(amount,f'Transfer to {self.name}')
            return True
        else:
            return False

    def get_balance(self):
        return self.funds


    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        else:
            return False

def create_spend_chart(categories):
    spent_amounts = []
    # Get total spent in each category
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])
        spent_amounts.append(round(spent, 2))

    # Calculate percentage rounded down to the nearest 10
    total = round(sum(spent_amounts), 2)
    spent_percentage = list(map(lambda amount: int((((amount / total) * 10) // 1) * 10), spent_amounts))

    # Create the bar chart substrings
    header = "Percentage spent by category\n"

    chart = ""
    for value in reversed(range(0, 101, 10)):
        chart += str(value).rjust(3) + '|'
        for percent in spent_percentage:
            if percent >= value:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"

    footer = "    " + "-" * ((3 * len(categories)) + 1) + "\n"
    descriptions = list(map(lambda category: category.description, categories))
    max_length = max(map(lambda description: len(description), descriptions))
    descriptions = list(map(lambda description: description.ljust(max_length), descriptions))
    for x in zip(*descriptions):
        footer += "    " + "".join(map(lambda s: s.center(3), x)) + " \n"

    return (header + chart + footer).rstrip("\n")
