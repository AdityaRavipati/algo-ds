def quick_sort(arr, start, end):
    if start<end:
        pIndex = partition(arr, start, end)
        quick_sort(arr, start, pIndex-1)
        quick_sort(arr, pIndex+1, end)
    return arr

def partition(arr, start, end):
    import pdb; pdb.set_trace()
    pIndex = start-1
    pivot = arr[end]
    for i in range(start, end):
        if arr[i] < pivot:
            pIndex += 1
            arr[pIndex], arr[i] = arr[i], arr[pIndex]
    arr[pIndex+1], arr[end] = arr[end], arr[pIndex+1]
    return pIndex+1


#print(quick_sort([10, 80, 30, 90, 40, 50, 70], 0, 6))
print(quick_sort([10, 1, 21, 5, 9, 2, 36], 0, 6))