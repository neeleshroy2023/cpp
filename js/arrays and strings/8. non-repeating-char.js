// User function Template for javascript
/**
 * @param {string} s
 * @returns {string}
 */
class Solution {
    nonRepeatingChar(s) {
        const frequency_map = new Array(26).fill(-1)
        for(let i=0; i < s.length; i++) {
            let index = s.charCodeAt(i) - 'a'.charCodeAt(0)
            if(frequency_map[index] === -1) {
                frequency_map[index] = i
            } else {
                frequency_map[index] = -2
            }
        }
        
        let idx = -1
        for(let i=0; i < 26; i++) {
            if(frequency_map[i] >= 0 && (idx === -1 || frequency_map[i] < frequency_map[idx])) {
                idx = i
            }
        }
        
        return idx === -1 ? '$' : s[frequency_map[idx]]
    }
}