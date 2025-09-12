/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */

class Solution {
    maxSubarraySum(arr, k) {
        let windowSum = 0
        
        for(let i=0; i<k; i++) {
            windowSum += arr[i]
        }
        
        let max = windowSum;
        
        for (let i = k; i < arr.length; i++) {
            windowSum = windowSum + arr[i] - arr[i - k]
            max = Math.max(max, windowSum)
        }
        
        return max
    }
}
