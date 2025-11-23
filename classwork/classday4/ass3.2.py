#2. Given a dictionary of students and their favourite colours:
people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}
#a. Find out how many students are in the list
#b. Change Lisa’s favourite colour
#c. Remove 'Jenny' and her favourite colour

print("how manu students are in dict",len(people))
print("lisa fav color",people['Lisa'])
print("Rmeov jenny")

people.pop("Jenny")
#del people["Jenny"]
print(people)

