class Book:
    name:str
    author:str
    pages:int
    price:int
    # instance variables self.
    # constructor -> initializing instance variables
    # python __init__()
    # constructor automatically invokes while object creation

    def __init__(self,name,author,pages,price):
        # initializing instance variables
        self.name=name
        self.author=author
        self.pages=pages
        self.price=price

    def display_book(self):
        print(self.name,self.author)

    def __str__(self): # string representation of object
        return self.name

obj=Book("randamoozham","mt",489,650)
obj.display_book()

print(obj)