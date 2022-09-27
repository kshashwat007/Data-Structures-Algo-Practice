# Recursive
def binarySearch(arr, ele, low, high):
    if high >= low:
        mid = (low+high) // 2
        if ele == arr[mid]:
            return mid
        elif ele > arr[mid]:
            binarySearch(arr, ele, mid+1, high)
        else:
            binarySearch(arr, ele, low, mid-1)
    else:
        return -1

# Iterative


def binarySearchIter(arr, ele, low, high):
    while low <= high:
        mid = (low+high) // 2
        if ele == arr[mid]:
            return mid
        elif ele > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1
