class Book:
    def __init__(self, author):
        self.__author = author
    
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
    
if __name__ == "__main__":
    b = Book("Jules Verne")
    print(b.author)
    b.set_author = "H.G. Wells"
    print(b.author)
    b.author = 42