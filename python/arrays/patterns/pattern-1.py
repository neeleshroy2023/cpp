# Remove duplicates from sorted array
def removeDuplicates(nums):
    length = len(nums)
    if length <= 1: 
        return nums
    left, right = 0, 1
    result = []
    while right < length:
        if nums[left] != nums[right]:
            result.append(nums[left])
        left+=1
        right+=1
    result.append(nums[left])
    return result

print(removeDuplicates([1,1,1,2,2,2,4,4,4,4,8, 8, 8]))

# Move all zeroes to the right
def moveZeroes(nums):
    n = len(nums)
    if n <= 1:
        return nums
    i = 0
    for j in range(n):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
    return nums

print(moveZeroes([1,0,2,0,9,9,3,4,0,0,0,8,9]))

# remove k element
def removeKElement(nums, k):
    n = len(nums)
    i = 0
    for j in range(n):
        if nums[j] != k:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
    while i < n:
        nums[i] = None
        i+=1
    return nums

print(removeKElement([1,0,2,0,9,9,3,4,0,0,0,8,9], 0))

# Compress array (e.g. [a,a,a,b,b,c] → [a,3,b,2,c,1])
def compressArray(nums):
    n = len(nums)
    counter = 0
    result = ''
    i=0
    for j in range(n):
        if nums[j] == nums[i]:
            counter += 1
        else:
            result += nums[i]
            result += str(counter)
            counter = 1
            i = j
    return result

print(compressArray(['a', 'a', 'b', 'b', 'b', 'c']))

# Stable partition [3, -1, 2, -5, -4, 6]
def stable_partition(nums):
    n = len(nums)
    if n <= 1:
        return nums
    i=0
    for j in range(n):
        if nums[i] - nums[j] > nums[i]:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
    return nums

print(stable_partition([3, -1, 2, -5, -4, 6]))

# remove adjacent duplicates
def remove_adjacent_duplicates(nums):
    n = len(nums)
    if n <= 1:
        return nums
    results = []
    i = 0
    for j in range(n):
        if nums[i] != nums[j]:
            results.append(nums[i])
            i=j
    while i < n:
        results.append(nums[i])
        i+=1
    return results

print(remove_adjacent_duplicates(['a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'e', 'f', 'g']))