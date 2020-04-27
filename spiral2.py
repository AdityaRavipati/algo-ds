def generateMatrix(A):

    size = int(A)

    if size <= 0:
        return []
    # matrix = [row[:] for row in [[]*size] * size]
    matrix = [row[:] for row in [[0] * size] * size]
    import pdb; pdb.set_trace()
    k=0
    l=0
    m=size
    n=size
    current = 1

    while (True):
        if current > size * size:
            break
        for i in range(l,n):
            matrix[k][i] = current
            current+=1
        k+=1
        for i in range(k,m):
            matrix[i][n-1] = current
            current+=1
        n-=1
        for i in range(n-1,l-1,-1):
            matrix[m-1][i] = current
            current+=1
        m-=1
        for i in range(m-1, k-1, -1):
            matrix[i][l]=current
            current+=1
        l+=1
    return matrix


print(generateMatrix(5))
