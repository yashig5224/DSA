class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # 1. Push Front
    def pushFront(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = self.tail = newNode
            return

        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode

    # 2. Push Back
    def pushBack(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = self.tail = newNode
            return

        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode

    # 3. Pop Front
    def popFront(self):
        if self.head is None:
            print("List is Empty")
            return

        if self.head == self.tail:
            self.head = self.tail = None
            return

        self.head = self.head.next
        self.head.prev = None

    # 4. Pop Back
    def popBack(self):
        if self.head is None:
            print("List is Empty")
            return

        if self.head == self.tail:
            self.head = self.tail = None
            return

        self.tail = self.tail.prev
        self.tail.next = None

    # 5. Print List
    def printList(self):
        if self.head is None:
            print("List is Empty")
            return

        temp = self.head

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")


# ---------------- Driver Code ----------------

dll = DoublyLinkedList()

print("Push Front")
dll.pushFront(20)
dll.pushFront(10)
dll.printList()

print("\nPush Back")
dll.pushBack(30)
dll.pushBack(40)
dll.printList()

print("\nPop Front")
dll.popFront()
dll.printList()

print("\nPop Back")
dll.popBack()
dll.printList()