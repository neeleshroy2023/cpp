const palindrome = (arr) => {
    const length = arr.length
    if (length === 0 || length === 1) {
        return true
    }

    let left = 0;
    let right = arr.length - 1

    let regEx = /[a-z0-9]/i

    while(left < right) {

        while (!regEx.test(arr[left])) {
            left++
        }

        while (!regEx.test(arr[right])) {
            right--
        }

        if (left >= right) {
            break;
        }
        
        if (arr[left].toLowerCase() !== arr[right].toLowerCase()) {
            return false
        }

        left++
        right--
    }

    return true
}