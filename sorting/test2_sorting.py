from lec2_sorting import RecursiveSort


def test_sorting_algorithm(method_name):
    test_cases = [
        [],  # Empty list
        [1],  # Single element
        [1, 2, 3, 4, 5],  # Already sorted
        [5, 4, 3, 2, 1],  # Reverse order
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3],  # Random order with duplicates
        [1, 1, 1, 1],  # All elements the same
        [7, -3, 5, 0, -1],  # Includes negative numbers
    ]

    for i, case in enumerate(test_cases):
        expected = sorted(case)
        sorter = RecursiveSort(case[:])
        getattr(sorter, method_name)()
        assert (
            sorter.array == expected
        ), f"{method_name} failed for case {i}: {case} -> {sorter.array} != {expected}"

    print(f"{method_name}: all test cases passed")


if __name__ == "__main__":
    for method in [
        "merge_sort",
        "bubble_sort",
        "insertion_sort",
        "quick_sort",
    ]:
        test_sorting_algorithm(method_name=method)
