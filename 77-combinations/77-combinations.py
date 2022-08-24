class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(start, k , path):
            if k == 0:
                res.append(path)
                return 
            
            for num in range(start, n+1):
                dfs(num+1, k-1, path+[num])
                
        res = []
        dfs(1, k, [])
        return res
        