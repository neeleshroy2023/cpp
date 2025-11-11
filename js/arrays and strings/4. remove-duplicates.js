class Solution {
    // Function to remove duplicates from the given array.
    removeDuplicates(arr) {
        // code here
        if (arr.length <= 1) return arr; 
        const hash = {}
        
        for(let i=0; i < arr.length; i++) {
            if (!hash[arr[i]]) {
                hash[arr[i]] = true
            } else {
                arr[i] = false
            }
        }
        
        return arr.filter(Boolean);
    }
}
