def generateMatrix(A):

    size = int(A+(A-1))

    if size <= 0:
        return []

    matrix = [row[:] for row in [[0] * size] * size]

    k=0
    l=0
    m=size
    n=size
    current = A

    while(current >= 1):
        for i in range(l,n):
            matrix[k][i] = current

        k+=1
        for i in range(k,m):
            matrix[i][n-1] = current

        n-=1
        for i in range(n-1,l-1,-1):
            matrix[m-1][i] = current

        m-=1
        for i in range(m-1, k-1, -1):
            matrix[i][l]=current

        l+=1
        current-=1
    return matrix


print(generateMatrix(5))
