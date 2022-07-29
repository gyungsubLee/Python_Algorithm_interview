class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complate = target - n
            
            if complate in nums[i+1:]:
                return [i, nums[i+1:].index(complate)+ i+1]