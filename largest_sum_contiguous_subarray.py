# Approach 1
# def max_sub_array(arr):
#     max_sum_here = 0
#     max_so_far = 0
#     for i in range(0, len(arr)):
#         max_sum_here += arr[i]
#         if max_sum_here > max_so_far:
#             max_so_far = max_sum_here
#         if max_sum_here < 0:
#             max_sum_here = 0
#
#     return max_so_far


# Algorithm to handle all negative numbers along with negative and positive
def maxSubArraySum(a, size):
    max_so_far = a[0]
    curr_max = a[0]

    for i in range(1, size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far, curr_max)

    return max_so_far


a = [-5, -10, -2, -7, -15]
# print"Maximum contiguous sum is" , maxSubArraySum(a,len(a))



def rotLeft(a, d):
    n = len(a)
    res = []
    for i in range(d, n):
        res.append(a[i])
    for i in range(0, d):
        res.append(a[i])
    listToStr = "".join(map(str, res))
    # res.append(a[d : n]+a[:d])
    # print res
    #listToStr = ' '.join([str(ele) for ele in res])
    print listToStr




#rotLeft([1,2,3,4,5], 4)
rotLeft([33, 47, 70, 37, 8, 53, 13, 93, 71, 72, 51, 100, 60, 87, 97], 13)
