# def titleToNumber(s):
#     import pdb; pdb.set_trace()
#     result = 0
#     for B in range(len(s)):
#         result *= 26
#         result += ord(s[B]) - ord('A') + 1
#
#     return result

##############################################


def printString(n):
    import pdb; pdb.set_trace()
    s = ''
    while (n):
        if (n % 26 == 0):
            s = 'Z' + s
            n = n // 26-1
        else:
            s = chr((n % 26) + 64) + s
            n //= 26

    print(s)


printString(52)