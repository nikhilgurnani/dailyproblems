'''
Daily Code Problem

Q. Given an integer k and a binary search tree, find the floor (less than or equal to) of k, and the ceiling (larger than or equal to) of k. If either does not exist, then print them as None.

Reference: https://www.geeksforgeeks.org/floor-and-ceil-from-a-bst/

'''

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __str__(self):
        return str(self.value)

def findCeilingFloor(root_node, k, floor=None, ceil=None):
    while root_node:
        if root_node.value == k:
            floor = root_node
            ceil = root_node
            break

        elif root_node.value > k:
            ceil = root_node
            root_node = root_node.left

        else: # if root_node.value <=k
            floor = root_node
            root_node = root_node.right

    print("Floor: " + str(floor))
    print("Ceil: " + str(ceil))


root = Node(8)
root.left = Node(4)
root.right = Node(12)

root.left.left = Node(2)
root.left.right = Node(6)

root.right.left = Node(10)
root.right.right = Node(14)

findCeilingFloor(root, 6)
