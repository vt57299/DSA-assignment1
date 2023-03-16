# Merge a linked list into another linked list at alternate positions.
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
    
    
    def merge_alternate(self, list2):                  #taking parameter for 2nd linked list
        curr1 = self.head                              # Head of first linked list
        curr2 = list2.head                             # Head of second linked list
        while curr1 is not None and curr2 is not None:                        # Looping till either of list gets empty
            next1 = curr1.ref                              
            next2 = curr2.ref

            curr1.ref = curr2
            curr2.ref = next1
            
            curr1 = next1
            curr2 = next2
        list2.head = curr2                             # Adding remaining nodes to to the 

# Creating first linked list
l1 = linkedlist()
l1.add(1)
l1.add(3)
l1.add(5)
print("First Linked List:")
l1.display()

# Creating second linked list
l2 = linkedlist()
l2.add(2)
l2.add(4)
l2.add(6)
print("Second Linked List:")
l2.display()

# Merging both linked lists
l1.merge_alternate(l2)
print("Merged Linked List:")
l1.display()
