""" WAP A program to 
"""
def mult_odd():
    result=1
    for i in range(1,100):
        if (i%2!=0):
            result=result*i
    print(result)
    print(len(str(result)))

mult_odd()


