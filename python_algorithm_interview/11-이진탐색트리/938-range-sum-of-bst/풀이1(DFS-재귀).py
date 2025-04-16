# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 내 풀이  [ runtime: 454, memory: 23MB ]
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


# 책 풀이1(DFS-재귀) [ runtime: 475, memory: 23.1MB ]
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        return (root.val if low <= root.val <= high else 0) + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)

# 책 풀이2(DFS-재귀_가지치기)  [ runtime: 202, memory: 23MB ]
# 이진 탐색 트리(BST)는 왼쪽이 항상 작고, 오른 쪽이 항상 크다.
#  -> 현재 노드가 low보다 작은 경우, 더이상 왼쪽 가지는 탐색할 필요가 없기 때문에 오른쪽만 탐색하도록 재귀 호출 처리한다.
#  -> (high 경우도 같음)
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0

            if node.val < low:
                return dfs(node.right)
            elif node.val > high:
                return dfs(node.left)
            return node.val + dfs(node.left) + dfs(node.right)
        
        return dfs(root)