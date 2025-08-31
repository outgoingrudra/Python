class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def insert_pos(self, d, pos):
        new = Node(d)
        if pos == 0:
            new.next = self.head
            self.head = new
            return
        temp = self.head
        for _ in range(pos-1):
            if temp is None: return
            temp = temp.next
        new.next = temp.next
        temp.next = new

    def show(self):
        t = self.head
        while t:
            print(t.data, end=" ")
            t = t.next

l = SLL()
l.insert_pos(10,0)
l.insert_pos(20,1)
l.insert_pos(15,1)
l.show()
