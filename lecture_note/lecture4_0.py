def swipe(n):
    """Print the digits of n, one per line, first backward then forward.

    >>> swipe(2837)
    7
    3
    8
    2
    8
    3
    7
    """
    if n < 10:
        print(n)
    else:
        print(n%10)
        
        swipe(n//10)
        print(n%10)
    
def skip_factorial(n):
    """Return the product of positive integers n * (n - 2) * (n - 4) * ...

    >>> skip_factorial(5) # 5 * 3 * 1
    15
    >>> skip_factorial(8) # 8 * 6 * 4 * 2
    384
    """
    if n <= 2:
        return n
    
    else:
        return n * skip_factorial(n - 2)
    
def is_prime2(n):
    assert n > 1
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i = i + 1
    return True

    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
def is_prime(n):
    if n <= 1:
        return False
    def f(i):
        if i**i > n:
            return True
        if  n% i == 0:
            return False
        else:
            return f(i+1)
    return f(2)


def hailstone(n):
    """Print out the hailstone sequence starting at n, 
    and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
   
    
    print(n)
    if n % 2 == 0:
        return even(n)
    else:
        return odd(n)

def even(n):
    
    return 1+ hailstone(n/2)

def odd(n):
    
    "*** YOUR CODE HERE ***"
    if n == 1:
        return 1
    else:
        return 1+ hailstone( 3*n + 1)

        