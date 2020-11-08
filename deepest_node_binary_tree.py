"""
You are given the root of a binary tree. Return the deepest node (the furthest node from the root).

Example:

    a
   / \
  b   c
 /
d

Preorder => a b d c
Postorder => d b c a
Inorder => d b a c

    a
   / \
  b   c
 /     \
d       e
         \
          f


The deepest node in this tree is d at depth 3.

https://www.geeksforgeeks.org/find-deepest-node-binary-tree/
"""


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return self.val

def height(root):
    if root is None:
        return 0

    return max( height(root.left), height(root.right) ) + 1

depth = 1

def deepest(node, level):
    global depth
    if node is None:
        return

    if level == 1:
        print( (depth, node.val) )
    else:
        depth += 1
        deepest( node.left, level - 1 )
        deepest( node.right, level - 1 )



root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.right = Node('c')

levels = height( root )

deepest(root, levels)
# (d, 3)
