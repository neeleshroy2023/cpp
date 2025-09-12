class Solution {
    canSplit(arr) {
        const n = arr.length
        let prefix = new Array(n).fill(0);
        let suffix = new Array(n).fill(0);

        prefix[0] = arr[0];
        suffix[n-1] = arr[n-1]

        for(let i=1; i < n; i++) {
            prefix[i] = prefix[i-1] + arr[i]
        }

        for(let i=n-1; i > 0; i--) {
            suffix[i] = suffix[i+1] + arr[i]
        }

        for(let i=0; i<n; i++) {
            if(prefix[i] === suffix[i+1]) {
                return true
            }
        }
        return false
    }
}