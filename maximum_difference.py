def max_diff(arr):
    #n = int(input())
    #arr = list(map(int, input().strip().split()))
    n = len(arr)
    min_val = arr[0]
    max_val = arr[1] - arr[0]
    for i in range(1, n):
        if arr[i] - min_val > max_val:
            max_val = arr[i] - min_val
        if arr[i] < min_val:
            min_val = arr[i]
    print max_val

max_diff([80, 2, 6, 3, 100])