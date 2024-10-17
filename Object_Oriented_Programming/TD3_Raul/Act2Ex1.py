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
        
    def currency(self, rate):
        return self.balance * rate
    
    def new_account(self, name, balance):
        return BankAccount(name, balance)

    def __str__(self):
        return f"Name: {self.name}, Balance: {self.balance}"
    