/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function(target, nums) {
    let windowStart = 0
    let windowSum = 0
    let minLength = Infinity

    for (let windowEnd = 0; windowEnd < nums.length; windowEnd++) {
        windowSum += nums[windowEnd];
        while (windowSum >= target) {
            minLength = Math.min(windowEnd - windowStart + 1, minLength)
            windowSum -= nums[windowStart]
            windowStart++
        }
    }

    if (minLength === Infinity) {
        return 0
    }

    return minLength
};