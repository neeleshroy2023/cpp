/**
 * @param {number[]} arr
 * @returns {number}
 */
class Solution {
    missingNum(arr) {
        // code here
        let max = arr.length + 1;
        let expected = 0
        let sum = 0
        for(let i=0; i < max; i++) {
            expected += i + 1
        }
        
        for(let i=0; i < arr.length; i++) {
            sum += arr[i]
        }
        
        return expected - sum
    }
}