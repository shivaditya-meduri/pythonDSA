# Implementation of stack data structure in Python using Lists where the last element of the list is the top of the stack for O(1) popping and pushing without reindexing

class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
         return self.stack_list.pop()
 
            
            
            
my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
