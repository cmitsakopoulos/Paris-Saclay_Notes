class Book:
    def __init__(self, author):
        self.__author = author
    
    def __new__(cls, *args, **kwargs):
        print("NEW")
        return super().__new__(cls)
    
    def get_author(self):
        return self.author
    
    @property
    def author(self):
        print("Getting author")
        return self.__author
    
    @author.setter
    def author(self, new_author):
        if isinstance(new_author, str):
            self.__author = new_author
        else:
            raise ValueError("Author must be a string")
    
    @classmethod
    def get_new_empty(cls, prefix_author):
        print(cls.counter)
        return cls("Random Book")
        return cls(prefix_author + " Random Book")
        
if __name__ == "__main__":
    book = Book.get_new_empty("EMPTY")
    b = Book("Jules Verne")
    print(b.author)
    b.set_author = "H.G. Wells"
    print(b.author)
    b.author = 42