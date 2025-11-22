
#10. Write a program to accept the price of a bike and display the road tax and insurance to be paid according to the following criteria . also display total amount to be paid.  
      
 #       Cost price (in Rs)           Tax                Inssurance  
  #      > 100000                     15 %                   20%  
   #     > 50000 and <= 100000        10%                    8%  
    #    <= 50000                     5%                     5%   
price=int(input("nter the price of bike "))
tax=0
iss=0
total=0
if(price>100000):
	tax=(15*price)/100	
	iss=(20*price)/100
	total=tax+price+iss
elif(100000 >= price > 50000):
	tax=(10*price)/100
	iss=(8*price)/100
	total=tax+price+iss
elif(price <= 50000):
	tax=(5*price)/100
	iss=tax
	total=price+iss+tax
print("total Amount to be paid is ",total)

