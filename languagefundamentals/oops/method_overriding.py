
class Parent:
    def mobile(self):
        print("Redmi note 12")

    def vehicle(self):
        print("Splender")

class Child(Parent):
    # pass
    def mobile(self):   # overridingq
        print("iphone 15")

ch=Child()
ch.mobile()
ch.vehicle()