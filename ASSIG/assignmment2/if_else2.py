#2. Modify the above question Q1. if student has ttendance less than 75% then ask user if he/she has medical cause or not ( 'Y' or 'N' ).  print "Allow" 
#if he/she has medical cause else not allowed. 
name=str(input("enter the name of the  student"))
n=int(input("enter the number the studnet attended"))
t=int(input("Enter  total number of classes held"))

percentage =(n/t)*100

if(percentage>75):
        print("the student",name,"is allowdto sit ")
else:
	inputyesno=input("Do you have any medical reason if yes 'Y' ,if no 'N' ")
	if(inputyesno=='y' or inputyesno=='Y' ):
		print(name,'you are allowed to sit')
	else: 
		print(name,"is not allow=ed to sit ")
          
