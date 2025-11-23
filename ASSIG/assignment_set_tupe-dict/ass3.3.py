#4. Sort and print students and their favourite colours alphabetically by name
people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}

sort_keys=sorted(people)

print(sort_keys)

for k  in sort_keys:
    print(k,people[k])
