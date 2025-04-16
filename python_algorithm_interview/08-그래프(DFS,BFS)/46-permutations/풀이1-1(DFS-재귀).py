class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res) # path 초기화: [] (str('')으로 하여 error)
        return res
    
    def dfs(self, _nums, path, res):
        if not _nums:
            res.append(path)
            
        for i in range(len(_nums)):
            self.dfs(_nums[i+1:]+_nums[:i], path+[_nums[i]], res) # [1] + [2] = [1, 2]