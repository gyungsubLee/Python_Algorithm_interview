class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        stack = [(nums, [])]
        while stack:
            nums, path = stack.pop()
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                newNums = nums[:i] + nums[i+1:]
                stack.append((newNums, path+[nums[i]]))
        return res
                