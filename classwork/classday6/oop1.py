class Employee:
    def __init__(self,ename,eid):
        self.ename=ename
        self.eid=eid
    def display(self):
        print(self.ename,self.eid)

e1=Employee('xyz',123)  
#internally class __new__() and then__init__() methos
e1.display()
