with open("new_file2.txt",'w') as fp:
    print("new file is created")
    fp.write("ehllo DITISS!!!!!")
    contents=fp.read()
    lines_list =contents.split('\n')
    

