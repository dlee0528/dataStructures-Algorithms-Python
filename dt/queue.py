'''
 Python Queue Types
    1. list
    2. collections.deque
    3. queue.LifoQueue
'''

# list has a problem associated with a dynamic array
# new memory area can be wasted unused
stock_price_queue = []

stock_price_queue.insert(0, 131.10)
stock_price_queue.insert(0, 131.12)
stock_price_queue.insert(0, 131.20)
stock_price_queue.insert(0, 131.19)

print(stock_price_queue)
print(stock_price_queue.pop())
print(stock_price_queue.pop())


from collections import deque

s = deque()
s.appendleft(2)
s.appendleft(50)
s.appendleft(12)
s.appendleft(4)

print(s)
print(s.pop())
print(s.pop())


class Queue:
    def __init__(self) -> None:
        self.buffer = deque()
    
    def enqueue(self,val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)
    

s1 = Queue()
s1.enqueue(1)
s1.enqueue(2)
s1.enqueue(3)
print(s1.buffer)
print(s1.dequeue())
print(s1.is_empty())