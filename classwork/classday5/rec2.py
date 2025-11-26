def fact_rec(n):
    if n<1:
        return 1
    else:
        print(n)
        return n*fact_rec(n-1)

fact_rec(3)
