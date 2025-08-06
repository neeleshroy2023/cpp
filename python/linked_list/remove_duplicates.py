import linked_list

ll = linked_list.LinkedList()

ll.append(1)
ll.append(6)
ll.append(1)
ll.append(4)
ll.append(2)
ll.append(2)
ll.append(4)

mpp = dict()

curr = ll.head
prev = None
while curr:
  if curr.data in mpp:
    prev.next = curr.next
    curr = None
  else:
    mpp[curr.data] = 1
    prev = curr
  curr = prev.next
  
ll.print_list()