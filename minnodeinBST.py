class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def mininBST(root):
    current = root
    while current.left:
        current = current.left
    return current



root = Node(5)
root.left = Node(3)
root.left.left = Node(2)
root.left.right = Node(4)
root.right = Node(6)

data = mininBST(root)
print(data.value)

