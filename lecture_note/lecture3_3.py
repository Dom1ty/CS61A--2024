def delay(arg):
    print("delayed")
    def g():
        return arg
    return g
print(delay(delay)()(6)())


def pirate(arggg):
    def plunder(arggg):
        return arggg
    return plunder

def make_keeper(n):
    """Returns a function that takes one parameter cond and prints
    out all integers 1..i..n where calling cond(i) returns True.

    >>> def is_even(x): # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    >>> make_keeper(5)(lambda x: True)
    1
    2
    3
    4
    5
    >>> make_keeper(5)(lambda x: False)  # Nothing is printed
    """
    "*** YOUR CODE HERE ***"
    def keeper(cond):
         for i in range(n+1):
                if cond(i):
                    print(i)
    return keeper


def find_digit(k):
    """Returns a function that returns the kth digit of x.

    >>> find_digit(2)(3456)
    5
    >>> find_digit(2)(5678)
    7
    >>> find_digit(1)(10)
    0
    >>> find_digit(4)(789)
    0
    """
    assert k > 0
    "*** YOUR CODE HERE ***"
    def length(n):
       for i in range(k - 1):
            n //= 10
       if n == 0:
           return 0
       
       return n % 10
    
    return length

        


