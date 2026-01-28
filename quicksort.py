'''
Docstring for quicksort
'''
def partition(arr : list, l : int, r : int) -> int:
    ''' This function performs the partition operation of quicksort algorithm '''
    pivot = arr[l]
    i = l + 1
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

def quick_sort(arr : list, l : int, r : int) -> list:
    ''' This function implements quicksort algorithm '''
    if l < r:
        pivot = partition(arr, l, r)
        quick_sort(arr, l, pivot - 1)
        quick_sort(arr, pivot + 1, r)
    return arr

list1 = [9, 7, 1, 9, 9, 5]
quick_sort(list1, 0, len(list1) - 1)
print("Sorted array is:", list1)
