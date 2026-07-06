def insertionSort(nums):

    n = len(nums)

    for i in range(1, n):

        current = nums[i]

        j = i - 1

        while j >= 0 and nums[j] > current:       #desc order:while nums[j] < current

            nums[j + 1] = nums[j]

            j -= 1

        nums[j + 1] = current

    return nums


nums = [5,3,4,1]
print(insertionSort(nums))