import linked_list

ll = linked_list.LinkedList()

ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)

p = ll.head
q = ll.head

count = 1
while count <= 2:
  q = q.next
  count += 1
  
while q:
  q = q.next
  p = p.next
  
print(p.data)