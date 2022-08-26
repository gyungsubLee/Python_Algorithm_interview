# 풀이 2-1
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

# 풀이2-2
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        stack = [(1, k, [])]
        
        while stack:
            start, k, path = stack.pop()
            if k == 0:
                res.append(path)
                continue
            for num in range(start, n+1):
                stack.append((num+1, k-1, path+[num]))
        return res
        