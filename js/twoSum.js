const twoSum = (arr, target) => {
    const hashmap = new Map()
    let count = 0;
    while(count < arr.length) {
        const number = hashmap.get(arr[count])
        if (number || number === 0) {
            return [number, count]
        }
        hashmap.set(target - arr[count], count)
    }
}