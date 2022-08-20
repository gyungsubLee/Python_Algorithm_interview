# index
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        stack=[(0, [])]
        while stack:
            start, path = stack.pop()
            res.append(path)
            for i in range(start, len(nums)):
                stack.append((i+1, path+[nums[i]]))
        return res
        