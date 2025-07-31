class Stack():
  def __init__(self):
    self.items = []
    
  def peek(self):
    if len(self.items == 0): return None;
    return self.items[-1];
  
  def push(self, item):
    self.items.append(item);
    return self.size();
  
  def pop(self):
    if self.isEmpty(): 
      return None;
    self.items.pop();
    return self.size();
  
  def isEmpty(self):
    if self.size() == 0: 
      return True
    return False
  
  def size(self):
    return self.size();
  