
class Solution:
    def insertAVL(self, items, threshold):
        '''
        :type items: list of int
        :type threshold: int
        :rtype: TreeNode
        '''

        root = AVLTree(items[0])

        for i in range(1, len(items)):
            root = self.insert(root, items[i], threshold)

        return root

    def inorder(self, root):
        if root == None:
            return

        self.inorder(root.left)
        print(root.val)
        self.inorder(root.right)

    def insert(self, root, info, threshold):
        if root == None:
            return AVLTree(info)

        if info < root.val:
            root.left = self.insert(root.left, info, threshold)
        else:
            root.right = self.insert(root.right, info, threshold)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > threshold:
            if self.get_balance(root.left) >= 0:
                root = self.rotate_right(root)
            else:
                root = self.rotate_left_right(root)
        elif balance < -threshold:
            if self.get_balance(root.right) <= 0:
                root = self.rotate_left(root)
            else:
                root = self.rotate_right_left(root)

        return root

    def rotate_right(self, root):
        left_temp = root.left

        root.left = left_temp.right
        left_temp.right = root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        left_temp.height = 1 + max(self.get_height(left_temp.left), self.get_height(left_temp.right))

        return left_temp

    def rotate_left(self, root):
        right_temp = root.right

        root.right = right_temp.left
        right_temp.left = root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        right_temp.height = 1 + max(self.get_height(right_temp.left), self.get_height(right_temp.right))

        return right_temp

    def rotate_left_right(self, root):
        root.left = self.rotate_left(root.left)

        return self.rotate_right(root)

    def rotate_right_left(self, root):
        root.right = self.rotate_right(root.right)

        return self.rotate_left(root)


    def get_balance(self, node):
        if node == None:
            return 0

        return self.get_height(node.left) - self.get_height(node.right)

    def get_height(self, node):
        if node == None:
            return -1

        return node.height

class AVLTree:
    def __init__(self, info):
        self.val = info
        self.height = 0
        self.left = None
        self.right = None

root = Solution().insertAVL([3,1,2], 1)
print(Solution().inorder(root))