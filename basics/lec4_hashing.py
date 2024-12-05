class HashingBasics:
    """
    Given an array and a set of queries,
    find how many times each query appears in the array
    """

    def __init__(self, array):
        self.array = array

    # O(n^n) time complexity
    # O(n) space complexity
    def brute_force(self, queries: set):
        freqs = dict()
        for query in queries:
            freqs[query] = 0
            for char in self.array:
                if char == query:
                    freqs[query] += 1
        return freqs

    # O(n) time complexity
    # O(n) space complexity
    def hashing(self, queries: set):
        freqs = dict()
        for char in self.array:
            freqs[char] = freqs.get(char, 0) + 1
        return {query: freqs.get(query, 0) for query in queries}


class Frequencies:
    def __init__(self, array):
        self.array = array

    # O(n) time complexity
    # O(n) space complexity for creating the dictionary
    def getFreqs(self):
        """Find the frequency of each element in the array."""
        freqs = dict()
        for char in self.array:
            freqs[char] = freqs.get(char, 0) + 1
        return freqs

    # O(n) time complexity
    # O(n) space complexity for creating the dictionary
    def getMinMaxFreqs(self):
        """Find the elements in an array with the most and least frequencies."""
        freqs = self.getFreqs()
        if not freqs:
            return None, None
        max_char = max(freqs.items(), key=lambda item: item[1])
        min_char = min(freqs.items(), key=lambda item: item[1])
        return max_char, min_char
