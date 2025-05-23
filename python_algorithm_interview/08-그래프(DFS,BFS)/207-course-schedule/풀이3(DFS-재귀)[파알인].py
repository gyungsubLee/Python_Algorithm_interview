from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        # 그래프 구성
        for x, y in prerequisites:
            graph[x].append(y)
        
        traced = set()
        visited = set()
        
        def dfs(i):
            # 순환구조 -> False
            if i in traced:
                return False
            
            # 이미 방문했던 노드
            if i in visited:
                return True
            
            traced.add(i)
            for y in graph[i]:
                if not dfs(y): 
                    return False
            
            # 탐색 종료 후 삭제
            traced.remove(i)
            # 탐색 종료 후 방문 노드 추가
            visited.add(i)
            
            return True
            
        # 순환 구조 판별
        for x in list(graph):
            if not dfs(x):
                return False
        
        return True
            