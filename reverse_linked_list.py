class Node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        print(self.val)



def reverseList(root):
    if root.next is None:
        return root

    root = reverseList(root.next)

    return root

root = Node(5)
root.next = Node(4)
root.next.next = Node(3)
root.next.next.next = Node(2)

print(reverseList(root))