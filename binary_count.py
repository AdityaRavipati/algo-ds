class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


count = 0
hash_t = set()
x = 10


def count_pairs_w_sum(root):
    global count
    if root:
        if root.value in hash_t:
            count += 1
        else:
            hash_t.add(x - root.value)

        count_pairs_w_sum(root.left)
        count_pairs_w_sum(root.right)


if __name__ == '__main__':
    root = Node(5)

    root.left = Node(3)
    root.right = Node(7)

    root.left.left = Node(2)
    root.left.right = Node(4)

    root.right.left = Node(6)
    root.right.right = Node(8)

    count_pairs_w_sum(root)

    print count
