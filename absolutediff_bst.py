# minimum absolute difference in a BST
class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


# setting target to positive infinity
target = 10000000


def absolute_diff(root, target):
    if root is None:
        return target

    # first compare the root with left and right subtree root values
    if root.left is not None:
        left = root.value - root.left.value
        target = min(left, target)
    elif root.right is not None:
        right = root.right.value - root.value
        target = min(target, right)

    # repeat the same same for left subtree and right subtree
    a = absolute_diff(root.left, target)
    b = absolute_diff(root.right, target)
    return min(a,b)

#         5
#      /     \
#     3      7
#    / \    / \
#   2  4   6  9


# Driver code

root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(9)


# root = Node(25)
# root.left = Node(15)
# root.right = Node(50)
# root.left.left = Node(10)
# root.left.right = Node(22)
# root.left.left.left = Node(4)
# root.left.left.right = Node(12)
# root.left.right.left = Node(18)
# root.left.right.right = Node(24)
# root.right.left = Node(35)
# root.right.right = Node(70)
# root.right.left.left = Node(31)
# root.right.left.right = Node(44)
# root.right.right.left = Node(66)
# root.right.right.right = Node(90)

print(absolute_diff(root, target))



