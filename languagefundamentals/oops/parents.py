class Parent:

    def properties(self):
        self.vehicles=["splender","cd100"]
        return self.vehicles
    
class Child(Parent):

    def properties(self):
        self.context=super().properties()
        self.context.append("thar")
        return self.context
    
ch=Child()
print(ch.properties())