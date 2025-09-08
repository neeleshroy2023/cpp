// User function Template for javascript

/**
 * @param {number[]} arr
 * @returns {number}
 */

class Solution {
    // Function to find equilibrium point in the array.
    findEquilibrium(arr) {
        // code here
        const n = arr.length
        if (n < 2) return -1
        
        const prefix = new Array(n).fill(0)
        const suffix = new Array(n).fill(0)

        prefix[0] = arr[0]
        suffix[n-1] = arr[n-1]
        for(let i=1; i < n; i++) {
            prefix[i] = prefix[i-1] + arr[i]
        }
        
        for(let i=n-2; i >= 0 ; i--) {
            suffix[i] = suffix[i+1] + arr[i]
        }
        
        for(let i=1; i<n; i++) {
            if(prefix[i] === suffix[i]) {
                return i
            }
        }
        
        return -1
    }
}