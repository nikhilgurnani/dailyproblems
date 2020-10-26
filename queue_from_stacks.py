"""
Implement a queue class using two stacks. A queue is a data structure that supports the FIFO protocol (First in = first out). Your class should support the enqueue and dequeue methods like a standard queue.

Queue =>
1 2 3 => Added from back, deleted from front
In
1
2
3
Out
1
2
3

Stack =>
3 2 1 => added from front, deleted from front
In
1
2
3
Out
3
2
1

"""



class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, val):
        while len(self.s1) != 0:
            self.s2.append( self.s1[-1] )
            self.s1.pop()
        self.s1.append(val)
        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

    def dequeue(self):
        return self.s1.pop()

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print (q.dequeue())
print (q.dequeue())
print (q.dequeue())
# 1 2 3
