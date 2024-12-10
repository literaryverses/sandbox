class Sort:
    def __init__(self, array):
        self.array = array

    # O(n^2) time complexity
    # O(1) space complexity
    def selection_sort(self):
        n = len(self.array)
        for i in range(n):
            min = i
            for j in range(i + 1, n):
                if self.array[j] < self.array[min]:
                    min = j

            self.array[i], self.array[min] = self.array[min], self.array[i]

    # O(n^2) time complexity
    # O(1) space complexity
    def bubble_sort(self):
        n = len(self.array)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]

    # O(n) time complexity is best case when array is already sorted;
    # hence add check to see if list is already sorted to optimize
    def modified_bubble_sort(self):
        n = len(self.array)
        for i in range(n - 1):
            swapped = False
            for j in range(n - i - 1):
                if self.array[j] > self.array[j + 1]:
                    swapped = True
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
            if not swapped:
                break  # quits if no swaps are made (already sorted!)

    # O(n^2) time complexity; best case is O(n)
    # O(1) space complexity
    def insertion_sort(self):
        n = len(self.array)
        for i in range(n - 1):
            j = i + 1
            while j > 0 and self.array[j - 1] > self.array[j]:
                self.array[j], self.array[j - 1] = self.array[j - 1], self.array[j]
                j -= 1
