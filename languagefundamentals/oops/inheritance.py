# single inheritance =>child have only one parent class

class Parent:
    def mobile(self):
        print("Redmi note 12")

class Child(Parent):
    pass

ch=Child()
ch.mobile()