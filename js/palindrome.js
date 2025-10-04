const palindrome = (arr) => {
    const length = arr.length
    if (length === 0 || length === 1) {
        return true
    }

    let left = 0;
    let right = arr.length - 1

    while(left < right) {
        if (arr[left] !== arr[right]) {
            return false
        }

        left++
        right--
    }

    return true
}