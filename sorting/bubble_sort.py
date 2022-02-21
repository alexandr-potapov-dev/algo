# Time O(n ^ 2) | Space O(1)
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[j] < array[i]:
                array[j], array[i] = array[i], array[j]
    return array
