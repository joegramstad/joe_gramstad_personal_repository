def quicksort(arr):
    if len(arr) < 2:
        return arr

    pivot_ind = len(arr) // 2
    arr[0], arr[pivot_ind] = arr[pivot_ind], arr[0]
    pivot = arr[0]
    left_arr = [elem for elem in arr[1:] if elem <= pivot]
    right_arr = [elem for elem in arr[1:] if elem > pivot]
    return quicksort(left_arr) + [pivot] + quicksort(right_arr)
