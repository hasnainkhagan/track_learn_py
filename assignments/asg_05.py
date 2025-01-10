# How to convert tuple to list and then list to tuple and run some examples over it.

# tuple to list
tuple_data = (1, 2, 3, 4)
list_data = list(tuple_data)

print("Original Tuple:", tuple_data)
print("Converted to List:", list_data)

# modifying the list
list_data.append(5)
print("Modified List:", list_data)


# list to tuple
list_data = [1, 2, 3, 4, 5]
tuple_data = tuple(list_data)

print("Original List:", list_data)
print("Converted to Tuple:", tuple_data)


# example : adding elements to a tuple via a list
tuple_data = (10, 20, 30)
list_data = list(tuple_data)  # convert to list
list_data.append(40)  # add an element
list_data.remove(20)  # remove an element
tuple_data = tuple(list_data)  # convert back to tuple

print("Updated Tuple:", tuple_data)

# example : sorting a tuple by converting to a list
unsorted_tuple = (3, 1, 4, 1, 5, 9)
list_data = list(unsorted_tuple)
list_data.sort()
sorted_tuple = tuple(list_data)

print("Sorted Tuple:", sorted_tuple)
