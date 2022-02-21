from sorting import bubble_sort, insertion_sort, selection_sort

unsorted_array = [20, -100, 1, 36, -50, 0, 24, 10, 2, 1]
sorted_array = [-100, -50, 0, 1, 1, 2, 10, 20, 24, 36]

result = bubble_sort(unsorted_array)
print(f"Bubble sort: {result}")
assert result == sorted_array


result = insertion_sort(unsorted_array)
print(f"Insertion sort: {result}")
assert result == sorted_array


result = selection_sort(unsorted_array)
print(f"Selection sort: {result}")
assert result == sorted_array
