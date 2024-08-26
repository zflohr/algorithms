def binary_search(arr: list[int], val: int) -> int:
    """Find the index of val in arr via a binary search.

    Args:
        arr: A sorted list of integers.
        val: The target value to search for in arr.

    Returns:
        The index of val in arr, or -1 if val isn't in arr.
    """
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == val:
            return mid
        if arr[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
    return -1
