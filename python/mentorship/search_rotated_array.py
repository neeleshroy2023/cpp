import math
def search_rotated(arr, target):
    n = len(arr)
    low = 0
    high = n-1
    while low < high:
        mid = math.floor((low + high) // 2)
        if arr[mid] == target:
            return mid
        if arr[low] <= arr[mid-1]:
            if arr[low] <= target < arr[mid-1]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid + 1] <= target < arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

print(search_rotated([10,12,14,2,4,6,8], 2))
