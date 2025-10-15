# find an element in a sorted array // arr: [2,4,6,8,10,12,14], element: 12

import math

def find_element(arr, target):
    low = 0
    high = len(arr) - 1
    while(low < high):
        mid = math.floor((low + high) // 2)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


print(find_element([2,4,6,8,10,12,14], 12))