# Implement a queue using the stack data structure

class queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def isEmpty(self):
        if not self.stack1 and not self.stack2:
            return True
        else: return False
    
    def add(self,element):
        self.stack1.append(element)
    
    def remove(self):
        if self.isEmpty():
            return "queue is empty,hence cannot remove the element!!"
        else:
            if not self.stack2:
                while self.stack1:
                    self.stack2.append(self.stack1.pop())
                return self.stack2.pop()
            else:
                return self.stack2.pop()
    def peek(self):
        if self.isEmpty():
            return "queue is empty!!!"
        else:
            if not self.stack2:
                self.stack2.append(self.stack1.pop(0))
                return self.stack2[-1]
            else:
                return self.stack2[-1]
        
            
    
obj = queue()
obj.add(10)
obj.add(20)
obj.add(30)
print("Empty:",obj.isEmpty())
# print("removed:", obj.remove())
# print("removed:", obj.remove())
# print("removed:", obj.remove())
print("peek: ",obj.peek())