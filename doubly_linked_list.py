class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_dll(self, new_node):
        new_node.prev = None
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
        return self.head

    def print_dll(self, node):
        while(node):
            print node.data
            node = node.next

    def inser_end_dll(self, data):
        new_node = Node(data)
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def rev_dll(self):
        temp = None
        current = self.head
        while(current):
            temp = current.prev
            new_head = llist.insert_dll(temp.data)
            temp = temp.next
        self.head = new_head
        return self.head






llist = DoublyLinkedList()
llist.insert_dll(Node(1))
llist.insert_dll(Node(2))
llist.insert_dll(Node(3))
llist.insert_dll(Node(4))
llist.insert_dll(Node(5))
llist.insert_dll(Node(6))
# llist.print_dll(llist.head)
head = llist.rev_dll()
llist.print_dll(llist.head)



