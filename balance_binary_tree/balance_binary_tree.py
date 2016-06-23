# leetcode 110, Balanced Binary Tree
# the coding style is very weird
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def checkBalance(self, root):
        if not root:
            return True, 0
        
        leftCheck, leftHeight = self.checkBalance(root.left)
        rightCheck, rightHeight = self.checkBalance(root.right)
        if leftCheck and rightCheck and abs (leftHeight - rightHeight) <= 1:
            return True, max(leftHeight + 1, rightHeight + 1)
        return False, max(leftHeight + 1, rightHeight + 1)

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        check, height = self.checkBalance(root)
        return check
