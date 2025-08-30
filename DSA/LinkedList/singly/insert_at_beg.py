class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertbeg(self, x):
        n = Node(x)
        n.next = self.head
        self.head = n

    def display(self):
        t = self.head
        while t:
            print(t.val, end=" ")
            t = t.next

l = LinkedList()
l.insertbeg(30)
l.insertbeg(20)
l.insertbeg(10)
l.display()
