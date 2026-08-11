class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, key):

    if root is None:
        return TreeNode(key)

    if key < root.val:
        root.left = insert(root.left, key)

    elif key > root.val:
        root.right = insert(root.right, key)

    return root


def search(root, key):

    if root is None:
        return False

    if root.val == key:
        return True

    if key < root.val:
        return search(root.left, key)

    return search(root.right, key)


def get_min(root):

    current = root

    while current.left:
        current = current.left

    return current


def delete(root, key):

    if root is None:
        return None

    if key < root.val:

        root.left = delete(root.left, key)

    elif key > root.val:

        root.right = delete(root.right, key)

    else:

        # No child
        if root.left is None and root.right is None:
            return None

        # Only right child
        if root.left is None:
            return root.right

        # Only left child
        if root.right is None:
            return root.left

        # Two children
        successor = get_min(root.right)

        root.val = successor.val

        root.right = delete(root.right, successor.val)

    return root