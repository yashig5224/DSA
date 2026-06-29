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
