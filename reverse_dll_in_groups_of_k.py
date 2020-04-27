class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def push(head, data):
    new_node = Node(data)
    new_node.next  = head
    if head != None:
        head.prev = new_node
    head = new_node
    return head

def revListInGroupOfGivenSize(head, k):
    current = head
    temp = None
    count = 0

    while(current and count<k):
        temp = current.prev
        current.prev = current.next
        current.next = temp
        current = current.prev
        count+=1

    if temp:
        temp.next = revListInGroupOfGivenSize(temp, k)
        temp.next.prev = head
    return current.prev


def printList(head):
    while (head != None):
        print(head.data,)
        head = head.next


head = None
head = push(head, 2)
head = push(head, 4)
head = push(head, 8)
head = push(head, 10)
k = 2
head = revListInGroupOfGivenSize(head, k)
printList(head)

