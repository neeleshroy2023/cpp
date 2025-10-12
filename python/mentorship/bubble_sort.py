def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n):
        is_swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                is_swapped = True
        if (is_swapped == False):
            break;
    return arr

print(bubble_sort([5, 1, 4, 2, 8]))