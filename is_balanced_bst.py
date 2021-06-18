"""
Check if a Binary Tree is a Balanced binary Tree
"""
class Node:
    def __init__(self, info, left=None, right=None):
        super().__init__()
        self.info = info
        self.left = left
        self.right = right

def height(root):
    if root is None:
        return -1

    return max(height(root.left), height(root.right)) + 1

def isBalanced(root):
    if root is None:
        return True

    leftHeight = height(root.left)
    rightHeight = height(root.right)

    if (abs(leftHeight - rightHeight) <= 1) and (isBalanced(root.left)) is True and (isBalanced(root.right)) is True:
        return True
    else:
        return False

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(8)

print(isBalanced(root))