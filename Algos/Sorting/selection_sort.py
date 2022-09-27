# https://www.programiz.com/dsa/selection-sort
# Selects the minimum element from the array and places it at the beginning
def selectionsort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


arr = [64, 34, 25, 12, 22, 11, 90]
selectionsort(arr)
print(arr)
