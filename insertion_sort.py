def insertion_sort(arr):
    n = len(arr)
    i = 1
    import pdb; pdb.set_trace()
    while(i<n):
        for j in range(i):
            if arr[i]<arr[j]:
                arr[j], arr[i] = arr[i], arr[j]
        i+=1
    print(arr)


insertion_sort([4, 3, 2, 10, 12, 1, 5, 6])