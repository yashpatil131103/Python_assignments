#take comma seprated integer from user 
#print its addtion
nums=input("Enter comma seprated number")
print(nums)
nums=nums.split(',')
print(nums)
total=0
for i in nums:
    n=int(i)
    total +=n
print(total)    


l2=list(map(int,nums))  #apply int function to every string in nums 
print(l2)


nums=input("Enter comma seprated intefea")
l3=list(map(int,nums.split(",")))
print(l3)


l4=[10,20,30]
import math
print(list(map(math.sqrt,l4)))
