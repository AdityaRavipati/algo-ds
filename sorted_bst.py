class Node(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

#################################################################################


def sortedlisttoBST(arr):
    if not arr:
        return None

    mid = (len(arr))/2
    root = Node(arr[mid])
    root.left = sortedlisttoBST(arr[:mid])
    root.right = sortedlisttoBST(arr[mid+1:])
    return root

#################################################################################


def serachinBST(root, value):
    if root == None or root.value == value:
        return None

    if value > root.value:
        return serachinBST(root.right, value)
    return serachinBST(root.left, value)

#################################################################################


def insertinBST(root, node):
    if root is None:
        root = node
    else:
        if node.value > root.value:
            if root.right is None:
                root.right = node
            else:
                insertinBST(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insertinBST(root.left, node)

#################################################################################


def deleteinBST1(root, node):   # this will delete children along with root, incase if the root has 2 children
    if root is None and root.value == node:
        root.value = None
    else:
        if node.value > root.value:
            if root.right.value == node.value:
                root.right = None
            else:
                deleteinBST1(root.right, node)
        else:
            if root.left.value == node.value:
                root.left = None
            else:
                deleteinBST1(root.left, node)

#################################################################################


def deleteinBST2(root, node):      # this will only delete root and replace children accordingly
    if root is None:
        return root  #return root as it is

#         50
#      /     \
#     30     70
#    / \    / \
#   20 40  60 80

# Algorithm to replace children with root:
#    If root(that has 2 children) is selected to delete from the BST,
#    then obviously least value child from the right subtree need to be replaced with root.
#    For example: 50 is selected to delete, then to make the BST stable we have to replace 50(root) with least valued
#    child(60) from right subtree.

    # If the node to be deleted is smaller than the root's value then it lies in left subtree
    if node.value < root.value:
        root.left = deleteinBST2(root.left, node)
    # If the node to be delete is greater than the root's value then it lies in right subtree
    elif node.value > root.value:
        root.right = deleteinBST2(root.right, node)
    else:
        #import pdb; pdb.set_trace()
        if root.left is None:       # this condition is for node that has one or no children
            temp = root.right
            #root = None
            return temp    # this return value of temp will be returned to the calling function which is in either line number '88' or '91'
        elif root.right is None:    # this condition is for node that has one or no children
            temp = root.left
            #root = None
            return temp   # this return value of temp will be returned to the calling function which is in either line number '88' or '91'
        # this condition is for the node that has 2 children
        temp = minvalueNode(root.right)   # gets the least valued child
        root.value = temp.value   # deleting the root value (50) and replacing with least valued child from right subtree (60)
        root.right = deleteinBST2(root.right, temp)   # now as the least valued child from right subtree (60) is left undeleted.
                                                      # we have to remove it. As we have already made it as a root.
    return root

#################################################################################


def minvalueNode(node):
    current = node
    while(current.left is not None):  # go until we reach the last leaf of the left subtree
        current = current.left
    return current

#################################################################################


def preorderBST(root):  # <node, left, right>
    if root:
        print(root.value),
        preorderBST(root.left)
        preorderBST(root.right)

#################################################################################


def inorderBST(root):    # <left, node, right>
    if root:
        inorderBST(root.left)
        print(root.value),
        inorderBST(root.right)

#################################################################################


def postorderBST(root):    # <left, right, node>
    if root:
        postorderBST(root.left)
        postorderBST(root.right)
        print(root.value),

#################################################################################

# Driver code

#arr = [4, 10, 12, 15, 18, 22, 24, 25, 31, 35, 44, 50, 66, 70, 90]
arr = [20, 30, 40, 50, 60, 70, 80]
root = sortedlisttoBST(arr)
# serachinBST(root, 40)
# insertinBST(root, Node(35))
temp =  deleteinBST2(root, Node(30))
print('\n-------------------------------------------')
inorderBST(temp)
# print('\n-------------------------------------------')
# preorderBST(root)
# print('\n-------------------------------------------')
# postorderBST(root)
