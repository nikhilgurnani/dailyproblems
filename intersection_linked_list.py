"""
You are given two singly linked lists. The lists intersect at some node. Find, and return the node. Note: the lists are non-cyclical.

Example:

A = 1 -> 2 -> 3 -> 4
B = 6 -> 3 -> 4

This should return 3 (you may assume that any nodes with the same value are the same node).

https://www.geeksforgeeks.org/write-a-function-to-get-the-intersection-point-of-two-linked-lists/
"""

def intersection(a, b):
    visited_val = {}
    ptr = a
    while ptr is not None:
        visited_val.update( { ptr.val: True } )
        ptr = ptr.next

    ptr = b

    while ptr is not None:
        if visited_val.get( ptr.val, None ):
            return ptr
        else:
            visited_val.update( { ptr.val: True } )
            ptr = ptr.next
    return None

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
    def prettyPrint(self):
        c = self
        while c:
            print(c.val)
            c = c.next

a = Node(3)
a.next = Node(6)
a.next.next = Node(9)
a.next.next.next = Node(15)
a.next.next.next.next = Node(30)

b = Node(10)
b.next = a.next.next.next

c = intersection(a, b)
c.prettyPrint()
# 3 4