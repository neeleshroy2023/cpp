

function smallestSubarray(arr, S) {
    if (arr.length === 0) {
        return 0
    }

    if (arr[0] === S) {
        return 1
    }

    let left = 0
    let right = 1

    let windowSum = arr[left]
    let minLength = +Infinity

    while (left < right) {
        if (windowSum >= S) {
            minLength = Math.min(right - left + 1, minLength);
            windowSum -= arr[left]
            left++;
        } else {
            windowSum += arr[right]
            right++;
        }
    }

    return minLength
}