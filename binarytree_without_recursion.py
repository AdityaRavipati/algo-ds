class Node(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def inorder(root):    # <left, node, right>
    s = []
    current = root
    while True:
        if (current is not None):
            s.append(current)
            current = current.left
        elif s:
            current = s.pop()
            print(current.value),
            current = current.right
        else:
            exit(0)

def preorder(root):
    s = []
    s.append(root)
    while s:
        current = s.pop()
        print(current.value),

        if current.right:
            s.append(current.right)
        if current.left:
            s.append(current.left)



# root = Node(10)
# root.left = Node(11)
# root.left.left = Node(7)
# root.right = Node(9)
# root.right.left = Node(15)
# root.right.right = Node(8)

root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)

# preorder(root)

############################################

# Breadth First Search(Level order Traversal)

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


# Iterative Method to print the height of binary tree
def printLevelOrder(root):
    # Base Case
    if root is None:
        return

    # Create an empty queue for level order traversal
    queue = []

    # Enqueue Root and initialize height
    queue.append(root)

    while (len(queue) > 0):
        # Print front of queue and remove it from queue
        print queue[0].data,
        node = queue.pop(0)

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)

        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)

        # Driver Program to test above function


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print "Level Order Traversal of binary tree is -"
printLevelOrder(root)
