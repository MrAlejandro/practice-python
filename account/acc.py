class Account:
    balance = None
    filepath = None

    def __init__(self, filepath):
        with open(filepath, 'r') as handler:
            self.filepath = filepath
            balance = handler.read()
            handler.close()

            if balance:
                self.balance = float(balance)
            else:
                self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def deposit(self, amount):
        self.balance += amount
        return self

    def commit(self):
        with open(self.filepath, 'w') as handler:
            handler.write(str(self.balance))
            handler.close()



    def print_balance(self):
        print(self.balance)


class CheckingAccount(Account):

    def __init__(self, filepath):
        Account.__init__(self, filepath)

checking = CheckingAccount('balance.txt')
checking.deposit(100)
checking.print_balance()

checking1 = CheckingAccount('balance.txt')
checking1.print_balance()

# account = Account('balance.txt')
# account.print_balance()
# account.withdraw(100).print_balance()
# account.deposit(111).print_balance()
# account.commit()
