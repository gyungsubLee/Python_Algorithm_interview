import collections
from typing import List 

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]
        
        # 양방향 그래프 구성
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
         # 첫번째 리프 노드 추가
        leaves = []
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)
        
        # 루트 노드만 남을 때까지 반복
        while n > 2:
            n -= len(leaves)
            new_leaves=[]
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
            
        return leaves


n = 4
edges = [[1,0],[1,2],[1,3]]
a = Solution()
a.findMinHeightTrees(n, edges)
        
            