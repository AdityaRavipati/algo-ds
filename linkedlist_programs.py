class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def print_fun(self):
        temp = self.head
        while(temp):
            print temp.data,
            temp = temp.next

    def lpush_beggining(self, new_node_val):
        new_node = Node(new_node_val)
        new_node.next = self.head
        self.head = new_node

    def lpush_mid(self, new_node_val, prev_node_val):
        new_node = Node(new_node_val)
        new_node.next = prev_node_val.next
        prev_node_val.next = new_node

    def move_to_front(self, new_node):
        new_node = Node(new_node)
        sec_last = None

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        if not temp or not temp.next:
            return

        while temp and temp.next:
            sec_last = temp
            temp = temp.next

        sec_last.next = None
        temp.next = self.head
        self.head = temp

    def reverse_llist(self):
        current = self.head
        prev = None
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def ldelete(self, key):
        temp = self.head
        prev = None
        while(temp):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        prev.next = temp.next
        temp = None

    def mid_of_llist(self):
        import pdb; pdb.set_trace()
        mid = self.head
        counter = 0
        temp = self.head
        while(temp):
            if (counter & 1):
                mid = mid.next
            counter+=1
            temp = temp.next

        if mid is not None:
            print mid.data

    def llist_loop(self):
        slow_link = self.head
        fast_link = self.head
        while(slow_link and fast_link and fast_link.next):
            if fast_link == slow_link:
                print "loop detected at {0}".format(str(fast_link.data))
                return
            if fast_link.next.next:
                fast_link = fast_link.next.next
            slow_link = slow_link.next

    def llist_lloop_hash_map(self):
        import pdb; pdb.set_trace()
        s = set()
        temp = self.head
        while(temp):
            if(temp in s):
                print "loop detected"
                return
            s.add(temp)
            temp = temp.next

    def mid(self):
        if self.head is None:
            return -1

        count = 0
        temp = self.head
        while(temp):
            count += 1
            temp = temp.next

        mid = count/2

        temp = self.head
        for i in range(0, count):
            if i == mid:
                print temp.data
            temp = temp.next





if __name__ == '__main__':
    llist = LinkedList()
    llist.lpush_beggining(6)
    llist.lpush_beggining(5)
    llist.lpush_beggining(4)
    llist.lpush_beggining(3)
    llist.lpush_beggining(2)
    llist.lpush_beggining(1)
    llist.mid()
    # llist.head = Node(2)
    # second = Node(3)
    # third = Node(4)
    # fourth = Node(5)
    # fifth = Node(2)
    # llist.head.next = second
    # second.next = third
    # third.next = fourth
    # fourth.next = fifth
    # llist.lpush_beggining(1)
    #llist.lpush_mid(2, Node(1))
    #llist.print_fun()
    #llist.ldelete(3)
    #llist.print_fun()
    #print('\n')
    #llist.reverse_llist()
    #llist.print_fun()
    #print('\n')
    #llist.mid_of_llist()
    # llist.llist_loop()
    # llist.llist_lloop_hash_map()
