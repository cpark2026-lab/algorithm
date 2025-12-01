class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):                 
        new_head = Node(value)           
        new_head.next = self.head         
        self.head = new_head            

    def pop(self):
        if self.is_empty():                  
            return "empty"
        delete_head = self.head            
        self.head = self.head.next           
        return delete_head                 

    def peek(self):
        if self.is_empty():
            return "empty"

        return self.head.data

    def is_empty(self):
        return self.head is None
