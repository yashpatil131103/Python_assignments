#Accept number from user and check wheathe it is divisble by 5 and 11 if give appropate message 
n=int(input("ENter the number"))

for i in range(2,n//2):
    if(n%5==0) & (n%11==0):
        print("Entered number is divisble by 4=5 and 11")
else:
    print("Entered number is NOT divisble by 5 and 11)=")

