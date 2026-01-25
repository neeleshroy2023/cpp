class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def build(arr):
    dummy = Node()
    curr = dummy
    for x in arr:
        curr.next = Node(x)
        curr = curr.next
    return dummy.next

def printLL(head):
    while head:
        print(head.val, end = " => ")
        head = head.next

# ------------------------ Definations ------------------------------------------------------

# Reverse linked list
def reverseList(head):
    curr = head
    prev = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

def reverseKNodes(head, k):
    curr = head
    for _ in range(k-1):
        if not curr.next:
            return head
        curr = curr.next

    ll1 = curr.next
    curr.next = None

    current = head
    prev = None
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    head.next = ll1
    return prev
    



# ------------------------ Driver ------------------------------------------------------

arr = [10, 20, 30, 40, 50, 60]
ll = build(arr)

printLL(reverseList(ll))
print("======================")
ll = build(arr)
printLL(reverseKNodes(ll, 3))
print("======================")