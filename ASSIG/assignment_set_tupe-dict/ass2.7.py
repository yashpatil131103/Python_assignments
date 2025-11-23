#7. Take two integer values in a & b. Swap their values using tuple, using temparary variable and without tuple and without temparary variable.
#Ex. a=10 b=23
#After swapping a=23 b=10

a=10
b=23
a,b=b,a
print(a,b)

temp=a
a=b
b=temp
print(a,b)


a=a+b
b=a-b
a=a-b
print(a,b)

