# https://www.programiz.com/dsa/insertion-sort
# Insertion sort places an unsorted element at its suitable position at each iteration. It starts with the second element and assumes the first element is sorted. We then compare the current element with its prev element until the correct position is found.
def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


arr = [12, 4, 7, 13, 6]
insertionSort(arr)
print(arr)
