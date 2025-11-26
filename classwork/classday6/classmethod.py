class Myclass:
    x=10
    def method1(self):
        print("INsdie a method",self.x)
x=Myclass()
x.method1()   # implicitly call fucntion method 1from Myclass
Myclass.method1(x) # above line and this line are same
