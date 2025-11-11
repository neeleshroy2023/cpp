/**
 * @param {Number[]} arr
 * @returns {void}
 */

class Solution {
    pushZerosToEnd(arr) {
        let countIndex = 0
        for(let i=0; i < arr.length; i++) {
            if (arr[i] === 0) {
                countIndex += 1
            } else {
                let temp = arr[i]
                arr[i] = arr[i - countIndex]
                arr[i - countIndex] = temp
            }
        }
        
        return arr
    }
}