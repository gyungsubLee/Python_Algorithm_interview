class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, path):
            if not nums:
                res.append(path)
            #     return
            # for i in range(len(nums)):
            #     dfs(nums[i+1:]+nums[:i], path+[nums[i]])   

            else:
                for i in range(len(nums)):
                    dfs(nums[i+1:]+nums[:i], path+[nums[i]])

        res = []
        dfs(nums, [])
        return res
        
                