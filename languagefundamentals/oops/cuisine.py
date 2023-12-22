class Cusinie:
    name: str

    def __init__(self,name):
        self.name=name

    def __str__(self):
        return self.name

class Dish(Cusinie):
    dish_name:str
    ingredients:str
    price:int

    def __init__(self,name,dish_name,ingredients,price):
        super().__init__(name)
        self.dish_name=dish_name
        self.ingredients=ingredients
        self.price=price

    
dish1=Dish("indian","briyani","rice",150)
print(dish1,end=",")
print(dish1.dish_name)