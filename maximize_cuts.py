def test(arr):
    #import pdb; pdb.set_trace()
    res1 = 0
    for i in range(len(arr)):
        if arr[0]>arr[len(arr)-1]:
            res = arr.pop(0)
        else:
            res = arr.pop(len(arr)-1)
        res1 = res1 + res
    print res1



test([5, 3, 7, 10])
#test([4993, 4883, 8894, 7241, 1476, 8226, 1207, 5674, 6967, 6766, 8371, 1467, 3169, 2228, 297, 288, 4300, 4194, 4689,
#      1155, 3934, 5209, 4342, 2916, 2808, 2067, 5467, 8012, 1855, 1894, 2684, 9266, 5705, 3578, 4775, 578, 1546, 216, 395, 7883, 720, 9476])