class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def print_nodes(self):
        current = self.head
        while(current):
            print current.data
            current = current.next

    def insert(self, str_val):
        new_node = Node(str_val)
        new_node.next = self.head
        self.head = new_node

    def deleteNode(self, position):
        if self.head == None:
            return

        temp = self.head
        if position == 0:
            self.head = temp.next
            temp = None
            return

        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        if temp is None:
            return
        if temp.next is None:
            return
        next = temp.next.next
        temp.next = None

        temp.next = next

    def get_len(self):
        current = self.head
        i = 0
        while(current):
            i+=1
            current = current.next
        return i

    def compare_llist_ele(self, new_str):
        current = self.head
        l = len(new_str)
        i = 0

        while(current and (i<l)):
            if new_str[i] == current.data:
                current = current.next
                i+=1
            else:
                break

        ll_len = self.get_len()
        while(i < ll_len):
            self.deleteNode(i)
            ll_len = self.get_len()

    def LCP(self, arr):
        for i in range(len(arr[0])-1, -1, -1):
            self.insert(arr[0][i])

        for i in range(1, len(arr)):
            self.compare_llist_ele(arr[i])
        self.print_nodes()

ll = LinkedList()
ll.LCP(["apple", "ape", "april"])