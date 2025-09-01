class Node:
    def __init__(self,d):
        self.data=d
        self.next=None

def hasCycle(head):
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return True
    return False

a=Node(1)
b=Node(2)
c=Node(3)
a.next=b
b.next=c
c.next=a
print(hasCycle(a))
