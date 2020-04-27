def is_safe(i, j, R, C):
    if (i >= 0 and j >= 0 and i < R and j < C):
        return True
    return False


def test(dim, l):
    R = dim[0]
    C = dim[1]
    m = []
    while (l != []):
        m.append(l[:5])
        l = l[5:]
    import pdb; pdb.set_trace()
    rotten = 2
    change = False
    while (True):
        for i in range(0, R):
            for j in range(0, C):
                if m[i][j] == rotten:
                    if is_safe(i + 1, j, R, C) and m[i + 1][j] == 1:
                        m[i + 1][j] = m[i][j] + 1
                        change = True
                    if is_safe(i, j + 1, R, C) and m[i][j + 1] == 1:
                        m[i][j + 1] = m[i][j] + 1
                        change = True
                    if is_safe(i - 1, j, R, C) and m[i - 1][j] == 1:
                        m[i - 1][j] = m[i][j] + 1
                        change = True
                    if is_safe(i, j - 1, R, C) and m[i][j - 1] == 1:
                        m[i][j - 1] = m[i][j] + 1
                        change = True
        if not change:
            break
        change = False
        rotten += 1

    for i in range(0, R):
        for j in range(0, C):
            if m[i][j] == 1:
                return(-1)

    return(rotten - 2)


print(test([3, 5], [2, 1, 0, 2, 1, 1, 0, 1, 2, 1, 1, 0, 0, 2, 1]))