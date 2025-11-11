class Solution {
    getSecondLargest(arr) {
        
        if (arr.length === 0) return -1
        if (arr.length === 1) return arr[0]
        // code here
        let largest = arr[0]
        let secondLargest = -Infinity
        
        for (let i=0; i<arr.length;i++) {
            if (arr[i] > largest) {
                secondLargest = largest;
                largest = arr[i]
            }
        }
        
        if (secondLargest === -Infinity) {
            return -1
        }
        
        return secondLargest
    }
}