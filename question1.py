# Delete the elements in an linked list whose sum is equal to zero

class Node:
    def __init__(self,data):
        self.data= data
        self.ref = None
    
class linkedlist:
    def __init__(self):
        self.head = None

    def add(self,data):                          
        new_node = Node(data)
        new_node.ref = self.head                 # Changing the refrence or link with the previous head
        self.head = new_node
    
    def display(self):
        if self.head is None:
            print("Linkedlist is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
    
    def remove_zero_sum(self):
        dummy = Node(0)
        dummy.ref = self.head
        prefix_sum = 0
        seen = {0: dummy}
        current = self.head

        while current:
            prefix_sum += current.data
            seen[prefix_sum] = current
            current = current.ref

        prefix_sum = 0
        current = dummy

        while current:
            prefix_sum += current.data
            if prefix_sum in seen:
                current.ref = seen[prefix_sum].ref
            current = current.ref

        self.head = dummy.ref

obj = linkedlist()
obj.add(10)
obj.add(20)
obj.add(-30)
obj.add(30)
obj.add(20)
obj.add(10)
print("Original linked list")
obj.display()

print("\nFinal linked list")
obj.remove_zero_sum()
obj.display()
