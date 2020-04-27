def reverse(head, k):
    # Code here
    if head is None:
        return

    head_1 = head
    head_2 = None
    while (head_1.next):
        if head_1.data == k:
            head_2 = head_1.next
            head_1.next = None
            break
        else:
            head_1 = head_1.next

    if head_2 is None:
        return head

    prev_1 = None
    current_1 = head
    while (head_2 and current_1):
        next = current_1.next
        current_1.next = prev_1
        prev_1 = current_1
        current_1 = next
    head_1 = prev_1

    prev_2 = None
    current_2 = head_2
    while (head_2 and current_2):
        next = current_2.next
        current_2.next = prev_2
        prev_2 = current_2
        current_2 = next
    head_2 = prev_2

    temp = head_1
    while(head_2 and temp.next):
        temp = temp.next
    temp.next = head_2

    return head_1
