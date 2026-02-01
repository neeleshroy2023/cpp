def two_sum(arr, target):
    n = len(arr)
    if n < 2:
        return arr
    left = 0
    right = n - 1
    while left < right:
        sum = arr[left] + arr[right]
        if sum == target:
            return [arr[left], arr[right]]
        elif sum < target:
            left+=1
        else:
            right-=1
    return arr

print(two_sum([1, 2, 4, 5, 7, 11, 15], 9))

def reverse_vowels(str):
    n = len(str)
    if n < 2:
        return str
    arr = list(str)
    left = 0
    right = n - 1
    def vowel_condition(char):
        return char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'

    while left < right:
        print(left)
        while left < right and arr[left] and not vowel_condition(arr[left]):
            left+=1
        while left < right and arr[right] and not vowel_condition(arr[right]):
            right-=1
        if left >= right:
            break
        arr[left], arr[right] = arr[right], arr[left]
        left+=1
        right-=1
    
    return ''.join(arr)

print(reverse_vowels("hello"))

def sort_zero_one(arr):
    n = len(arr)
    if n < 2:
        return arr
    left = 0
    right = n -1
    while left < right:
        while left < right and arr[left] == 0:
            left+=1
        while left < right and arr[right] == 1:
            right-=1
        if left >= right:
            break
        arr[left], arr[right] = arr[right], arr[left]
        left+=1
        right-=1
    return arr

print(sort_zero_one([1,1,1,1,1,0,0,1,0,0,0,1,1,1,1,0,1]))

def pair_target_sum(arr, k):
    n = len(arr)
    if n < 2:
        return 0
    arr.sort()
    left=0
    right = n-1
    min_diff = 100
    potential = [0, 0]
    while left < right:
        sum = arr[left] + arr[right]
        difference = abs(k - sum)
        if difference < min_diff:
            min_diff = difference
            potential[0] = arr[left]
            potential[1] = arr[right]
            right-=1
        elif difference > min_diff:
            left+=1
        else:
            return [arr[left], arr[right]]
    return potential
        
print(pair_target_sum([10, 30, 20, 5], 34))

def square_and_sort(arr):
    n = len(arr)
    if n < 2:
        return 0
    result = [0] * len(arr)
    idx = n - 1
    left = 0
    right = n - 1
    while left < right or idx >= 0:
        left_square = arr[left] * arr[left]
        right_square = arr[right] * arr[right]
        if left_square > right_square:
            result[idx] = left_square
            left+=1
        else:
            result[idx] = right_square
            right-=1
        idx-=1
    return result

print(square_and_sort([-4, -1, 0, 3, 10]))

        