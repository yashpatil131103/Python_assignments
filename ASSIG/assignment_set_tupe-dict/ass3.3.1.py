#3. Write a menu driven program to practice Dictionary functions.
#Write a program to accept name of a person and their vehicle and store it in a dictionary.
#Ask user if they want to continue to accept multiple values.
#Display following menu:
#a. Add new person name and a vehicle name.
#b. Delete a person name and vehicle name from the dictionary.
#----Accept person name from user.
#----Check whether person name exists in the dictionary.
#----If exists show person name and vehicle name to the user.
#----Confirm for deletion, if user enters y
#then delete otherwise no. Display appropriate message.
#c. Modify vehicle name for the person
#----Accept a person name from user.
#----Check whether the person’s name exists.
#----If the name exists, show the person’s name and vehicle name to user.
#Ask for new value and then overwrite the old value.
#d. Search vehicle for the given person’s name.
#e. Search list of people, who have given a vehicle
#f. Display all person names.
#g. Display all vehicle names.
#h. Exit


vehicles={ "Yash":"dream Yuga"}

#add person and vehicle
name = input("Enter you name")
veh_name = input("Enter you vechile name")
vehicles[name] = veh_name

#delete a person
name=input("Enter name to be deleted")
#get or in operator
if name in vehicles:
    print(name,vehicles[name])
    yn=input("Do you want to delete")
    if(yn == "Y"):
        del vehicles[name]
else:
    print("person name not found")


#display all teh person name
print(list(vehicles.keys()))



#Modify the value 
name=input("Enter name to modify ")

if name in vehicles:
    print(name,vehicles[name])
    entry=input("Enter new vehicle name")
    vehicles[name]=entry
    print(name,vehicles[name])

print(list(vehicles.keys()))


#d. Search vehicle for the given person’s name.

name=input("Enter the vehicles name to get the owner name")
for k,v in vehicles.items():
    if v==name:
        print(k,v)

#e. Search list of people, who have given a vehicle
for name in vehicles.keys():
    if name!=None:
        print(name)
#f. Display all person names.
for k,v in vehicles.items():
    print(k)
#g. Display all vehicle names.
for k,v in vehicles.items():
    print(v)
