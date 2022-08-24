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
        