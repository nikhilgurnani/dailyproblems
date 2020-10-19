"""
# [1, 2, 3, 4, 5]

"""

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        current_node = self
        result = []
        while current_node:
            result.append(current_node.val)
            current_node = current_node.next
        return str(result)

count = 1

def remove_kth_from_linked_list(curr, k):
    global count
    if curr.next == None:
        if k == 1:
            return None
        return curr



    curr.next = remove_kth_from_linked_list(curr.next, k)

    count = count + 1

    if count == k:
        return curr.next
    else:
        return curr



head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(head)
# [1, 2, 3, 4, 5]
head = remove_kth_from_linked_list(head, 1)
print(head)
# [1, 2, 4, 5]
