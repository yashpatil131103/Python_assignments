#1.A student will not be allowed to sit in exam if his/her attendence is less than 75%.  
#Take following input from user Number of classes held Number of classes attended. And print percentage of class attended  
#Is student is allowed to sit in exam or not. 
name=str(input("enter the name of the  student"))
n=int(input("enter the number the studnet attended"))
t=int(input("Enter  total number of classes held"))

percentage =(n/t)*100

if(percentage>75):
	print("the student",name,"is allowdto sit ")
else:
	print("the student ",name,"is not allowed to sit ")

