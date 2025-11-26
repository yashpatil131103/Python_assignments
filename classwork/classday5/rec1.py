#RECUSIVE FUNCTIOn
def print_hello(n):
    if n<1:
        return
    else:
        print("HEllo",n)
        print_hello(n-1) #recussive 

print_hello(3)      
