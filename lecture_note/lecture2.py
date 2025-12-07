def fib(n):
    pre,current = 0,1
    k = 1
    while k < n:
        pre,current = current,pre + current
        k += 1
    return current
x = fib(5)
print(x)