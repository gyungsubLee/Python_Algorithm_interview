# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root):
        def dfs(root):
            if not root:
                return 0, 0
            l1, l2 = dfs(root.left)
            r1, r2 = dfs(root.right)        
            l2 = 1 + l2 if root.left and root.left.val == root.val else 0
            r2 = 1 + r2 if root.right and root.right.val == root.val else 0
            return max(l1, r1, l2 + r2), max(l2, r2)
        return dfs(root)[0]    