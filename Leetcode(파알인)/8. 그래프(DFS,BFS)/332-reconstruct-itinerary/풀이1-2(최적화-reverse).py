# 풀이2-1 reverse를 통한 큐 연산 처리

from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)
        
        route=[]
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop())
            route.append(a)
        
        dfs('JFK')
        return route[::-1]


# 풀이 2-2(슬라이싱)
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route = []
        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
        visit('JFK')
        return route[::-1]
