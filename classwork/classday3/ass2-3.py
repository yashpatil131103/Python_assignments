#two string , s1 and s2 return a new string made of the first middle and last charcters each input strrign

s1="America"
s2="Japan"


str1= s1[0:1:] + s2[0:1:] + s1[(len(s1)//2):((len(s1)//2)+1)] + s2[(len(s2)//2):((len(s2)//2)+1)] + s1[-1:-2:-1]+s2[-1:-2:-1]
print(str1)
