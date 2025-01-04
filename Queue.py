# Implemented using linked list with head as first and tail as last which will enable O(1) dequeue and enqueue methods

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

    def dequeue(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.first 
            self.first = None 
            self.last = None 
            self.length = 0
            return temp 
        else:
            temp = self.first 
            self.first = self.first.next 
            temp.next = None 
            self.length -= 1 
            return temp




my_queue = Queue(1)
my_queue.enqueue(2)
