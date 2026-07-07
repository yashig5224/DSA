class Solution:

    def merge(self, arr, start, mid, end):

        temp = []

        i = start
        j = mid + 1

        # Compare both halves
        while i <= mid and j <= end:

            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1

        # Remaining left half
        while i <= mid:
            temp.append(arr[i])
            i += 1

        # Remaining right half
        while j <= end:
            temp.append(arr[j])
            j += 1

        # Copy back to original array
        for k in range(len(temp)):
            arr[start + k] = temp[k]

    def mergeSort(self, arr, start, end):

        if start >= end:
            return

        mid = (start + end) // 2

        self.mergeSort(arr, start, mid)

        self.mergeSort(arr, mid + 1, end)

        self.merge(arr, start, mid, end)