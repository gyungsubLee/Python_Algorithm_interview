# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        q, sum = collections.deque([root]), 0
        while q:
            node = q.popleft()
            if node:
                if node.val > low:
                    q.append(node.left)
                if node.val < high:
                    q.append(node.right)
                if low <= node.val <= high:
                    sum += node.val
        return sum