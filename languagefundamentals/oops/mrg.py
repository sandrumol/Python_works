
class Parent:
    def properties(self):
        print("1kg gold 50 lakhs rupees 2 car")

    def bride(self):
        print("shoba")

class Child(Parent):
    def bride(self):
        print("shuba")

ch=Child()
ch.properties()
ch.bride()
