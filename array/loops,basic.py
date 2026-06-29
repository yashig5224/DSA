# Working with a standard Python List
fruits = ["apple", "banana", "cherry"]

print("--- Direct Loop ---")
for fruit in fruits:
    print(fruit)

print("--- Index Loop ---")
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")

print("--- Enumerate Loop ---")
for index, fruit in enumerate(fruits):
    print(f"Item {index} is {fruit}")

numbers = [42, 17, 89, 3, 25]

# Track values starting with the first element
smallest = numbers[0]
largest = numbers[0]

# Loop to compare each number
for num in numbers:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num

print(smallest)  # 3
print(largest)   # 89


# reverse using slicing
numbers = [10, 20, 30, 40]
reversed_numbers = numbers[::-1]

print(reversed_numbers)  # [40, 30, 20, 10]
print(numbers)           # [10, 20, 30, 40] (Original is safe)


# reverse manually
def reverse_manually(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        # Swap the elements
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

numbers = [10, 20, 30, 40]
reverse_manually(numbers)
print(numbers)  # [40, 30, 20, 10]
