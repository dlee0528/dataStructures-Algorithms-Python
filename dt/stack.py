'''
 python list will double its size when we attemp to insert an element at an index 
 greater than the default size of the array.
 This can waste memoery - popping empty slots..
 So, collections.deque (linked list) is recommended
'''

s = []
s.append('https://www.google.ca')
s.append('https://www.cbc.ca')
s.append('https://www.youtube.ca')
print(s)
print(s.pop())
print(s[-1]) # get the last one
print(s)

from collections import deque
stack = deque()
stack.append('https://www.google.ca')
stack.append('https://www.cbc.ca')
stack.append('https://www.youtube.ca')
print(stack)


class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self, val):
        self.container.append(val)
    
    def pop(self):
        self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)
    
s = Stack()
s.push("s")
s.push("t")
s.push("a")
s.push("c")
s.push("k")
print('initial Stack\n', s.container)
print(s.peek())
print(s.is_empty())