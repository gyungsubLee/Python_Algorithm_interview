class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(path, index):
            res.append(path)
            if not nums:
                return 
            for i in range(index, len(nums)):
                dfs(path+[nums[i]], i+1)
        
        res=[]
        dfs([], 0)
        return res
        