def selectionSort(nums):

    n = len(nums)

    for i in range(n):

        minIndex = i

        for j in range(i + 1, n):

            if nums[j] < nums[minIndex]:      #desc order:if nums[j] > nums[maxIndex]
                minIndex = j

        nums[i], nums[minIndex] = nums[minIndex], nums[i]

    return nums


nums = [4,2,5,1,3]
print(selectionSort(nums))