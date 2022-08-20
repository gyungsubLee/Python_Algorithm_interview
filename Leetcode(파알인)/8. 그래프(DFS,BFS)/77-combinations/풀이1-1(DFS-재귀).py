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
            # i 대신 start를 잘못써서 중복인 경우까지 다 나옴
            # -> [[1,2],[1,3],[1,4],[2,2],[2,3],[2,4],[3,2],[3,3],[3,4],[4,2],[4,3],[4,4]]
            # => 생각하면서 하자...
            self.dfs(elements, i+1, k-1, n, res) 
            elements.pop()
        