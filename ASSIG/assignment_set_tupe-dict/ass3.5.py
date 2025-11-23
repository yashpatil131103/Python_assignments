#5. Take a sentence as input from user. Every word is seperated by space. 
#a. Create a word_count dictionary which will have unique words and their count. 

sent=input("Enter a Sentnce ")

words =sent.split(" ")
word_count={}

for word in words:
    if word in word_count:
        val=word_count[word]
        word_count[word]=val+1
    else:
        word_count[word]=1

print(word_count)

s=0
es=0
e_es_count={'s':0,'es':0}
for i in word_count:
    if i[-1]=='s':
        if i[-2:]=='es':
            e_es_count['es']=e_es_count['es']+1                         
        e_es_count['s']=e_es_count['s']+1

    print("Current e_es_count is ",e_es_count)

print("ends with s",e_es_count['s']," ends with es",e_es_count['es'])    

       
