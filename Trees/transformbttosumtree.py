class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def transform_to_sum_tree(root):

    if root is None:
        return 0

    old_value = root.data

    left_sum = transform_to_sum_tree(root.left)

    right_sum = transform_to_sum_tree(root.right)

    root.data = old_value + left_sum + right_sum

    return root.data