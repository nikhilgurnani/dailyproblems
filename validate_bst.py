"""
You are given the root of a binary search tree. Return true if it is a valid binary search tree, and false otherwise. Recall that a binary search tree has the property that all values in the left subtree are less than or equal to the root, and all values in the right subtree are greater than or equal to the root.

    5
  /   \
 3     7
/ \   /
1  4 6

Postorder (L, R, N) => 1 4 3 6 7 5
Inorder (L, N, R) => 1 3 4 5 6 7
"""

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def inorder(root, arr):
    if root is None:
        return
    inorder( root.left, arr )
    arr.append( root.key )
    inorder( root.right, arr )

def is_bst(root):
    arr = list()
    inorder( root, arr )
    copy = arr
    copy.sort()
    return ( arr == copy )


a = TreeNode(5)
a.left = TreeNode(3)
a.right = TreeNode(7)
a.left.left = TreeNode(1)
a.left.right = TreeNode(4)
a.right.left = TreeNode(6)
print(is_bst(a))
