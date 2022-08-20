class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # stack
        res = []
        stack = [(candidates, target, [])] # initialize

        while stack:
            nums, _target, path = stack.pop()
            if _target < 0:
                continue
            if _target == 0:
                res.append(path)
                continue
            
            for i in range(len(nums)):
                stack.append((nums[i:], _target-nums[i], path+[nums[i]]))
        
        return res
    