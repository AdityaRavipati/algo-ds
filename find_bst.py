class Node(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def check_bst(root):
    current = root
    s = []
    prev = -1234152
    while(True):
        if current:
            s.append(current)
            current = current.left
        elif s:
            current = s.pop()
            if current.data < prev:
                return False
            prev = current.data
            current = current.right
        else:
            return True


root = Node(4)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right = Node(5)

print(check_bst(root))

