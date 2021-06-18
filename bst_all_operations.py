"""
Write all operations on a Binary Search Tree
"""

class Node:
    def __init__(self, info, left=None, right=None):
        super().__init__()
        self.info = info
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self, root):
        super().__init__()
        self.root = root

    def contains(self, info):
        ptr = self.root

        while ptr != None:
            if ptr.info == info:
                return True
            if ptr.info > info:
                ptr = ptr.left
            else:
                ptr = ptr.right
        return False

    def add(self, info):
        ptr = self.root
        while ptr != None:
            if ptr.info < info:
                if ptr.right is None:
                    ptr.right = Node(info)
                    break
                ptr = ptr.right
            else:
                if ptr.left is None:
                    ptr.left = Node(info)
                    break
                ptr = ptr.left


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.info, end=" ")
    inorder(root.right)
def preorder(root):
    if root is None:
        return
    print(root.info, end=" ")
    preorder(root.left)
    preorder(root.right)
def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.info, end=" ")

root = Node(5)
bst = BinarySearchTree(root)
bst.add(4)
bst.add(6)
bst.add(3)
bst.add(7)
inorder(root)
print("")
preorder(root)
print("")
postorder(root)
print("")
print(bst.contains(5))
print(bst.contains(10))