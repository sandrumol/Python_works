# bank-> ac_num,name ,branch,ifsc code,ac_type,balance
# def create_acc()
# def deposit(self,amount)
# def withdraw(self,amount)
# def get_balance()

class Bank:
    ac_num:str
    name:str
    ac_type:str
    ifsc_code:str
    branch:str
    balance:int

    def create_account(self,ac_no,name,ac_type,ifsc_code,branch,balance):
        # initializing instance variables
        self.ac_num=ac_no
        self.name=name
        self.ac_type=ac_type
        self.ifsc_code=ifsc_code
        self.branch=branch
        self.balance=balance
    
    def deposit(self,amount):
        self.balance+=amount
        print(f"Your {self.ac_num} has been credited with {amount} available balance is {self.balance}")

    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance=amount
            print(f"Your {self.ac_num} has been debited with {amount} available balance is {self.balance}")

    def get_balance(self):
        print("Your available balance is ",self.balance)

obj=Bank()
obj.create_account(123,"hari","savings","sbi00045","kakkanad",6000)
obj.deposit(50000)
