class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for fr, to, pr in flights:
            graph[fr].append((to, pr))
        vis = [0]*n
        q = [(0, src, k+1)]
        while q:
            price, node, k = heapq.heappop(q)
            if node == dst:
                return price
            if vis[node] >= k:
                continue
            vis[node] = k
            for _node, d_pr in graph[node]:
                heapq.heappush(q, (price+d_pr, _node, k-1))
        return -1
            
            