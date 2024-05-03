p = [42,[73,None]]
p[1][1] = p

print(p)
print(p[1][1][1][1][1][0])

next_dict = {'value' : 73, 'next': None }
d = {'value' : 42, 'next' : next_dict }
next_dict['next'] = d

print(d)

class Node():

    def __init__(self, value):
        self.value = value
        self.next = None

    def update(self, value, next):
        self.value = value
        self.next = next

n1 = Node(42)
n2 = Node(73)
n1.update(42,n2)
n2.update(73,n1)

