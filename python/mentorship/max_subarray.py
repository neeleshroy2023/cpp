# Longest subarray with sum K [10, 5, 2, 7, 1, 9], K = 15;

def longest_subarray(arr, target):
    n = len(arr)
    if n < 2:
        return arr
    left=0
    right=0
    sum=arr[0]
    max_subarray = []
    while right < n:
        while left <= right and sum > target:
            sum -= arr[left]
            left += 1
        if sum == target and len(max_subarray) < right - left + 1:
            max_subarray = arr[left:right+1]
        right += 1
        if right < n:
            sum += arr[right]
    
    return max_subarray

print(longest_subarray([1,1,1], 2))
   