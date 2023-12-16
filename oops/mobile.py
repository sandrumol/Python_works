class Mobile:
    name:str
    brand:str
    display:str
    price:int

    def __init__(self,name,brand,display,price):
        self.name=name
        self.brand=brand
        self.display=display
        self.price=price
    
    def display_mobiles(self):
        print(self.name,self.price,self.brand)

    def __str__(self): # string representation of object
        return self.name    # print(obj)

obj=Mobile("iphone15promax","apple","amoled",120000)
obj1=Mobile("samsung23ultra","samsung","amoled",130000)
obj.display_mobiles()
obj1.display_mobiles()

print(obj)
