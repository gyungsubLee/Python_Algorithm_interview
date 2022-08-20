class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        stack=[(k, 1, [])]
        while stack: 
            _k, start, path = stack.pop()
            if _k <0:
                continue
                
            if _k == 0 and len(path) == k:
                res.append(path[:])
                continue
            
            for i in range(start, n+1):
                path.append(i)
                stack.append((_k-1, i+1, path[:]))
                path.pop()
            
        return res