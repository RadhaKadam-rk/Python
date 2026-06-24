class Node:
    def __init__(self,val):
        self.next = None
        self.val = val

b = Node(2)
c = Node(3)
b.next = c
head = b

# Inserting node at first
a = Node(1)
a.next = head
head = a
current = head
while current != None:
    print(current.val,end ="->")
    current =current.next

#  Inserting at end
e = Node(5)
current = head
while current.next!= None:
    current = current.next

current.next = e
current = head
while current != None:
    print(current.val , end ="->")
    current =current.next

#Inserting at middle
d = Node(4)
current = head
while current.next.next!= None:
    current = current.next

d.next = current.next
current.next = d
current = head
while current!=None:
    print(current.val,end="->")
    current = current.next

#Deleting at front
head = head.next
current = head
while current!=None:
    print(current.val,end="->")
    current = current.next

#Deleting at end
current = head
while current.next.next!= None:
    current=current.next

current.next = None
current =head
while current!=None:
    print(current.val,end="->")
    current=current.next

#Finding middle of list
while current!=None:
    print(current.val,end="->")
    current=current.next

current = head
slow = current
fast = current
while fast.next!=None:
    slow = slow.next
    fast = fast.next.next

print(slow.val)

#Deleting the next of given val of list
current = head
k = 2
while current.val != k:
    current = current.next

current.next = current.next.next

current = head
while current!=None:
    print(current.val,end = "->")
    current = current.next

#Doubly Linked List
class doubleNode:
    def __init__(self,x):
        self.prev=None
        self.next=None
        self.x= x

a = doubleNode(1)
b = doubleNode(2)
c = doubleNode(3)
a.next = b
b.prev = a
b.next = c
c.prev = b
head = a
current = head
while current !=None:
    print(current.x,end="->")
    current = current.next

#Circular linked list
class cirNode:
    def __init__(self,data):
        self.prev=None
        self.next = None
        self.data = data

a = cirNode(1)
b = cirNode(2)
c = cirNode(3)
a.next = b
b.next = c
c.next = a
