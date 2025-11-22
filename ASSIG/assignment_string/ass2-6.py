#6. Find all occurrences of “USA” from right to left in a given string 
#ignoring the case. also display the
#starting position
#Given:

#Expected answer : 16, 11
#str1 = "Welcome to USA. usa awesome, isn't it?"

str1 = "Welcome to USA. usa awesome, isn't it?"
text = str1.lower()
word = "usa"

i = len(text) - 1
occurnace = []

while i >= 0:
    if text[i:i+3] == word:
        occurnace.append(i + 1)  
    i -= 1

print(occurnace)  
