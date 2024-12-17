# O(n) time complexity
# O(1) space complexity
def largest_element(array):
    """Find largest element in array"""
    n = len(array)
    maxi = array[0]
    for i in range(1, n):
        if array[i] > maxi:
            maxi = array[i]
    return maxi


# O(n) time complexity
# O(1) space complexity
def second_largest_and_smallest(array):
    """Find the second largest and smallest element in array"""
    n = len(array)
    mini = s_min = float("inf")
    maxi = s_max = -float("inf")
    for i in range(n):
        if array[i] < mini:
            s_min = mini
            mini = array[i]
        elif array[i] < s_min and array[i] != mini:
            s_min = array[i]
        if array[i] > maxi:
            s_max = maxi
            maxi = array[i]
        elif array[i] > s_max and array[i] != maxi:
            s_max = array[i]
    return s_min, s_max


# O(n) time complexity
# O(1) space complexity
def is_sorted(array):
    """Check if an array is sorted or not"""
    n = len(array)
    for i in range(n - 1):
        if array[i + 1] < array[i]:
            return False
    return True


# O(n) time complexity
# O(1) space complexity
def contains_duplicates(array):
    """Check if an array has duplicates"""
    hashset = set()
    for n in array:
        if n in hashset:
            return True
        hashset.add(n)
    return False


# O(n) time complexity
# O(1) space complexity
def remove_duplicates(sorted_array):
    """Remove duplicates in a sorted array"""
    i = 0
    for j in range(1, len(sorted_array)):
        if sorted_array[j] != sorted_array[i]:
            i += 1
            sorted_array[i] = sorted_array[j]

    return sorted_array[: i + 1]


# O(n) time complexity
# O(n) space complexity
def isAnagram(str1, str2):
    """Determine if the strings are anagrams of each other"""
    if len(str1) != len(str2):
        return False

    count_str1, count_str2 = {}, {}
    for i in range(len(str1)):
        count_str1[str1[i]] = count_str1.get(str1[i], 0) + 1
        count_str2[str2[i]] = count_str2.get(str2[i], 0) + 1

    for c in count_str1:
        if count_str1[c] != count_str2.get(c, 0):
            return False

    return True


# O(n) time complexity
# O(1) space complexity
def left_rotate_once(array):
    """Left rotate an array by once place"""
    n = len(array)
    move = array[0]
    for i in range(n - 1):
        array[i] = array[i + 1]
    array[n - 1] = move

    return array


# O(n) time complexity
# O(1) space complexity
def left_rotate_kth(array, k):
    """Left rotate an array by k times"""

    def reverse(array, start, end):
        while start <= end:
            array[start], array[end] = array[end], array[start]
            start += 1
            end -= 1

    n = len(array)
    # reverse first k elements
    reverse(array, 0, k - 1)
    # reverse last n-k elements
    reverse(array, k, n - 1)
    # reverse the whole array
    reverse(array, 0, n - 1)
    return array


# O(n) time complexity
# O(1) space complexity
def right_rotate_kth(array, k):
    """Right rotate an array by k times"""

    def reverse(array, start, end):
        while start <= end:
            array[start], array[end] = array[end], array[start]
            start += 1
            end -= 1

    n = len(array)
    # reverse first n-k elements
    reverse(array, 0, n - k - 1)
    # reverse last k elements
    reverse(array, n - k, n - 1)
    # reverse the whole array
    reverse(array, 0, n - 1)
    return array


# O(n) time complexity
# O(1) space complexity
def zeros_to_end(array):
    """Puts zeros at the end of an array"""
    j = -1
    for i in range(len(array)):
        if array[i] == 0 and j == -1:
            j = i

        if array[i] != 0 and j > -1:
            array[i], array[j] = array[j], array[i]
            j += 1
    return array


# O(n) time complexity
# O(1) space complexity
def linear_search(array, char):
    """Returns index of a char in an array,
    otherwise returns -1"""
    for i, c in enumerate(array):
        if char == c:
            return i
    return -1


#
#
def union(array):
    pass


def missing_number(array):
    pass


# O(n) time complexity
# O(1) space complexity
def max_consecutive_ones(array):
    """Returns the max number of consecutive 1s in an array"""
    count = 0
    maxi = 0
    for i in range(len(array)):
        if array[i] == 1:
            count += 1
        else:
            count = 0
        maxi = max(maxi, count)
    return maxi


def once_in_twice(array):
    pass


def longest_sum_given(array):
    pass


def longest_sum_k(array):
    pass
