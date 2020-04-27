# Pivot Index
def pivot_index(A):
    m = len(A)
    pivot = []
    for i in range(0, m):
        for j in range(i+1, m):
            if A[i]==A[j]:
                pivot.append(i)
                break
    if len(pivot)==0 or len(pivot)==(m-1):
        return -1
    return pivot[0]

# A=[1,7,3,6,7,6]
# print(pivot_index(A))

#############################################

# Largest Number At Least Twice of Others
def twiceofothernums(nums):
    m=len(nums)
    index = []
    count = 0
    for i in range(0,m):
        for j in range(0, m):
            if (i!=j) and (nums[i] >= 2 * nums[j]):
                count+=1
            if count == m-1:
                index.append(i)
        count=0
    if len(index)==0:
        return -1
    return index[0]

# A=[3,6,1,0]
# nums = [0,0,0,1]
# print(twiceofothernums(nums))

#######################################################

# Plus One
def plusone(digits):
    m=len(digits)
    s = [str(i) for i in digits]
    res = int("".join(s))
    k = 1
    while(res & k):
        res = res ^ k
        k <<= 1
    res = res ^ k
    res = [int(x) for x in str(res)]
    return res

# digits = [9,9]
# #digits = [4, 3, 2, 9]
# print(plusone(digits))

#######################################################

# Pascal's Triangle
def pascalTriangle(n):
    import pdb;pdb.set_trace()
    matrix = []
    space = n
    for row in [[] * n] * n:
        matrix.append((" "*space)+str(row))
        space = (n-1)
    for line in range(1,n+1):
        c=1
        for i in range(1,line+1):
            # print(" " * space)
            # matrix[0].append(c)
            c = int(c*((line-i)/i))

    # return matrix


# print(pascalTriangle(5))


#######################################################

# def printPascal(n):
#     import pdb; pdb.set_trace()
#     for line in range(1, n + 1):
#         C = 1;  # used to represent C(line, i)
#         for i in range(1, line + 1):
#             # The first value in a
#             # line is always 1
#             print(C);
#             C = int(C * (line - i) / i);
#         print("");
#
#     # Driver code
#
#
# n = 5;
# printPascal(n);

#######################################################
# def searchRange(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: List[int]
#     """
#     total = len(nums) - 1
#     st = []
#     end = []
#     res = []
#     if total == 0:
#         if target in nums:
#             return [0,0]
#         else:
#             return [-1,-1]
#     import pdb;
#     pdb.set_trace()
#     for i in range(0, total+1):
#         if nums[i] == target:
#             st.append(i)
#         if nums[total - i] == target:
#             end.append(total - i)
#
#     if st and end:
#         res.append(st[0]), res.append(end[0])
#         return res
#     else:
#         return [-1, -1]
#
#
#
#
# print(searchRange([1,3], 1))

#######################################################

# def isPerfectSquare(num):
#     """
#     :type num: int
#     :rtype: bool
#     """
#     import pdb; pdb.set_trace()
#     st = 1
#     end = num
#     while (st < end):
#         mid = (st + end) / 2
#         if mid * mid == num:
#             return True
#         elif mid * mid < num:
#             st = mid + 1
#         elif mid * mid > num:
#             end = mid
#     return False
#
# print(isPerfectSquare(104976))

#######################################################

def findMin(nums):
    import pdb; pdb.set_trace()
    if nums == []:
        return -1
    elif len(nums)==1:
        return nums[0]
    elif len(nums)==2:
        return min(nums)
    res = []
    st = 0
    end = len(nums)
    mid = (st+end)/2
    for i in range(1, mid):
        if nums[i]>nums[0]:
            pass
        else:
            return nums[i]
    for i in range(mid, end):
        if nums[i]<nums[0]:
            res.append(nums[i])
        else:
            pass
    return min(res)



# print(findMin([4,5,6,7,0,1,2]))

#######################################################

def search(A, B):
    import pdb; pdb.set_trace()
    st = 0
    end = len(A)
    while(True):
        mid = (st + end) / 2
        if A[mid] > B:
            end = mid
        elif A[mid] < B:
            st = mid
        elif A[mid] == B:
            return mid

# A = [4, 5, 6, 7, 0, 1, 2, 3]
# print(search(A, 7))


#######################################################

# class Node:
#     # A utility function to create a new node
#     def __init__(self, key):
#         self.val = key
#         self.left = None
#         self.right = None
#
#
# # Iterative Method to print the height of binary tree
# def printLevelOrder(root):
#     if root is None:
#         return
#     stack = []
#     res = []
#     stack.append(root)
#     while stack:
#         count = len(stack)
#         while (count > 0):
#             node = stack.pop()
#             res.append([node.val])
#             if node.right:
#                 stack.append(node.right)
#             if node.left:
#                 stack.append(node.left)
#     return res

class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


# Iterative method to do level order traversal
# line by line
# def printLevelOrder(root):
#     # Base case
#     if root is None:
#         return
#     # Create an empty queue for level order traversal
#     q = []
#     res = []
#     tmp = []
#     # Enqueue root and initialize height
#     q.append(root)
#
#     while q:
#
#         # nodeCount (queue size) indicates number
#         # of nodes at current lelvel.
#         count = len(q)
#
#         # Dequeue all nodes of current level and
#         # Enqueue all nodes of next level
#         while count > 0:
#             temp = q.pop(0)
#             tmp.append(temp.val)
#             if temp.left:
#                 q.append(temp.left)
#             if temp.right:
#                 q.append(temp.right)
#             count -= 1
#
#         import pdb;
#         pdb.set_trace()
#         res.append(tmp[:]),
#
#     return res

def maxDepth(root):
    import pdb; pdb.set_trace()
    if root is None:
        return
    else:
        lDepth = maxDepth(root.left)
        rDepth = maxDepth(root.right)

        if (lDepth > rDepth):
            return lDepth + 1
        else:
            return rDepth + 1


# Driver Program to test above function
root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.left.left = Node(4)
root.left.right = Node(6)
root.right.left = Node(15)
root.right.right = Node(7)
print(maxDepth(root))
























