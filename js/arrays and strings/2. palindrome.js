/**
 * @param {string} s
 * @return {boolean}
 */
class Solution {
    isPalindrome(s) {
        // code here
        let left = 0
        let right = s.length-1
        let isPalin = true;
        while(left < right) {
            if (s[left] !== s[right]) {
                isPalin = false;
                break;
            }
            left++
            right--
        }
    
        return isPalin
    }
}
