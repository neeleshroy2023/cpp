/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let left = 0
    let right = height.length - 1
    let maxArea = 0

    while (left < right){
        let width = right - left;
        let heightForArea = Math.min(height[left], height[right])

        let area = width * heightForArea
        maxArea = Math.max(area, maxArea)

        if (height[left] > height[right]) {
            right--
        } else {
            left++
        }
    }

    return maxArea
};