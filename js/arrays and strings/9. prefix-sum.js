/**
 * @param {number[]} arr
 * @returns {number[]}
 */
class Solution {
    prefSum(arr) {
        for(let i=1; i < arr.length; i++) {
            arr[i] = arr[i-1] + arr[i]
        }
        return arr
    }
}
