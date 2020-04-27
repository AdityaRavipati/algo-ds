def spiralPrint(a):
    if len(a) == 0:
        return []
    k =0
    l=0
    m = len(a)
    n = len(a[0])
    res = []
    while(k<m and l<n):
        for i in range(l,n):
            res.append(a[k][i])
        k+=1

        for i in range(k,m):
            res.append(a[i][n-1])
        n-=1

        if(k<m):
            for i in range(n-1, l-1, -1):
                res.append(a[m-1][i])
            m-=1

        if(l<n):
            for i in range(m-1, k-1, -1):
                res.append(a[i][l])
            l+=1
    return res

a = [[1,2,3],
     [4,5,6],
     [7,8,9]]

print(spiralPrint(a))