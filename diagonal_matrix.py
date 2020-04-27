# def valid(i, j, R, C):
#     if (i < 0 or j < 0 or i >= R or j >= C):
#         return False
#     return True
#
# def diagonal_matrix(matrix):
#     R = len(matrix)
#     C = len(matrix[0])
#     res = []
#     for k in range(0, R):
#         sub = []
#         sub.append(matrix[0][k])
#         i=1
#         j=k-1
#         while(valid(i, j, R, C)):
#             sub.append(matrix[i][j])
#             i+=1
#             j-=1
#         res.append(sub)
#     for k in range(1, C):
#         sub = []
#         sub.append(matrix[k][C-1])
#         i = k+1
#         j = C-2
#         while (valid(i, j, R, C)):
#             sub.append(matrix[i][j])
#             i += 1
#             j -= 1
#         res.append(sub)
#     print(res)

def valid(i, j, R, C):
    if (i < 0 or j < 0 or i >= R or j >= C):
        return False
    return True

def diagonal_matrix(matrix):
    R = len(matrix)
    C = len(matrix[0])
    res = []
    for k in range(0, R):
        res.append(matrix[0][k])
        i=1
        j=k-1
        while(valid(i, j, R, C)):
            res.append(matrix[i][j])
            i+=1
            j-=1
    for k in range(1, C):
        res.append(matrix[k][C-1])
        i = k+1
        j = C-2
        while (valid(i, j, R, C)):
            res.append(matrix[i][j])
            i += 1
            j -= 1
    print(" ".join(str(e) for e in res))



#diagonal_matrix([[1,2], [3,4]])
diagonal_matrix([[1,2,3],[4,5,6],[7,8,9]])
