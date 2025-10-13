def merge_sort(arr):
    n = len(arr)
    if n < 2:
        return arr
    mid = n // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    merge_sort(left_half)
    merge_sort(right_half)

    return merge(arr, left_half, right_half)

def merge(arr, left, right):
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1
        k+=1
    while i < len(left):
        arr[k] = left[i]
        k+=1
        i+=1
    while j < len(right):
        arr[k] = right[j]
        j+=1
        k+=1
    return arr

print(merge_sort([8, 3, 1, 7, 0, 10, 2]))