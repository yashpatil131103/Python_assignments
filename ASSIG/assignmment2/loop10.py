#10.Write a program in python to find the sum of the series [ x - x^3 + x^5 –x^7+x^9-x^11+ ......].  
#Test Data : 
#Input the value of x :2 Input number of terms : 5 Expected Output : 
#The values of the series: 
#2 
#-8 
#32 
#-128 
#512 
#The sum = 410 
total=0

x=int(input("entere value of x"))

n=int(input("enter  no of terms in series"))
for i in range(1,n+1):
    num=((-1)**(i-1)) * x**(2*n-1)
   
    print(num)
    total += num
print(total)

