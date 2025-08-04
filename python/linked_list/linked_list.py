class Node:
    def __init__(self, data):
      self.data = data
      self.next = None
      
class LinkedList:
  def __init__(self):
     self.head = None
     
  def append(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    last_node = self.head
    while last_node.next:
      last_node = last_node.next
    last_node.next = new_node
  
  def print_list(self):
    if self.head is None:
      print("No nodes in the list");
    else:
      last = self.head
      while last:
        print(last.data);
        last = last.next;
  
  def prepend(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      new_node.next = self.head;
      self.head = new_node
      
  def insert_after_node(self, prev_node, data):
    if not prev_node:
      print("Previous node doesn't exist")
      return
    
    new_node = Node(data);
    new_node.next = prev_node.next;
    prev_node.next = new_node
    
  def deleteNode(self, node):
    curr = self.head;
    prev = None;
    while(curr.data != node.data):
      prev = curr
      curr = curr.next
      
    if curr is None:
      return
      
    prev.next = curr.next
    curr = None
      
  def delete_node_at_pos(self, pos):
    count=0;
    prev = None;
    curr = self.head
    
    if pos == 0:
      self.head = curr
      curr = None
      return
      
    
    while(count <= pos):
      prev = curr
      curr = curr.next
      count += 1
    prev.next = curr.next
    curr = None
  
  def length(self):
    count = 0
    curr = self.head
    while(curr.next):
      count += 1
      curr = curr.next
    return count

  def node_swap(self, key_1, key_2):
    if key_1 == key_2:
      return
    
    prev_1 = None
    curr = self.head
    while(curr and curr.data != key_1):
      prev_1 = curr
      curr = curr.next
      
    prev_2 = None
    curr_2 = self.head
    while(curr_2 and curr_2.data != key_2):
      prev_2 = curr_2
      curr_2 = curr_2.next
      
    if not curr_2 or not curr:
      return
    
    if prev_1:
      prev_1.next = curr
    else:
      self.head = curr_2
      
    if prev_2:
      prev_2.next = curr_2
    else:
      self.head =curr
    curr.next, curr_2.next = curr_2.next, curr.next

  def reverse(self):
    if not self.head.next:
      return
    prev = None
    curr = self.head
    
    while curr:    
      next = curr.next
      curr.next = prev
      prev = curr
      curr = next
    
    self.head = prev
  
  def recursive_reverse(self):
    def recursive_reverse(cur, prev):
      if not cur:
        return prev
      next = cur.next
      cur.next = prev
      prev = cur
      cur = next
      return recursive_reverse(cur, prev)
    self.head = recursive_reverse(self.head, None)