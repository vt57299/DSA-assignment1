# Delete the elements in an linked list whose sum is equal to zero

class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def display(self):
        if self.head is None:
            print("LinkedList is empty!!!")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
    
    def insert(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def delete(self):
        if self.head is None:
            print("linkedlist is empty so, can't delete the element!!!")
        else:
            self.head = self.head.ref
    def delete_sum_zero(self):
        if self.head is None:
            print("linkedlist is empty so, can't delete the element!!!")
        else:
            self

obj= LinkedList()
obj.insert(10)
obj.insert(20)
obj.insert(30)
obj.delete()
obj.display()