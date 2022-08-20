# 풀이1-1) 슬라이싱
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, path):
            res.append(path)
            if not nums:
                return
            for i in range(len(nums)):
                dfs(nums[i+1:], path+[nums[i]])
        
        res=[]
        dfs(nums, [])
        return res

# 풀이1-2) index
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(start, path):
            res.append(path)
            for i in range(start, len(nums)):
                dfs(i+1, path+[nums[i]])

        res=[]
        dfs(0, [])
        return res
        
        