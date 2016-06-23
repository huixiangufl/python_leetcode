# leetcode 144, binary tree preorder traversal
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        orders = []
        stack = [root]
        while stack:
            p = stack.pop()
            orders.append(p.val)
            if p.right:
                stack.append(p.right)
            if p.left:
                stack.append(p.left)
        return orders
