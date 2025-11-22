#7. Write a program to take a number from user. Check whether the last digit of that is divisible by 3 or not.  
#[hint: last digit of num is num%10]
n=int(input("Enteh the number"))	
temp=n%10
if(temp%3==0):
	print("entered number's last digit  is  divisible by 3")
else:
	print("Entered number's last digit  is not divisible by 3")
