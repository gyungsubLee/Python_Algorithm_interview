# 풀이 1-1  -> 파알인 풀이
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
        

# 풀이 1-2 -> nums 복사 
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.dfs(range(1,n+1), k, [], res)
        return res
        
    def dfs(self, nums, k, path, res):
        if k == 0:
            res.append(path)
        
        if len(nums) >= k:
            for i in range(len(nums)):
                self.dfs(nums[i+1:], k-1, path+[nums[i]], res)
        return


# 풀이 1-3 (method-func)
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


# 풀이 1-4 -> start 포인터 
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
        