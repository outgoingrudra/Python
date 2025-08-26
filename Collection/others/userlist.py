from collections import UserList

class MyList(UserList):
    def remove_even(self):
        self.data = [x for x in self.data if x % 2 != 0]

l = MyList([1,2,3,4,5,6])
l.remove_even()
print(l)
