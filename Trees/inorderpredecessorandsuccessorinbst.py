def findPreSuc(root, key):

    predecessor = None
    successor = None

    current = root

    while current:

        if key < current.val:
            # Current can be a successor
            successor = current
            current = current.left

        elif key > current.val:
            # Current can be a predecessor
            predecessor = current
            current = current.right

        else:
            # Key found

            # Find predecessor
            if current.left:
                temp = current.left

                while temp:
                    predecessor = temp
                    temp = temp.right

            # Find successor
            if current.right:
                temp = current.right

                while temp:
                    successor = temp
                    temp = temp.left

            break

    return predecessor, successor