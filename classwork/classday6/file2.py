fp=open('new_file.txt','w')

fp.write("Hello how are tou")


contents=fp.read()
print(contents)

fp.close()
