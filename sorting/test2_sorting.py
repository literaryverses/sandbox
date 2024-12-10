from test1_sorting import test_sorting_algorithm


if __name__ == "__main__":
    for method in [
        "merge_sort",
        "bubble_sort",
        "insertion_sort",
        "quick_sort",
    ]:
        test_sorting_algorithm(method_name=method)
