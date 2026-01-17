class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def build(arr):
    dummy = ListNode()
    curr = dummy
    for value in arr:
        curr.next = ListNode(value)
        curr = curr.next
    return dummy.next

def printLL(head):
    while head:
        print(head.val, " => ")
        head = head.next

# ------------------------ Definations ------------------------------------------------------

# Kth from end
def findKFromEnd(head, k):
    slow = fast = head

    for _ in range(k):
        fast = fast.next

    while fast:
        fast = fast.next
        slow = slow.next
    return slow.val

# Remove Kth from end
def removeKFromEnd(head, k):
    slow = fast = head
    prev = None

    for _ in range(k):
        fast = fast.next

    while fast:
        fast = fast.next
        prev = slow
        slow = slow.next
    
    prev.next = slow.next
    return head

# Find Mid using Gap
def findMid(head):
    slow = fast = head
    count = 0
    temp = head
    while temp:
        count += 1
        temp = temp.next
    mid = count // 2

    for _ in range(mid):
        fast = fast.next
    
    while fast.next:
        fast = fast.next
        slow = slow.next

    return slow.val

# ------------------------ Drivers ------------------------------------------------------

arr = [10, 20, 30, 40, 50 ,60, 70]
ll1 = build(arr)

print(findKFromEnd(ll1, 3))
print("-----------")
print(findMid(ll1))
print("-----------")
printLL(removeKFromEnd(ll1, 3))
