import datetime

class Customer:
    def __init__(self, name: str, ident: int, balance: int):
        self._name = name          
        self._id = ident           
        self.bookings = []
        self._balance = balance   
    
    def __str__(self):
        return f"User {self._name} has the following bookings {self.bookings}"
    
    @property
    def name_changer(self):
        print(f"The user's name is {self._name}")
        return self._name  
    
    @name_changer.setter
    def name_changer(self, value: str):
        self._name = " ".join(value.split())  
        print(f"User's name changed to {self._name}")
    
    @name_changer.deleter
    def name_changer(self):
        del self._name
        print("User's name emptied")
    
    @property
    def get_id(self):
        print(f"User {self._id} is {self._name}")
        return self._id  
    
    @get_id.setter
    def get_id(self, value: int):
        self._id = value
        print(f"User's id changed to {self._id}")
    
    @get_id.deleter
    def get_id(self):
        del self._id
        print("User's id emptied")
   
    @property
    def update_booking(self):
        print(f"User has these bookings in their account: {self.bookings}")
        return self.bookings  
    
    @update_booking.setter
    def update_booking(self, item: str):
        self.bookings.append(item)
        print(f"{item} has been added to the user's bookings")
    
    # Property for balance_
    @property
    def balance_(self):
        print(f"User has {self._balance} in their account")
        return self._balance  
    
    @balance_.setter
    def balance_(self, value: int):
        if value >= 0:
            self._balance += value
        else:
            self._balance -= value
        print(f"User balance has been updated to {self._balance}, {value} has been considered")
    
    @balance_.deleter
    def balance_(self):
        del self._balance
        print("User's balance emptied")


class Trip:
    def __init__(self, offer:float):
        self.destinations = []
        self.costs = []
        self.dates = []
        self.offer = offer

    def apply_offer(self, choice, customer_id):
        customer_ident = Customer.get_id
        print(customer_id)

    @property
    def destinations_changer(self):
        print(f"Destinations are: {self.destinations}")
        return self.destinations.copy() 
    
    @destinations_changer.setter
    def destinations_changer(self, destinations):
        for i in destinations.split(" "):
            if i in destinations:
                print(f"{i} already in list")
            else:
                self.destinations.append(i)
        print(f"User's name changed to {self.destinations}")

    @property
    def costs_changer(self):
        print(f"The user's name is {self.costs}")
        return self.costs  

    pass
class Corporation:
    pass

class Payment:
    pass
class Store:
    pass

if __name__ == "__main__":
    test = Customer("OogaBooga", 9, 10)
    test.get_id = 200
    print(test._id)
    print(test)
    update_dest = Trip()
    ooga = apply_offer("Miou", 200)
    print(ooga)