class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        stack=[(nums, [])]
        while stack:
            _nums, path = stack.pop()
            if not _nums:
                res.append(path)
                continue
            for i in range(len(_nums)):
                stack.append((_nums[i+1:]+_nums[:i], path+[_nums[i]]))
        return res