# Check whether the array is wave array or not
# def wave_array(A):
#     for i in range(1, len(A)-1, 2):
#         if (A[i] > A[i+1]) and (A[1] > A[i-1]):
#             pass
#         elif (A[i] < A[i+1]) and (A[1] < A[i-1]):
#             pass
#         else:
#             return False
#     return True


def sort_wave_array(A):
    A.sort()
    m = len(A)
    for i in range(0, m - 1, 2):
        A[i], A[i + 1] = A[i + 1], A[i]
    return A




#A = [5, 1, 7, 3, 8, 2, 6]
A = [1, 2, 3, 4, 5, 6, 7]
#A = [1, 5, 3, 7, 2, 8, 6]
print(sort_wave_array(A))
