from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)
        
        route=[]
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)
        
        dfs('JFK')
        return route[::-1]