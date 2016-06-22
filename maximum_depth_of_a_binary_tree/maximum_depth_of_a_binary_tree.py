# leetcode 104, maximum depth of a binary tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)

# python non-recursive solution, using stack
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        stack = [(root, 1)]
        maxDepth = 1
        while stack:
            p, depth = stack[-1]
            stack.pop()
            maxDepth = max(depth, maxDepth)
            if p.right:
                stack.append((p.right, depth + 1))
            if p.left:
                stack.append((p.left, depth + 1))
        return maxDepth

# python non-recursive solution, using quuee
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        queue = [(root, 1)]
        maxDepth = 1
        while queue:
            p, depth = queue[0]
            queue.pop(0)
            maxDepth = max(depth, maxDepth)
            if p.right:
                queue.append((p.right, depth + 1))
            if p.left:
                queue.append((p.left, depth + 1))
        return maxDepth
