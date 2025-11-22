#given two string ,s1,s2 create a new string by appendnig s2 in the middle of s1
s1="ault"
s2="Kelly"

str1=s1[0:(len(s1)//2)] +s2 + s1[len(s1)//2:]
print(str1)
