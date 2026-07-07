class Solution:

    def partition(self, arr, start, end):

        pivot = arr[end]

        index = start - 1

        for j in range(start, end):

            if arr[j] <= pivot:

                index += 1

                arr[index], arr[j] = arr[j], arr[index]

        arr[index + 1], arr[end] = arr[end], arr[index + 1]

        return index + 1

    def quickSort(self, arr, start, end):

        if start >= end:
            return

        pivotIndex = self.partition(arr, start, end)

        self.quickSort(arr, start, pivotIndex - 1)

        self.quickSort(arr, pivotIndex + 1, end)