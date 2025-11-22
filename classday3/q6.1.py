l1=['a','b','c','','d']
l2=l1.copy()
for e in l1:
    if e== "":
        l2.remove(e)
print(l2)
