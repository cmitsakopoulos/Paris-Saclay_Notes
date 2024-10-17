#Properties vs getters and setters
# Let's consider the example of a bank account
# Write an implementation of a bank account class with the following properties:necessary getters, setters and deleters with apropiate verification.

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name == "":
            raise ValueError("Name cannot be empty")
        self.__name = name

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = balance

    @balance.deleter
    def balance(self):
        del self.__balance

    def __str__(self):
        return f"Name: {self.name}, Balance: {self.balance}"
    

if __name__ == "__main__":
    account = BankAccount("Raul", 100)
    print(account)
    account.name = "Raul"
    account.balance = 100
    print(account)
    account.balance = -100
    print(account)
    del account.balance
    print(account)
    account.name = ""
    print(account)