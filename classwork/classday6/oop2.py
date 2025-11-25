class car:
    def __init__(self,studname,rno,cource):
        self.studentname=studname
        self.rollno=rno
        self.cource=cource
    def display(self):
        print(self.studentname,self.rollno,self.cource)

c1=car('MH!@K@$%^','abcd','creta')   
c1.display()
