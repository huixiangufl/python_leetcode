# leetcode 101, symmetric tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.checkSymmetric(root.left, root.right)
    
    def checkSymmetric(self, left, right):
        if not left and not right:
            return True
        if ( left and not right ) or ( not left and right ):
            return False
        if left.val != right.val:
            return False
        return self.checkSymmetric(left.left, right.right) and self.checkSymmetric(left.right, right.left)
