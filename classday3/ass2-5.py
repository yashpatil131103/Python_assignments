#Create a third -string made of the first char of s1 then the last char of s2,\
#next the second char of s1 and secondd last char of s2, and so on .
# Any leftover chars given at the end of the result 
s1="Abcdefg"
s2="ijkVWXyz"
s3=s2[::-1]
s4=""
greater=""

if(len(s1)>len(s3)):
    greater=s1
    length=len(s3)
else:
    greater=s3
    length=len(s1)


for i in range(length):
    s4=s4+s1[i]+s3[i]    

s4=s4+greater[length:]   
print(s4)
