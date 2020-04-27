class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def inorder(root, a, b):
    if root:
        if a < root.value:
            inorder(root.left, a, b)
        if root.value >=a and root.value <=b:
            print(root.value),
        if b > root.value:
            inorder(root.right, a, b)

root = Node(25)
root.left = Node(15)
root.right = Node(50)
root.left.left = Node(10)
root.left.right = Node(22)
root.left.left.left = Node(4)
root.left.left.right = Node(12)
root.left.right.left = Node(18)
root.left.right.right = Node(24)
root.right.left = Node(35)
root.right.right = Node(70)
root.right.left.left = Node(31)
root.right.left.right = Node(44)
root.right.right.left = Node(66)
root.right.right.right = Node(90)

inorder(root, 31, 90)




