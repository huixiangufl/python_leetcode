# leetcode 257, Binary Tree Paths
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        paths = []
        if not root:
            return paths
        self.dfs(root, str(root.val), paths)
        return paths
    
    def dfs(self, root, path, paths):
        if not root.left and not root.right:
            paths.append(path)
            return
        if root.left:
            self.dfs(root.left, path + '->' + str(root.left.val), paths)
        if root.right:
            self.dfs(root.right, path + '->' + str(root.right.val), paths)
