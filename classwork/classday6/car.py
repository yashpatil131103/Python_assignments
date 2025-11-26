class car:
    def __init__(self):
        self.regno=input("Enter reg no")
        self.owner=input("Enter owner name")
        self.model=input("model")
    def display(self):
        print(self.regno,self.owner,self.model)
c1=car()
c1.display()
