l1=[10,20,30,40,50,60]
l2=[0,1,2,3,4,5]
print(l1)
print(l2)
print("l1[2:2] special case answer will be empty if the star=end ",l1[2:2])
print("l1[3:5]",l1[3:5])
print("l1[-4:-3]",l1[-4:-3])
print("only start is given l1[4:] ",l1[4:])
print("only end is given l1[:3]",l1[:3])
print("only -ve value is given of steo l1[2:0:-1] ",l1[2:0:-1])

print("step is greater then  1 ,when the step is negative we go inreverse order ,l1[2:6:2]",l1[2:6:2])
print("WHen step is +ve ,start should less then end start<end,here star>end  l2[4:1:1]",l2[4:1:1])
print("When step is -ve ,start should greater than end (start>end),here start<end l2[1:4:-1]",l2[4:1:1])


