#1. accept amount from user and find the minimum number notes required to get the amount amount =512  
#Notes: 2000,500,100,50,10,5,2,1  

#500-1 note  
#10  - 1 note  
#2-  1 coin  
#
#amount=20550  
#2000 – 10 note  
#500 – 1 note  
#50 -1 note  

amount=int(input("Enter the amount "))
temp=amount
th2,hu5,fif,ten,five,two,one=0

if(temp>=2000):
    temp=temp%2000:
if(temp>=500):
    temp=temp%500:
if(temp>=50):
    temp=temp%100
if(temp>=10):
    temp=temp%50
if(temp>=5):
    temp=temp%10
if(temp>=2):
    temp=temp%2
if(temp>1):
    temp=temp%1


print("no of notes of 2000",th2)
print("no of notes of 500",th2)
print("no of notes of 50",th2)
print("no of notes of 10",th2)
print("no of notes of 2",th2)
print("no of notes of 1",th2)

