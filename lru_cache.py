class Node(object):
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LRUCache(object):
    def __init__(self, capacity):
        self.cap = int(capacity)
        self.hash = {}
        self.count = 0
        self.head = None

    def insert(self, new_node):
        new_node.next = self.head
        new_node.prev = None
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def delete(self, del_node=None, last_node=False):
        if last_node:
            current = self.head
            while(current.next):
                current = current.next
            val = current.data
            current.prev.next = None
            return val
        else:
            if self.head == del_node:
                self.head = del_node.next
            if del_node.next is not None:
                del_node.next.prev = del_node.prev
            if del_node.prev is not None:
                del_node.prev.next = del_node.next

    def set(self, key, value):
        if key in self.hash.keys():
            updated_node = Node(value)
            self.delete(updated_node)
            self.insert(updated_node)
        else:
            self.hash[key] = value
            new_node = Node(value)
            if self.count < self.cap:
                self.count+=1
                self.insert(new_node)
            else:
                data = self.delete(last_node=True)
                for key, val in self.hash.items():
                    if val == data:
                        del self.hash[key]
                self.insert(new_node)

    def get(self, key):
        if key in self.hash.keys():
            val = self.hash[key]
            print val
            self.delete(Node(val))
            self.insert(Node(val))
        else:
            print -1


lc = LRUCache(2)
lc.set(1, 10)
lc.set(2, 20)
lc.get(1)
lc.set(3, 30)
lc.get(2)
lc.set(4, 30)
lc.get(1)
lc.get(3)
lc.get(4)


