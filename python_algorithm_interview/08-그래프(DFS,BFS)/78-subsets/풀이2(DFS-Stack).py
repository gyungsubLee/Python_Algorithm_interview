# index
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        stack=[(0, [])]
        while stack:
            start, path = stack.pop()
            res.append(path)
            # if start >= len(nums): continue 없어도 문제 없음.
            for i in range(start, len(nums)):
                stack.append((i+1, path+[nums[i]]))
        return res