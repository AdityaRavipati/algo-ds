def min_operations(n):
    i = n
    j = 0
    while(i>0):
        if i%2 == 0:
            i = i/2
        elif i%2 != 0:
            i-=1
        j+=1
    return j




print(min_operations(8))