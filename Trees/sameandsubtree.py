#same tree
def is_same_tree(p, q):

    # Case 1: Both are empty
    if p is None and q is None:
        return True

    # Case 2: Only one is empty
    if p is None or q is None:
        return False

    # Case 3: Values are different
    if p.data != q.data:
        return False

    # Case 4: Compare left and right subtrees
    return (
        is_same_tree(p.left, q.left)
        and
        is_same_tree(p.right, q.right)
    )
    
#compact version same tree
def is_same_tree(p, q):

    if p is None and q is None:
        return True

    if p is None or q is None:
        return False

    return (
        p.data == q.data
        and is_same_tree(p.left, q.left)
        and is_same_tree(p.right, q.right)
    )
    
    
    
#subtree of another tree
def is_subtree(root, subRoot):

    # If subRoot is empty,
    # it is considered a subtree
    if subRoot is None:
        return True

    # If main tree is empty but subRoot is not
    if root is None:
        return False

    # If values match,
    # check whether both trees are identical
    if root.data == subRoot.data:

        if is_same_tree(root, subRoot):
            return True

    # Continue searching in left and right subtrees
    return (
        is_subtree(root.left, subRoot)
        or
        is_subtree(root.right, subRoot)
    )
#compact version subtree of another tree
def is_subtree(root, subRoot):

    if subRoot is None:
        return True

    if root is None:
        return False

    if is_same_tree(root, subRoot):
        return True

    return (
        is_subtree(root.left, subRoot)
        or
        is_subtree(root.right, subRoot)
    )            
    
    
#complete code
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_same_tree(p, q):

    if p is None and q is None:
        return True

    if p is None or q is None:
        return False

    return (
        p.data == q.data
        and is_same_tree(p.left, q.left)
        and is_same_tree(p.right, q.right)
    )


def is_subtree(root, subRoot):

    if subRoot is None:
        return True

    if root is None:
        return False

    if is_same_tree(root, subRoot):
        return True

    return (
        is_subtree(root.left, subRoot)
        or
        is_subtree(root.right, subRoot)
    )    
    