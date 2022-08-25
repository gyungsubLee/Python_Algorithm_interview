class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)
            
        def dfs(n):
            if visit[n] == -1: return False
            if visit[n] == 1: return True
            visit[n] = -1
            for _n in graph[n]:
                if not dfs(_n):
                    return False
            visit[n] = 1
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
