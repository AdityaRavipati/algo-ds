def numberOfPaths(A, B):
    dp = [1 for i in range(B)]
    import pdb; pdb.set_trace()
    for i in range(A - 1):
        for j in range(1, B):
            dp[j] += dp[j - 1]
    return dp[B - 1]


A = 3
B = 3
print(numberOfPaths(A, B))
