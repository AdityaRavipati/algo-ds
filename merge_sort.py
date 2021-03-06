def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = 0
        j = 0
        k = 0
        while(i<len(L) and j<len(R)):
            if L[i]<R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1

        while(i<len(L)):
            arr[k] = L[i]
            i += 1
            k+=1
        while(j<len(R)):
            arr[k] = R[j]
            j += 1
            k+=1
        return arr


print(mergeSort(['geekksgeeks']))
#print(mergeSort(['geekksgeeks', 'geeksquiz', 'geekpgeeks', 'geekakgeeks', 'geekbgeeks']))