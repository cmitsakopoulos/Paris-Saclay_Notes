import datetime

class Book:
    def __init__(self, title: str, deposit: int, author:str, ISBN:int):
        self.title = title
        self.deposit = deposit
        self.author = author
        self.ISBN = ISBN
    

class User:
    def __init__(self, name: str, deposit: int):
        self.username = name
        self.deposit = deposit
    def info(self):
        print("User")
    

class Magazine:
    def __init__(self, title: str, volume: int, publication: datetime, deposit:int):
        self.title = title
        self.deposit = deposit
        self.volume = volume
        self.publication = publication 

class Location:
    def __init__(self, beam: int, shelf: int, level: int):
        self.beam = beam
        self.shelf = shelf
        self.level = level

class Copy:
    def __init__(self, barcode: int, re_turn: datetime):
        self.barcode = barcode
        self.re_turn = re_turn
    def get(self):
        return self.barcode, self.re_turn
    
class do_something:
    def __init__(self):
        pass


book_Loc = Location(20, 8, 9)
copy_test = Copy(100, 10/2/2000)
book = Book("How to code", 1, "Mike", 1984)
user_1 = User("Hamidi", 0)

