# simple pattern 
n=8
for i in range(n):
    print("*" *(i+1))

print("#########################################################")

n=int(input("enter number"))
for i in range(1,n,2):
    print("*"*(i))

print("##########################################################################")

n=int(input("Enher no os lne enter only odd numbers"))
stars=1
spaces=n//2
while stars<=n:  #for starts in  range(1,n+1,2):
    print(" " * spaces+"*"*stars)    
    stars=stars+2
    spaces=spaces-1

print("####################################################################")


