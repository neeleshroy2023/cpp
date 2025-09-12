// User function Template for javascript

/**
 * @param {number[]} arr
 * @return {number[]}
 */

class Solution {
    productExceptSelf(arr) {
        const n = arr.length
        const prefix = new Array(n).fill(1)
        const suffix = new Array(n).fill(1)
        
        const productExceptSelf = new Array(n)
        
        for(let i=1; i < n; i++) {
            prefix[i] = prefix[i-1] * arr[i-1]
        }
        
        for(let i=n-2; i >= 0; i--) {
            suffix[i] = suffix[ix+1] * arr[i+1]
        }
        
        for(let i=0; i < n; i++) {
            productExceptSelf[i] = prefix[i] * suffix[i]
        }
        
        return productExceptSelf;
    }
}