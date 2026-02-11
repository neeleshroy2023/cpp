# Fixed Window Expansion

# Max sum subarray of size k
def max_subarray(arr, k):
    n=len(arr)
    s = sum(arr[:k])
    if n <= k:
        return s
    max_sum = s
    for i in range(k, n):
        s = s + arr[i] - arr[i-k]
        max_sum = max(s, max_sum)
    return max_sum

print(max_subarray([1, 5, 4, 2, 9], 3))

# Min sum subarray of size k
def min_subarray(arr, k):
    n = len(arr)
    s = sum(arr[:k])
    if n <= k:
        return s
    min_sum = s
    for i in range(k, n):
        s = s + arr[i] - arr[i-k]
        min_sum = min(min_sum, s)
    return min_sum

print(min_subarray([1,5,4,2,-9], 3))

# Min avg subarray of size k
def avg_subarray(arr, k):
    n = len(arr)
    s = sum(arr[:k])
    a = s // k 
    if n <= k:
        return a
    max_avg = a
    for i in range(k, n):
        s = s + arr[i] - arr[i-k]
        a = s // k
        max_avg = max(max_avg, a)
    return max_avg

print(avg_subarray([1,5,4,2,9], 3))