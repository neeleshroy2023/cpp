def maxSubArray(nums):
    if not nums:
        return 0
    
    current_max = nums[0]
    overall_max = nums[0]
    
    for i in range(1, len(nums)):
        num = nums[i]
        
        current_max = max(num, current_max + num)
        overall_max = max(overall_max, current_max)
            
    return overall_max

# Example Usage:
print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# Output: 6