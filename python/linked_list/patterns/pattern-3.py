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

# Find intersection
def intersection(head1, head2):
    ptr1, ptr2 = head1, head2
    while ptr1 != ptr2:
        ptr1 = head2 if ptr1 is None else ptr1.next
        ptr2 = head1 if ptr2 is None else ptr2.next
        
    return ptr1.val

# Are lists merging?
def is_merging(head1, head2):
    ptr1, ptr2 = head1, head2
    while ptr1 != ptr2:
        ptr1 = head2 if ptr1 is None else ptr1.next
        ptr2 = head1 if ptr2 is None else ptr2.next
    if ptr1 is None and ptr2 is None:
        return False
    return True

# Remove nth node
def remove_nth_node(head, n):
    ptr = head
    prev = None
    while n > 1:
        prev = ptr
        ptr = ptr.next
        n -= 1
    prev.next = ptr.next
    return head

# ------------------------ Drivers ------------------------------------------------------

arr = [10, 20, 30, 40, 50 ,60, 70]
ll1 = build(arr)

print(findKFromEnd(ll1, 3))
print("-----------")
print(findMid(ll1))
print("-----------")
printLL(removeKFromEnd(ll1, 3))

print("-----------")
arr1 = [1,3,1,2,4]
arr2 = [3]
ll2 = build(arr1)
ll3 = build(arr2)

head1 = ll2
ll2 = ll2.next.next.next
head2 = ll3
ll3.next = ll2

print(intersection(head1, head2))
print("-----------")

print(is_merging(head1, head2))
print("-----------")

ll1 = build(arr)
printLL(remove_nth_node(ll1, 3))
print("-----------")

