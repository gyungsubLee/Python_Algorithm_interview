class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(k, start, path):
            if k == 0:
                res.append(path[:])
                return
            for i in range(start, n+1):
                path.append(i)
                dfs(k-1, i+1, path)
                path.pop()
                
        res=[]
        dfs(k, 1, [])
        return res