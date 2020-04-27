def min_plat(arr, dep):
    n = len(arr)
    arr.sort()
    dep.sort()

    res = 0
    plat = 1
    i = 1
    j = 0
    while(i<n and j<n):
        if arr[i]<dep[j]:
            plat+=1
            i+=1
            if plat>res:
                res = plat
        else:
            plat-=1
            j+=1
    print(res)


min_plat([900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000])
