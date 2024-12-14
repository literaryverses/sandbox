class RecursiveSort:
    def __init__(self, array):
        self.array = array

    # O(n log n) time complexity
    # O(n) space complexity
    def merge_sort(self):
        def merge(low, mid, high):
            temp = []
            left = low
            right = mid + 1

            # sorting and storing elements in the temp array
            while left <= mid and right <= high:
                if self.array[left] <= self.array[right]:
                    temp.append(self.array[left])
                    left += 1
                else:
                    temp.append(self.array[right])
                    right += 1

            # if elements in the left half are still left
            while left <= mid:
                temp.append(self.array[left])
                left += 1

            # if elements in the right half are still left
            while right <= high:
                temp.append(self.array[right])
                right += 1

            # transferring from temp array to the actual array
            for i in range(len(temp)):
                self.array[low + i] = temp[i]

        def mergesort(low, high):
            # base case
            if low >= high:
                return

            mid = (low + high) // 2

            # sort the left half
            mergesort(low, mid)

            # sort the right half
            mergesort(mid + 1, high)

            # merge the two halves
            merge(low, mid, high)

        mergesort(0, len(self.array) - 1)

    # O(n^2) time complexity
    # O(n) space complexity for auxiliary stack space
    def bubble_sort(self):
        def bubblesort(n):
            if n <= 1:
                return
            for j in range(n - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]

            bubblesort(n - 1)

        n = len(self.array)
        bubblesort(n)

    # O(n^2) time complexity
    # O(n) space complexity for auxiliary stack space
    def insertion_sort(self):
        def insertionsort(i, n):
            if i == n:
                return
            j = i
            while j > 0 and self.array[j - 1] > self.array[j]:
                self.array[j], self.array[j - 1] = self.array[j - 1], self.array[j]
                j -= 1
            insertionsort(i + 1, n)

        n = len(self.array)
        insertionsort(0, n)

    def quick_sort(self):
        pass
