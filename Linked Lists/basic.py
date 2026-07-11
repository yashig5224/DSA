#push front 
from torch import Node


def pushFront(self, data):

    newNode = Node(data)

    if self.head is None:

        self.head = newNode
        self.tail = newNode
        return

    newNode.next = self.head

    self.head = newNode
    
#print list
def printList(self):

    temp = self.head

    while temp:

        print(temp.data),

        temp = temp.next

    print
    
#push back
def pushBack(self, data):

    newNode = Node(data)

    if self.head is None:

        self.head = newNode
        self.tail = newNode
        return

    self.tail.next = newNode

    self.tail = newNode        
    
#pop front 
def popFront(self):

    if self.head is None:
        return

    self.head = self.head.next

    if self.head is None:
        self.tail = None    

#pop back
def popBack(self):

    if self.head is None:
        return

    if self.head == self.tail:

        self.head = None
        self.tail = None
        return

    temp = self.head

    while temp.next != self.tail:

        temp = temp.next

    temp.next = None

    self.tail = temp
    
    
#insert at position
def insert(self, index, data):

    if index == 0:

        self.pushFront(data)
        return

    temp = self.head

    for i in range(index - 1):

        temp = temp.next

    newNode = Node(data)

    newNode.next = temp.next

    temp.next = newNode

    if newNode.next is None:

        self.tail = newNode            
        
#search
def search(self, key):

    temp = self.head

    index = 0

    while temp:

        if temp.data == key:
            return index

        temp = temp.next

        index += 1

    return -1                