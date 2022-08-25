class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for fr, to in sorted(tickets, reverse=True):
            graph[fr].append(to)
        
        res = []
        def dfs(node):
            while graph[node]:
                dfs(graph[node].pop())
            res.append(node)

        dfs("JFK")
        return res[::-1]