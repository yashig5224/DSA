#brute force approach
def inversionCount(arr):

    n = len(arr)

    count = 0

    for i in range(n):

        for j in range(i + 1, n):

            if arr[i] > arr[j]:
                count += 1

    return count


#optimal:merge sort
class Solution:

    def merge(self, arr, start, mid, end):

        temp = []

        i = start
        j = mid + 1

        inv = 0

        while i <= mid and j <= end:

            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1

            else:
                temp.append(arr[j])
                inv += (mid - i + 1)
                j += 1

        while i <= mid:
            temp.append(arr[i])
            i += 1

        while j <= end:
            temp.append(arr[j])
            j += 1

        for k in range(len(temp)):
            arr[start + k] = temp[k]

        return inv

    def mergeSort(self, arr, start, end):

        if start >= end:
            return 0

        mid = start + (end - start) // 2

        leftInv = self.mergeSort(arr, start, mid)

        rightInv = self.mergeSort(arr, mid + 1, end)

        mergeInv = self.merge(arr, start, mid, end)

        return leftInv + rightInv + mergeInv

    def inversionCount(self, arr):

        return self.mergeSort(arr, 0, len(arr) - 1)