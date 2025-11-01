def longestSubarraySumK(nums, k):
    prefix_sum_map = {0: -1} 
    current_sum = 0
    max_length = 0
    
    for i, num in enumerate(nums):
        current_sum += num
        required_sum = current_sum - k
        
        if required_sum in prefix_sum_map:
            length = i - prefix_sum_map[required_sum]
            max_length = max(max_length, length)
            
        if current_sum not in prefix_sum_map:
            prefix_sum_map[current_sum] = i
            
    return max_length

# Example Usage:
print(longestSubarraySumK([10, 5, 2, 7, 1, 9], 15)) 
# Output: 4