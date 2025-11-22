i=0
total=0 
while i<10: 
    marks=int(input("enter marks")) 
    if marks<40:
        break
    else:
	    total =total+marks
    i=i+1
else: # while  else ---> run when beak us not executed in the  loop
    print("totoal marks  =" ,total)  	
