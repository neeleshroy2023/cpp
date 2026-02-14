from collections import defaultdict
import heapq

# Given an array, return a dictionary of element → count.
def frequency_count(arr):
    d = defaultdict(int)
    for item in arr:
        d[item] += 1
    return d

print(frequency_count([1,1,2,3]))

def first_non_repeating(arr):
    d = defaultdict(int)
    for item in arr:
        d[item] += 1
    for key, value in d.items():
        if value == 1:
            return key
    return -1
print(first_non_repeating([4,5,1,2,0,4]))

def majority_element(arr):
    n = len(arr)
    m = n // 2
    d = defaultdict(int)
    for item in arr:
        d[item] += 1
    
    for key, value in d.items():
        if value > m:
            return key
    return -1

print(majority_element([2,2,1,1,1,2,2]))

# Check If Two Arrays Are Equal
def isEqual(arr1, arr2):
    if (len(arr1) != len(arr2)):
        return False
    d = defaultdict(int)

    for item in arr1:
        d[item] += 1
    
    for item in arr2:
        if item in d:
            if d[item] > 0:
                d[item] -= 1
            if d[item] == 0:
                del d[item]
        else:
            return False
        
    if len(d) == 0: 
        return True
    return False

print(isEqual([1,2,2,3], [2,1,3,2]))

# Top K frequent elements
def topKFrequent(arr, k):
    d = defaultdict(int)
    for item in arr:
        d[item] += 1
    
    pq = []
    for key, freq in d.items():
        heapq.heappush(pq, [freq, key])

        if (len(pq) > k):
            heapq.heappop(pq)
    
    res = []
    temp = [0] * len(pq)
    index = len(pq) - 1

    while pq:
        temp[index] = heapq.heappop(pq)[1]
        index -= 1
    for val in temp:
        res.append(val)
    return res

print(topKFrequent([3, 1, 4, 4, 5, 2, 6, 1], 2))