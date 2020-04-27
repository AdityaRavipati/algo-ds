# User function Template for python3
from collections import defaultdict


def union(head1, head2):
    d = make_dict(head1, head2)
    uni_res = make_union(d)
    sorted_ll = merge_sort(uni_res)
    return sorted_ll


def merge_sort(h4):
    if h4 is None or h4.next is None:
        return h4
    mid = mid_sort(h4)
    midafternext = mid.next
    mid.next = None
    left = merge_sort(h4)
    right = merge_sort(midafternext)
    sorted_ll = merge_left_right(left, right)
    return sorted_ll


def merge_left_right(a, b):
    merge_data = None
    if a is None:
        return b
    if b is None:
        return a
    if a.data < b.data:
        merge_data = a
        merge_data.next = merge_left_right(a.next, b)
    else:
        merge_data = b
        merge_data.next = merge_left_right(a, b.next)
    return merge_data


def mid_sort(h5):
    if h5 is None:
        return head
    slow_p = h5
    fast_p = h5
    while (fast_p.next and fast_p.next.next):
        slow_p = slow_p.next
        fast_p = fast_p.next.next
    return slow_p


def make_dict(h1, h2):
    if h1 is None or h2 is None:
        return
    d = defaultdict(lambda: 0)
    while (h1 or h2):
        if h1:
            d[h1.data] = d[h1.data] + 1
            h1 = h1.next
        if h2:
            d[h2.data] = d[h2.data] + 1
            h2 = h2.next
    return d


def make_union(d):
    res = None
    for key, value in d.items():
        res = push(res, key)
    return res


def push(h3, data):
    new_node = Node(data)
    new_node.next = h3
    h3 = new_node
    return h3