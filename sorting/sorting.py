def merge_sort(arr: list[int]) -> list[int]:
    """Sort arr via a divide-and-conquer paradigm.

    Args:
        arr: The initial unsorted list or a rearrangement thereof
            produced by recursive calls to this function.

    Returns:
        A list whose items are sorted in ascending order.
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    return merge(left_sorted, right_sorted)

def merge(left: list[int], right: list[int]) -> list[int]:
    """Merge two sorted lists to produce a new, sorted list.

    Args:
        left: A list whose items are sorted in ascending order.
        right: A list whose items are sorted in ascending order.

    Returns:
        A sorted list comprised of the items of left and right.
    """
    sorted_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list
