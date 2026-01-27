def partition(arr : list, l : int, r : int) -> int:
    pivot = arr[l]
    i  = l + 1
    j = r 
    while i < j:
        while i < j and arr[i] <= pivot:
            i += 1
        while j >= i and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j

def QuickSort(arr : list, l : int, r : int) -> list:
    if l < r:
        pivot = partition(arr, l, r)
        QuickSort(arr, l, pivot - 1)
        QuickSort(arr, pivot + 1, r)
    return arr

l = [9, 7, 1, 9, 9, 5]

QuickSort(l, 0, len(l) - 1)
print("Sorted array is:", l)

