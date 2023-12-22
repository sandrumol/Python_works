from abc import ABC,abstractmethod

class DbConnect(ABC):

    @abstractmethod
    def __init__(self,user,password,port,db):
        pass

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute_query(self):
        pass

    @abstractmethod
    def close(self):
        pass

class MyDb(DbConnect):

    def __init__(self,user,password,port,db):
        self.user=user
        self.password=password
        self.port=port
        self.db=db

    def connect(self):
        print("My database connected")

    def execute_query(self):
        print("My database executed")

    def close(self):
        print("My database closed")


obj=MyDb("user","user@123",3306,"mydb")
obj.connect()
obj.execute_query()
obj.close()