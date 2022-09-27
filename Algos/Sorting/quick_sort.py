def quicksort(array):
    quickSortHelper(array, 0, len(array) - 1)
    return array


def quickSortHelper(array, startIdx, endIdx):
    if startIdx >= endIdx:
        return
    pivotIdx = startIdx
    leftIdx = startIdx + 1
    rightIdx = endIdx
    while rightIdx >= leftIdx:
        if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
            swap(leftIdx, rightIdx, array)
        if array[leftIdx] < array[pivotIdx]:
            leftIdx += 1
        if array[rightIdx] > array[pivotIdx]:
            rightIdx -= 1
    swap(pivotIdx, rightIdx, array)
    leftArrayIsSmaller = rightIdx - 1 - leftIdx < endIdx - (rightIdx + 1)
    if leftArrayIsSmaller:
        quickSortHelper(array, startIdx, rightIdx-1)
        quickSortHelper(array, rightIdx + 1, endIdx)
    else:
        quickSortHelper(array, rightIdx + 1, endIdx)
        quickSortHelper(array, startIdx, rightIdx - 1)


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


arr = [12, 11, 13, 5, 6, 7]
quicksort(arr)
print(arr)
