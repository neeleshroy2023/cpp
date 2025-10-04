const reverse = (arr) => {
    if (arr.length < 2) {
        return arr
    } 

    let left = 0;
    let right = arr.length - 1

    while(left < right) {
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp

        left++
        right--
    }

    return arr
}