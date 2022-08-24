class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(nums, target, path):
            if target < 0:
                return
            if target == 0:
                res.append(path)
            
            for i in range(len(nums)):
                dfs(nums[i:], target-int(nums[i]), path+[nums[i]])
                
        res = []
                
        dfs(candidates, target, [])
        return res
        
    