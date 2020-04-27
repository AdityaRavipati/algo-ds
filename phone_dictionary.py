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

def dictionary(str1, str2):
    for i in range(len(str2)):
        res_match = []
        for ele in str1:
            if str2[:i+1] == ele[:i+1]:
                res_match.append(ele)
        if res_match == []:
            print(0)
        else:
            res_match = list(set(res_match))
            if len(res_match) == 1:
                res1 = " ".join(str(e) for e in res_match)
                print res1
            else:
                res = mergeSort(res_match)
                res1 = " ".join(str(e) for e in res)
                print(res1)


dictionary(['geekksgeeks', 'geeksquiz'], 'geekks')
#dictionary(['geeikistest', 'geeksforgeeks', 'geeksfortest'], 'geeips')