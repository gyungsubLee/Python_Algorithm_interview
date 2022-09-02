# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    val:int = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if node:
                dfs(node.left)
                if low <= node.val <= high:
                    self.val += node.val
                dfs(node.right)
        
        dfs(root)
        return self.val
        