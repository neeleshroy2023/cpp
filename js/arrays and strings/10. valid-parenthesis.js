/**
 * @param {string} s
 * @returns {boolean}
 */

class Solution {
    isBalanced(s) {
        if (s.length === 0 || s.length % 2 === 1) return false
        const map = {
            "}": "{",
            "]": "[",
            ")": "("
        }
    
        const stack = []
    
        for (let i=0; i < s.length; i++) {
            const mapped = map[s[i]]
            if ( stack.length > 0 && mapped && mapped === stack[stack.length - 1]) {
                stack.pop()
            } else {
                stack.push(s[i])
            }
        }
    
        return stack.length === 0
    }
}