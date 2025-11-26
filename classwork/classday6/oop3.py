class Employee:
    company_name="google"
    def __init__(self,ename,eid):
        self.ename=ename
        self.eid=eid
    def diplay(self):  #instance method
        print(self.ename,self.eid)
    @classmethod      #class method
    def method1(cls):
        print("IS thsi a paramter")
        print(cls.class_var2)
    @staticmethod        #decorator
    def method2():
        print("us this a paramter of static method")

E1=Employee("heuhr",121)
