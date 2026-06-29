arr = [1, 2, 3, 4, 5]
n = len(arr)

# Start index loop
for st in range(n):
    # End index loop
    for end in range(st, n):
        # Print elements from 'st' to 'end'
        for i in range(st, end + 1):
            print(arr[i], end="")
        print(" ", end="")  # Print space after each subarray
    print()  # Print newline after finishing all subarrays starting with 'st'





# BRUTE FORCE APPROACH
arr = [1, -2, 3, 4, -5]
n = len(arr)

# Step 1: Initialize max_sum to a very small number
max_sum = float("-inf")

# Start index loop
for st in range(n):
    # End index loop
    for end in range(st, n):

        current_subarray_sum = 0   # DECLARE CURSUM=0
        # Calculate sum of elements from 'st' to 'end'
        for i in range(st, end + 1):
            current_subarray_sum += arr[i] #ADD END POINT AFTER EVERY SUBARRAY SUM IN ITERATION 

        # Update global max_sum if current one is larger
        if current_subarray_sum > max_sum:
            max_sum = current_subarray_sum

print(f"\nMaximum Subarray Sum: {max_sum}")




#KADANE'S ALGORITHM
# Input array from the image
arr = [3, -4, 5, 4, -1, 7, -8]

# Initialize variables exactly like the image
currSum = 0
maxSum = float("-inf") 

# Loop through the array
for i in range(len(arr)):
    currSum += arr[i]

    # Update maxSum with the largest value found so far
    maxSum = max(currSum, maxSum)

    # If the running sum drops below zero, reset it to zero
    if currSum < 0:
        currSum = 0

print(f"Maximum Subarray Sum: {maxSum}")
# Output: 15 (from the subarray [5, 4, -1, 7])
