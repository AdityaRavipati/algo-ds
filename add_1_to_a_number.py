def addOne(x):
    import pdb; pdb.set_trace()
    m = 1
    # Flip all the set bits
    # until we find a 0
    while(x & m):
        x = x ^ m
        m <<= 1

    # flip the rightmost
    # 0 bit
    x = x ^ m
    return x


# Driver program
n = 9
print addOne(n)