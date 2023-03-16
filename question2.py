# Reverse a linked list in groups of given size

class Node:
    def __init__(self,data):
        self.data= data
        self.ref = None
    
class linkedlist:
    def __init__(self):
        self.head = None

    def add(self,data):                          
        new_node = Node(data)
        new_node.ref = self.head                 
        self.head = new_node
    
    def display(self):
        if self.head is None:
            print("Linkedlist is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
    def rev_in_group(self,head,k):
        if head == None:
            return None
        prev = None
        current = head
        next = None
        count = 0

        while current is not None and count< k:
            next = current.ref
            current.ref = prev
            prev = current
            current = next
            count += 1
        if next is not None:
            head.ref = self.rev_in_group(next, k)
        return prev
    
    
l2 = linkedlist()
l2.add(2)
l2.add(4)
l2.add(6)
l2.add(8)
print("Original linked list")
l2.display()

# l2.rev_in_group_of(2)
print("Reversed linked list")

l2.head = l2.rev_in_group(l2.head, 2)
l2.display()
