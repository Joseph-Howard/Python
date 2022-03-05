#When objects are created, they are passed in the name of the category.

class Category:
    name=''
    funds = 0
#The class should have an instance variable called `ledger` that is a list.
# The class should also contain the following methods:
    def __init__(self, name):
        self.name = name
        self.ledger = list()

# A `deposit` method that accepts an amount and description.
# If no description is given, it should default to an empty string.
# The method should append an object to the ledger list in the form
# of `{"amount": amount, "description": description}`.
    def deposit(self, amount, description=''):
        self.ledger.append(f'"amount":{amount},"description":{description}')


# A `withdraw` method that is similar to the `deposit` method,
# but the amount passed in should be stored in the ledger as a
# negative number. If there are not enough funds, nothing should
# be added to the ledger. This method should return `True` if the
# withdrawal took place, and `False` otherwise.
    def withdraw(self,amount, description = ''):



# A `get_balance` method that returns the current balance of the
# budget category based on the deposits and withdrawals that have occurred.
    def get_balance(self):

# A `transfer` method that accepts an amount and another budget
# category as arguments. The method should add a withdrawal with
# the amount and the description "Transfer to [Destination Budget Category]".
# The method should then add a deposit to the other budget category with
# the amount and the description "Transfer from [Source Budget Category]".
# If there are not enough funds, nothing should be added to either ledgers.
# This method should return `True` if the transfer took place, and `False'
# if not
    def transfer(self,amount,category):
        print('transfer')
# A `check_funds` method that accepts an amount as an argument.
#It returns `False` if the amount is greater than the balance of the
#budget category and returns `True` otherwise. This method should be
# used by both the `withdraw` method and `transfer` method.
    def check_funds(self, amount):
        AcctTotal = 0
        for i in range(self.ledger())
            SplitAmount = self.ledger()[i].split()

        print('check_funds')


def create_spend_chart(categories):
    print('bar chart')


x=Category('food')

x.deposit(10,'test')
print(x)
