# Author: Jeffrey Jacob
# Date: 11/17/2022
# Program: my implementation of a stack
# Inputs: stuff like any object really
# Outputs: other stuff anything that can go in a list

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        return False

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

