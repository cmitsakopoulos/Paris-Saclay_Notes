## Using dunder methods in the magazines and books example

# jPLEASE PUSH ADDITIONS TO CODE, SOME .py files are INCOMPLETE, DELETE WHEN DONE PLS
### user.py
```python
class User:
    def __init__(self, name:str, deposit:int):
        self.name = name
        self.deposit = deposit
        self.copies = {
        }

        def set_name(self, name):
            return

        def get_copies(self)
        return

    def __repr__(self):
        return f"User: {self.name}"
```
Using `from typing import Dict, List` your data types can be represented by test instead of symbols; aka List, instead of [].

## main.py
```python
from user import User
from copy import Copy

def borrow(user: User, book: Book):
    user_copies = user.get_copies() #Check if the user can borrow
    for copy in user_copies():
        if copy.is_late():
            raise ValueError(f"{User} has a late copy")
    try: #Check that a copy is available
        copy = book.get_available_copy()
    except ValueError:
        raise ValueError() #Inform user
    # Check for user deposit availability to borrow
    if user.deposit < book.deposit:
        raise ValueError() # print messages
    else:
        user.deposit -= book.deposit
    user.add_copy(copy)
    print() #Update message that the copy is added to the User's database

if __name__ = "__main__":
    dupont = User("Dupont", 50)
    martin = User("Martin", 20)
    print(dupont, martin)

    cp1 = Copy(1234, "27/12/2020")
    cp2 = Copy(4758, "17/12/2020")
    print(cp1, cp2)

    refact = Book() #enter information as per Class attribute positions
    linux = Magazine() #enter information as per Class attribute positions

    refact.add_copy(cp1) #update the relevant classes with new information
```
### copy.py
```python
from datetime import datetime

class Copy:
    def __init__(self, barcode, return_date):
        self.barcode = barcode
        self.return_date = datetime.strptime(return_date, "%d/%m/%Y") if return_date is not None else None

        def is_available(self):
            return self.return_date is None

        def is_late(self):
            if self.return_date is None:
                return False
            return self.return_date < datetime.now()

        def __repr__(self):
            return f"Copy(self.barcode), (self.return_date)"
```

### resource.py
```python
class Resource:
    def __init__(self, title, deposit):
        self.title = title
        self.deposit = deposit
        self.copies = {}

    def add_copy(self):
        self.copies.update({copy.barcode: copy})
    
    def get_available_copy(self):
        for copy in self.copies.values():
            if copy.is_available(): #this method from Class copy is 
                return copy
        raise ValueError("A copy of this resource is not available")

    def get_copies(self):
        return self.copies
```
### book.py
```python
from resource import Resource #Remember to import otherwise you get a type error, from the super().__init__ method.
class Book(Resource): #Here you are saying that Book is a subclass of Resource, determines how Python should treat this class
    def __init__(self, title, deposit, author, isbn):
        super().__init__(title, deposit)
        self.author = author
        self.isbn = isbn

    def __repr__(self):
```
### magazine.py
```python
from datetime import datetime
from resource import Resource
class Magazine(Resource):
    def __init__(self, deposit, volume, publication):
        super().__init__(title, deposit)
        self.volume = volume
        self.publication = datetime.strptime(return_date, "%d/%m/%Y") if return_date is not None else None

    def __repr__(self):
        return 
```
### location.py
```python

class Location:
    def __init__(self, base, shelf, level):
        self.base = base
        self.self = self
        self.level = level


