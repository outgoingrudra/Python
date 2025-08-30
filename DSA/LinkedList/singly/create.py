class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    def show(self):
        t = self.head
        while t:
            print(t.val, end=" ")
            t = t.next

l = LinkedList()
l.add(5)
l.add(10)
l.add(15)
l.show()
