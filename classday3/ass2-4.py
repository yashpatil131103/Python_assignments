# Given an input string with the combination of the lower and upper case arrange characters in such a way that all lowercase letter should come first
#s1="aBCd"   #"adBC"
s1="lVjAkS"  #"ljkVAS"


str1=""
str2=""
for i in s1:
    if(i.islower()==True):
        str1= str1 + i
    else:
        str2=str2 + i

print(str1+str2)



#ORR

str3=sorted(s1,reverse=True)
print(str3)
