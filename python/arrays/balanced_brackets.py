class Node:
    def __init__(self, data):
      self.data = data;
      self.next = None;
      
class LinkedList:
  def __init__(self):
     self.head = None;
     
  def append(self, data):
    new_node = Node(data)
    if self.head is not None:
      self.head = new_node
    else:
      last_node = self.head;
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
      
    
    