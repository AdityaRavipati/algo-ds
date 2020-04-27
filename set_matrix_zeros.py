def set_matrix_zeros(A):
    C = len(A[0])
    R = len(A)
    row = [1] * R
    col = [1] * C

    for i in range(0, R):
        for j in range(0, C):
            if (A[i][j] == 0):
                row[i] = 0
                col[j] = 0

    for i in range(0, R):
        for j in range(0, C):
            if row[i] == 0 or col[j] == 0:
                A[i][j] = 0

    for l in A:
        a = " ".join(str(i) for i in l)
        print a



A = [[1, 0, 1],
     [1, 1, 1],
     [1, 0, 1]]
set_matrix_zeros(A)