
# O(n) time complexity
# O(1) space complexity
def find_largest_element(array):
    n = len(array)
    max = array[0]
    for i in range(1, n):
        if array[i] > max:
            max = array[i]
    return max