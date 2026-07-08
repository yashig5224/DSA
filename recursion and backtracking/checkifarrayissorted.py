def isSorted(arr, n):

    if n == 0 or n == 1:
        return True

    if arr[n-2] > arr[n-1]:
        return False

    return isSorted(arr, n-1)