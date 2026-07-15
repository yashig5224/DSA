class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:

    def __init__(self):
        self.tail = None

    # Insert at Head
    def pushFront(self, data):
        new = Node(data)

        if self.tail is None:
            self.tail = new
            new.next = new
            return

        new.next = self.tail.next
        self.tail.next = new

    # Insert at Tail
    def pushBack(self, data):
        new = Node(data)

        if self.tail is None:
            self.tail = new
            new.next = new
            return

        new.next = self.tail.next
        self.tail.next = new
        self.tail = new

    # Delete Head
    def popFront(self):
        if self.tail is None:
            return

        if self.tail.next == self.tail:
            self.tail = None
            return

        self.tail.next = self.tail.next.next

    # Delete Tail
    def popBack(self):
        if self.tail is None:
            return

        if self.tail.next == self.tail:
            self.tail = None
            return

        prev = self.tail.next

        while prev.next != self.tail:
            prev = prev.next

        prev.next = self.tail.next
        self.tail = prev

    # Print
    def printList(self):
        if self.tail is None:
            print("Empty")
            return

        temp = self.tail.next

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.tail.next:
                break

        print("(head)")


# Driver Code
cll = CircularLinkedList()

cll.pushBack(10)
cll.pushBack(20)
cll.pushBack(30)
cll.printList()

cll.pushFront(5)
cll.printList()

cll.popFront()
cll.printList()

cll.popBack()
cll.printList()