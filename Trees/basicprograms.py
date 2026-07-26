class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

#building tree using preorder sequence
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree(nodes):
    if nodes[index[0]] == -1:
        index[0] += 1
        return None

    new_node = Node(nodes[index[0]])
    index[0] += 1

    new_node.left = build_tree(nodes)
    new_node.right = build_tree(nodes)

    return new_node


nodes = [1, 2, 4, -1, -1, 5, -1, -1, 3, -1, -1]

index = [0]

root = build_tree(nodes)

#preorder traversal
def preorder(root):
    if root is None:
        return

    print(root.data, end=" ")

    preorder(root.left)

    preorder(root.right)
    
#inorder traversal
def inorder(root):
    if root is None:
        return

    inorder(root.left)

    print(root.data, end=" ")

    inorder(root.right)
    
#postorder traversal
def postorder(root):
    if root is None:
        return

    postorder(root.left)

    postorder(root.right)

    print(root.data, end=" ")
    
#level order traversal
from collections import deque


def level_order(root):
    if root is None:
        return

    queue = deque()

    queue.append(root)

    while queue:
        current = queue.popleft()

        print(current.data, end=" ")

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)
            
#level order traversal with levels
from collections import deque


def level_order_by_level(root):
    if root is None:
        return []

    result = []

    queue = deque([root])

    while queue:

        level_size = len(queue)

        current_level = []

        for _ in range(level_size):

            node = queue.popleft()

            current_level.append(node.data)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result

#level order traversal with levels using None as a marker
from collections import deque


def level_order_null_marker(root):
    if root is None:
        return

    queue = deque()

    queue.append(root)
    queue.append(None)

    while queue:

        node = queue.popleft()

        if node is None:

            print()

            if queue:
                queue.append(None)

        else:

            print(node.data, end=" ")

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)


#binary tree code template
from collections import deque


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder(root):

    if root is None:
        return

    print(root.data, end=" ")

    preorder(root.left)
    preorder(root.right)


def inorder(root):

    if root is None:
        return

    inorder(root.left)

    print(root.data, end=" ")

    inorder(root.right)


def postorder(root):

    if root is None:
        return

    postorder(root.left)
    postorder(root.right)

    print(root.data, end=" ")


def level_order(root):

    if root is None:
        return

    queue = deque([root])

    while queue:

        node = queue.popleft()

        print(node.data, end=" ")

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)                    