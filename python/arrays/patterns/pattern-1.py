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
