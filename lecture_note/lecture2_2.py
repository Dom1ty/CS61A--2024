def cube(k):
    return pow(k,3)
def summation(n,term):
    total = 0
    for i in range(1,n+1):
        total += term(i)
    return total
print(summation(5,cube))
