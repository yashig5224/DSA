#height of bt
def height(root):

    if root is None:
        return 0

    left_height = height(root.left)

    right_height = height(root.right)

    return 1 + max(left_height, right_height)


#count nodes
def count_nodes(root):

    if root is None:
        return 0

    left_count = count_nodes(root.left)

    right_count = count_nodes(root.right)

    return 1 + left_count + right_count

#sum of nodes
def sum_nodes(root):

    if root is None:
        return 0

    left_sum = sum_nodes(root.left)

    right_sum = sum_nodes(root.right)

    return root.data + left_sum + right_sum