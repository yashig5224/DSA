class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):

        if index < 0 or index >= self.size:
            return -1

        temp = self.head

        for i in range(index):
            temp = temp.next

        return temp.val

    def addAtHead(self, val):

        newNode = Node(val)

        newNode.next = self.head

        self.head = newNode

        self.size += 1

    def addAtTail(self, val):

        newNode = Node(val)

        if self.head is None:
            self.head = newNode
            self.size += 1
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = newNode

        self.size += 1

    def addAtIndex(self, index, val):

        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
            return

        newNode = Node(val)

        temp = self.head

        for i in range(index - 1):
            temp = temp.next

        newNode.next = temp.next

        temp.next = newNode

        self.size += 1

    def deleteAtIndex(self, index):

        if index < 0 or index >= self.size:
            return

        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return

        temp = self.head

        for i in range(index - 1):
            temp = temp.next

        temp.next = temp.next.next

        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)