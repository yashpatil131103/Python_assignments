#wap to print grades based on marks 
#A+ >75
# A 60-75
#B  50-60
#C  40-50
#F  <40
marks =67
if marks <40:
	print("FAIL")
elif 40 <=marks <50:
	print("C")
elif 50<=marks <60:
	print("B")
elif 60<=marks <75:
	print("A")
elif marks >= 75:
	print("A+")


