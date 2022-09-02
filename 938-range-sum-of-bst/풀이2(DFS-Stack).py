# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 풀이(DFS-stack-가지치기)
# 유효한 노드만 삽입 ->  가지치기 탐색
#  -> 이진 탐색 트리의 속성(val:왼쪽 -> 오른쪽 정렬)을 사용하여
#  -> node.val > low: stack.append(stack.left)
#  -> node.val < high: stack.append(stack.rihgt)
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        stack, sum = [root], 0
        while stack:
            node = stack.pop()
            if node:
                if node.val > L:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
                if L <= node.val <= R:
                    sum += node.val
        return sum