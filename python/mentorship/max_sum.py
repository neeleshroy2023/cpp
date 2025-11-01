def max_sum(arr):
    n=len(arr)
    if n==0:
        return 0
    if n==1:
        return arr[0]
    sum = arr[0]
    left=0
    right=1
    while right < n:
        curr = sum + arr[right]
        if curr < sum:
            left = right + 1
        else:
            right += 1