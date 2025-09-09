/*
*   Input:  presum[] = {5, 7, 10, 11, 18}
    Output: [5, 2, 3, 1, 7]
    Explanation: Original array {5, 2, 3, 1, 7} 
    Prefix sum array = {5, 5+2, 5+2+3, 5+2+3+1, 5+2+3+1+7} = {5, 7, 10, 11, 18}
    Each element of original array is replaced by the sum of the prefix of current index.

    Input: presum[] = {45, 57, 63, 78, 89, 97}
    Output: [45, 12, 6, 15, 11, 8] 
*/

const presum = [45, 57, 63, 78, 89, 97]

let curr = presum[0];
for(let i=0; i < presum.length; i++) {
    let temp = presum[i]
    presum[i] = curr;
    curr = presum[i+1] - temp
}

console.log(presum)