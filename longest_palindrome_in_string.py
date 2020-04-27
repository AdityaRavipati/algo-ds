def longest_palindrome(s):
    l = []
    lastlen = 0
    newlen = 0
    import pdb; pdb.set_trace()
    for i in range(0, len(s)):
        for j in range(i + 1, len(s) + 1):
            p = s[i:j]
            pp = p[::-1]
            if (p == pp):
                newlen = len(p)
            if newlen > lastlen:
                l.append(p)
                lastlen = newlen
    print(l[-1])

longest_palindrome('aaaabbaa')