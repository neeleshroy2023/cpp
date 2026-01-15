
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build(arr):
    dummy = ListNode()
    curr = dummy
    for x in arr:
        curr.next = ListNode(x)
        curr = curr.next
    return dummy.next

def printLL(head):
    while head:
        print(head.val, " -> ")
        head = head.next
    print("None")

arr = [10,20,34,47,59,69]
ll = build(arr)
print("printing LL: ", printLL(ll))

# Length of linkedList
def LLlength(head):
    count = 0
    while head:
        count+=1
        head = head.next
    return

print("LLlength", LLlength(ll))

# Find Kth node from start
def findKthNode(head, k):
    count = 0
    while(head):
        count += 1
        if (count == k):
            return head.val
        head = head.next
    return 0

print("findKthNode", findKthNode(ll, 3))

# Max element
def maxElement(head):
    maxi = head.val
    while head:
        maxi = max(maxi, head.val)
        head = head.next
    return maxi
    
print("maxElement", maxElement(ll))

# Min element
def minElement(head):
    mini = head.val
    while head:
        mini = min(mini, head.val)
        head = head.next
    return mini
    
print("minElement", minElement(ll))

# First occurence element
def firstOccurence(head, k):
    count = 0
    while head:
        if k == head.val:
            break
        head = head.next
        count += 1
    return count
    
print("firstOccurence", firstOccurence(ll, 34))

# Last occurence element
def lastOccurence(head, k):
    count = 0
    occurence = count;
    while head:
        if k == head.val:
            occurence = count
        head = head.next
        count += 1
    return count
    
print("lastOccurence", lastOccurence(ll, 34))

# Sum of all nodes
def nodeSum(head):
    sum = 0
    while head:
        sum += head.val
        head = head.next
    return sum
    
print("nodeSum", nodeSum(ll))

# Average of all nodes
def nodeAverage(head):
    sum = 0
    count = 0
    while head:
        sum += head.val
        count += 1
        head = head.next
    return sum//count
    
print("nodeAverage", nodeAverage(ll))

# Count Even numbers
def countEven(head):
    count = 0
    while head:
        if (head.val % 2 == 0):
            count += 1
        head = head.next
    return count
    
print("countEven", countEven(ll))

# Count Odd numbers
def countOdd(head):
    count = 0
    while head:
        if (head.val % 2 != 0):
            count += 1
        head = head.next
    return count
    
print("countOdd", countOdd(ll))

# Copy LinkedList to Array
def copyToArray(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr
    
print("copyToArray", copyToArray(ll))

# Check if sorted
def checkIfSorted(head):
    curr = head.val
    while head:
        if (curr > head.val):
            return False
        curr = head.val
        head = head.next
    return True
    
print("checkIfSorted", checkIfSorted(ll))

# Compare for equality
def compareEquality(head1, head2):
    ll1Length = LLlength(head1)
    ll2Length = LLlength(head2)
    if ll1Length != ll2Length:
        return False
    while head1:
        if (head1.val != head2.val):
            return False
        head1 = head1.next
        head2 = head2.next
    return True

arr1 = [10, 20, 30, 80, 50]
arr2 = [10, 20, 30, 40, 50]
ll1 = build(arr1)
ll2 = build(arr2)
print("compareEquality", compareEquality(ll1, ll2))