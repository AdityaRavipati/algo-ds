class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list():
    def __init__(self):
        self.last = None

    def addToEmpty(self, data):
        if self.last != None:
            return self.last

        temp = Node(data)
        self.last = temp

        self.last.next = self.last
        return self.last

    def addBegin(self, data):
        temp = Node(data)
        temp.next = self.last.next
        self.last.next = temp
        return self.last



