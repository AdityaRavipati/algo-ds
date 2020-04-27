# User function Template for python3
from collections import defaultdict

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head = None

    def findIntersection(self, h1, h2):
        get_dict = self.make_dict(h1, h2)
        intersection_res = self.get_intersection(get_dict)
        result = self.mergeSort(intersection_res)
        return result

    def mergeSort(self, h):
        if h == None or h.next == None:
            return h
        mid = self.get_mid(h)
        next_to_mid = mid.next
        mid.next = None
        left = self.mergeSort(h)
        right = self.mergeSort(next_to_mid)
        result = self.sorted_merge(left, right)
        return result

    def sorted_merge(self, a, b):
        result = None
        if a is None:
            return b
        if b is None:
            return a
        if a.data < b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)
        return result

    def get_mid(self, head):
        if head == None:
            return head
        slow_p = head
        fast_p = head
        while (fast_p.next and fast_p.next.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
        return slow_p

    def make_dict(self, h1, h2):
        import pdb; pdb.set_trace()
        if h1 is None or h2 is None:
            return
        new_dict = defaultdict(lambda: 0)
        while(h1 or h2):
            if h1:
                new_dict[h1.data] = new_dict[h1.data] + 1
                h1 = h1.next
            if h2:
                new_dict[h2.data] = new_dict[h2.data] + 1
                h2 = h2.next
        return new_dict

    def get_intersection(self, new_dict):
        result = None
        if new_dict:
            for key, value in new_dict.items():
                if value > 1:
                    result = self.push(result, key)
        return result

    def push(self, head, new_data):
        import pdb; pdb.set_trace()
        new_node = Node(new_data)
        new_node.next = head
        head = new_node
        return head

    def printList(self, head):
        while head:
            print head.data
            head = head.next


if __name__ == '__main__':
    ll = LinkedList()
    arr1 = [34, 56, 77, 12, 99, 80]
    arr2 = [56, 12, 38, 96, 75, 48]
    head = None
    ll1 = LinkedList()
    for data in arr1:
        ll1.push(head, data)

    ll2 = LinkedList()
    for data in arr2:
        ll2.push(head, data)

    # Apply intersection
    ll.printList(ll1.head)
    ll.printList(ll2.head)

    res_head = ll.findIntersection(ll1.head, ll2.head)
    print ("Sorted Linked List is:")
    ll.printList(res_head)