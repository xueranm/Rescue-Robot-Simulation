class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposite(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        self.balance -= amt

class SavingsAccount(BankAccount):

    def __init__(self):
        super().__init__()
        self.transaction_count = 0

    def withdraw(self,amount):
        super().withdraw(amount)
        self.transaction_count += 1



account = SavingsAccount()
account.deposit(45)


class Vehicle:
    def __init__(self):
        self.color = 'Blue'

    def drive(self):
        pass

class Collectible:
    def __init__(self):
        self.price = 1000

    def inspect(self):
        pass

class ClassicCar(Vehicle, Collectible):
    def __init__(self):
        super().__init__()
        Vehicle.__init__(self)
        Collectible.__init__(self)




