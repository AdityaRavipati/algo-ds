def fib(n, lookup):
    # Base case
    if n == 0 or n == 1:
        lookup[n] = n

        # If the value is not calculated previously then calculate it
    if lookup[n] is None:
        lookup[n] = fib(n - 1, lookup) + fib(n - 2, lookup)

    print lookup
    return lookup[n]


n = 5
lookup = [None]*(10)
print "Fibonacci Number is ", fib(n, lookup)