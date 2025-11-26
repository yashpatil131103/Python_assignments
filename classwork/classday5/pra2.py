""" WAP function for factorial """

def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)

n=int(input("Enter the number for finding factorial "))
fact(n)

