# given a number chck if it is  prime or not 

#for  doesn't break it will be go to  ELSE   eg negative  nnumber if all given are n%i!=0 then  
n=int(input("Enter a number "))
if n<2:
    print("INvalid value")
else:
    for i in range(2,n/2):
        if n%i==0:  
            print("NOT prime")
            break
    else:
        print("IS Prime")
        break
