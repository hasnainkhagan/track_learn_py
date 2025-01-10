# Create a python file and submit it covering all data structures concepts in it with different examples. 

# Data Structures in Python

# 1. Lists: Ordered, mutable, used for storing a collection of items.
print("==== Lists Example ====")
my_list = [10, 20, 30, 40, 50]
print(f"Original List: {my_list}")

# add an item
my_list.append(60)
print(f"After Append: {my_list}")

# remove an item
my_list.remove(30)
print(f"After Remove: {my_list}")

# accessing elements
print(f"Element at index 2: {my_list[2]}")

# slice a list
print(f"Sliced List (from index 1 to 3): {my_list[1:4]}")

# 2. Tuples: Ordered, immutable, ideal for data that shouldn’t change.
print("\n==== Tuples Example ====")
my_tuple = (10, 20, 30, 40, 50)
print(f"Original Tuple: {my_tuple}")

# accessing elements
print(f"Element at index 1: {my_tuple[1]}")

# slicing a tuple
print(f"Sliced Tuple (from index 2 to 4): {my_tuple[2:5]}")

# 3. Dictionaries: Stores data as key-value pairs, allowing fast lookups.
print("\n==== Dictionaries Example ====")
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(f"Original Dictionary: {my_dict}")

# accessing values using keys
print(f"Name: {my_dict['name']}")
print(f"Age: {my_dict['age']}")

# adding a new key value pair
my_dict['job'] = 'Developer'
print(f"After Adding 'job': {my_dict}")

# removing a key-value pair
del my_dict['age']
print(f"After Removing 'age': {my_dict}")

# 4. Sets: Unordered collection of unique items, useful for membership tests.
print("\n==== Sets Example ====")
my_set = {10, 20, 30, 40, 50}
print(f"Original Set: {my_set}")

# adding an item
my_set.add(60)
print(f"After Adding 60: {my_set}")

# removing an item
my_set.remove(30)
print(f"After Removing 30: {my_set}")

# checking membership
print(f"Is 40 in the set? {40 in my_set}")
print(f"Is 100 in the set? {100 in my_set}")

# set operations (union, intersection, difference)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(f"Union of set1 and set2: {set1.union(set2)}")
print(f"Intersection of set1 and set2: {set1.intersection(set2)}")
print(f"Difference of set1 and set2: {set1.difference(set2)}")