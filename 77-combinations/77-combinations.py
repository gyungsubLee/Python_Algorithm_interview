class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        self.dfs([], 1, k, n, res)
        
        return res
    
    def dfs(self, elements, start:int, k:int, n:int, res:List):
        if k == 0:
            res.append(elements[:])
            return
        
        for i in range(start, n+1):
            elements.append(i)
            self.dfs(elements, i+1, k-1, n, res)
            elements.pop()
        