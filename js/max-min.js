function max_min(arr) {
    if (arr.length <= 1) {
        return {
            min: arr[0],
            max: arr[0]
        }
    }

    let min = Infinity;
    let max = -Infinity;
    let count = 0;
    while (count < arr.length - 1) {
        if (arr[count+1] > arr[count]) {
            if (arr[count + 1] > max) {
                max = arr[count + 1]
            }
        } else {
            if (arr[count + 1] < min) {
                min = arr[count + 1]
            }
        }

        count += 2
    }

    return {
        min,
        max
    }
}