# Build prefix sum array
def prefix_sum(arr):
    ps = [0] * len(arr)
    ps[0] = arr[0]
    for i in range(1, len(arr)):
        ps[i] = ps[i-1] + arr[i]
    return ps

# print(prefix_sum([1,2,3,4,5,6]))

# Given an array of integers nums and an integer k,
#  return the total number of subarrays whose sum equals to k.
def subArraykSum(nums, k):
        hash = {0: 1}
        current_sum = 0
        count = 0
        for num in nums:
            current_sum += num
            target = current_sum - k
            if target in hash:
                 count += hash[target]
            if current_sum in hash:
                 hash[current_sum] += 1
            else:
                 hash[current_sum] = 1
        return count

# print(subArraykSum([1, 2, 1, 3], 3))

# Subarray Sums Divisible by K
def subarraySumDivisibleK(nums, k):
    hash = {0: 1}
    current_sum = 0
    count = 0
    for num in nums:
        current_sum += num
        target = current_sum % k
    if target in hash:
        count += hash[target]
        hash[target] += 1
    else:
        hash[target] = 1
    return count

# print(subarraySumDivisibleK([4, 5, 0, -2, -3, 1], 5))

def equilibriumIndex(nums):
    n = len(nums)
    ps = [0]* n
    ss = [0]* n
    ps[0] = nums[0]
    ss[n-1] = nums[n-1]
    for i in range(1, n):
        ps[i] = ps[i-1] + nums[i]
    for i in range(n-2, -1, -1):
        ss[i] = ss[i+1] + nums[i]
    for i in range(0, n):
         if ps[i] == ss[i]:
            return i
    return 0

print(equilibriumIndex([-7, 1, 5, 2, -4, 3, 0]))
print(equilibriumIndex([1, 2, 0, 3]))
print(equilibriumIndex([1, 1, 1, 1]))
        
def difference_array(arr, queries):
    for q in queries:
        arr[q[0]] += q[2]
        if q[1] + 1 < len(arr) - 1:
            arr[q[1] + 1] -= q[2]
    
    ps = [0] * len(arr)
    ps[0] = arr[0]
    for i in range(1, len(arr)):
        ps[i] = ps[i-1] + arr[i]
    return ps

print(difference_array([2, 3, 5, 6, 7], [[2, 4, 2], [3, 4, -1]]))

def rainwaterHarvest(arr):
    n = len(arr)
    psMax = [0] * n
    ssMax = [0] * n
    
    psMax[0] = arr[0]
    ssMax[n-1] = arr[n-1]
    totalWater = 0

    for i in range(1, n):
        psMax[i] = max(psMax[i-1], arr[i])
    for i in range(n-2, -1, -1):
        ssMax[i] = max(ssMax[i+1], arr[i])
    
    for i in range(0, n):
        totalWater += min(psMax[i], ssMax[i]) - arr[i]
    return totalWater

print(rainwaterHarvest([2, 1, 5, 3, 1, 0, 4]))