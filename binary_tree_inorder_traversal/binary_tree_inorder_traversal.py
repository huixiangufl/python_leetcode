# leetcode 94, binary tree inorder traversal
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        orders = []
        stack = []
        p = root
        while p:
            print p.val
            stack.append(p)
            p = p.left
            
        while stack:
            p = stack[-1]
            stack.pop()
            orders.append(p.val)
            p = p.right
            while p:
                stack.append(p)
                p = p.left
        
        return orders
