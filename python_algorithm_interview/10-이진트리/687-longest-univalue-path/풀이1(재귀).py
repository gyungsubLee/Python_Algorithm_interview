# 풀이1 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    result: int = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            if node is None:
                return 0

            # 존재하지 않는 노드까지 DFS 재귀 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 현재 노드가 자식 노드와 동일한 경우 거리 1 증가
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            # 왼쪽, 오른쪽 자식 노드간 거리의 합 최대값이 결과
            self.result = max(self.result, left + right)
            # 자식 노드 상태값 중 큰 값 리턴
            return max(left, right)

        dfs(root)
        return self.result



# 풀이 2
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