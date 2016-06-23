# leetcode 129, Sum Root to Leaf Numbers
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.pathsum = 0
        if not root:
            return self.pathsum
        self.dfs(root, str(root.val))
        return self.pathsum
        
    def dfs(self, root, path):
        if not root.left and not root.right:
            self.pathsum += int(path)

        if root.left:
            self.dfs(root.left, path + str(root.left.val))
        if root.right:
            self.dfs(root.right, path + str(root.right.val))
