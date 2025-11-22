#6. Remove empty strings from the list of strings
#list1 = ["Ashish", "", "Atharva", "Amit", "", "Revati"]
#output:
#["Ashish", "Atharva", "Amit", "Revati"]

list1 = ["Ashish", "", "Atharva", "Amit", "", "Revati"]
l2=[]
for i in list1:
    if(i   != ""):
        l2.append(i)
print(l2)



#------------------------------------------

