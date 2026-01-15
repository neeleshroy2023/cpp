class ListNode:
    def __init__(self, val = 0, next = None):
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


# ------------------------ Definations ------------------------------------------------------


# Find middle
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.val

# has_cycle
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if (slow == fast):
            return True
    return False

# Find second middle in even-length list
def second_middle(head):
    slow = fast = head
    prev = ListNode()
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return prev.val
    return prev.val

# Find length of cycle
def cycle_length(head):
    slow = fast = head
    count = 0
    hasCycle = False
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            hasCycle = True
            break
    if not hasCycle:
        return 0
    curr = slow.next
    while curr.next != slow.next:
        count += 1
        curr = curr.next
    return count

# Find entry point of a cycle
def cycle_entry(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow.next.val
    return None

# Check if list has odd or even length

# Find 1/3rd point of list
def one_third_point(head):
    slow = fast = head
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next.next
    return slow.val

# Find 2/3rd point of list
def two_third_point(head):
    slow = fast = head
    while fast and fast.next and fast.next.next:
        slow = slow.next.next
        fast = fast.next.next.next
    return slow.val

# Find distance between slow and fast meeting point
def distance(head):
    slow = fast = head
    distance_count = 0
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        distance_count += 1
        if slow == fast:
            return distance_count
    return 0

# Split list into two halves
def half_list(head):
    print("-------")
    slow = fast = head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    ll2 = prev.next
    prev.next = None
    ll1 = head

    printLL(ll1)
    print("--------")
    printLL(ll2)
    

# --------------------------- Executions ---------------------------------------------------

# static linkedlist
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
ll = build(arr)

# cycled linkedlist
head1 = build([1,2,3,4,5])
n1 = head1
n2 = n1.next
n3 = n2.next
n4 = n3.next
n5 = n4.next
n5.next = n3
# middle
print(find_middle(ll))

# detect cycle

print(has_cycle(head1))

# second middle element
print(second_middle(ll))

# cycle length
print(cycle_length(head1))

# cycle start
print(cycle_entry(head1))

# one-third
print(one_third_point(ll))

# two-third
print(two_third_point(ll))

# distance
print(distance(head1))

# Split list into two halves
half_list(ll)



