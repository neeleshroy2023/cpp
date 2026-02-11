# Build prefix sum array
def prefix_sum(arr):
    ps = [0] * len(arr)
    ps[0] = arr[0]
    for i in range(1, len(arr)):
        ps[i] = ps[i-1] + arr[i]
    return ps

print(prefix_sum([1,2,3,4,5,6]))

