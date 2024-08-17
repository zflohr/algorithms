def merge(arr: list[int], left: int, mid: int, right: int) -> None:
    """Merge two sublists of arr to produce a new, sorted sublist.

    Args:
        arr: The initial unsorted list or a rearrangement thereof
            produced by calls to merge.
        left: The index of the leftmost item in a sublist of arr.
        mid: The index that defines the end of a sublist and the
            beginning of another in arr.
        right: The index of the rightmost item in a sublist of arr.
    """
    n1 = mid - left + 1
    n2 = right - mid
    left_half = [arr[left + i] for i in range(n1)]
    right_half = [arr[mid + 1 + i] for i in range(n2)]
    i, j = 0, 0
    k = left
    while i < n1 and j < n2:
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = left_half[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = right_half[j]
        j += 1
        k += 1

def merge_sort(arr: list[int], left: int, right: int) -> None:
    """Sort arr via a divide-and-conquer paradigm.

    Args:
        arr: The initial unsorted list or a rearrangement thereof
            produced by calls to merge.
        left: The index of the leftmost item in a sublist of arr.
        right: The index of the rightmost item in a sublist of arr.
    """
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)
