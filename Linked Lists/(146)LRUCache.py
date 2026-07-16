class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        # Dummy Head and Tail
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    # Remove a node from DLL
    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

    # Insert node right after head (Most Recently Used)
    def insert(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def get(self, key):

        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Move node to front
        self.remove(node)
        self.insert(node)

        return node.val

    def put(self, key, value):

        # Key already exists
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)
        self.insert(node)
        self.cache[key] = node

        # Capacity exceeded
        if len(self.cache) > self.capacity:

            lru = self.tail.prev

            self.remove(lru)

            del self.cache[lru.key]