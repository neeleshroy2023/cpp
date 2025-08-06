import linked_list

ll1 = linked_list.LinkedList()
ll2 = linked_list.LinkedList()

ll1.append(1)
ll1.append(5)
ll1.append(6)
ll1.append(8)

ll2.append(2)
ll2.append(3)
ll2.append(4)
ll2.append(7)

curr_1 = ll1.head
curr_2 = ll2.head

ll3 = linked_list.LinkedList()

while curr_1 or curr_2:
  if curr_1.data > curr_2.data:
    ll3.append(curr_2.data)
    curr_2 = curr_2.next
  elif curr_1.data < curr_2.data:
    ll3.append(curr_1.data)
    curr_1 = curr_1.next
  elif curr_1.data == curr_2.data:
    ll3.append(curr_1.data)
    ll3.append(curr_2.data)
    curr_1 = curr_1.next
    curr_2 = curr_2.next

while curr_1:
  ll3.append(curr_1.data)
  curr_1 = curr_1.next

while curr_2:
  ll3.append(curr_2.data)
  curr_2 = curr_2.next

print(ll3.print_list())