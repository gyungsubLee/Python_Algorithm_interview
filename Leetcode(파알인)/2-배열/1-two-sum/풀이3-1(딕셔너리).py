class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, n in enumerate(nums):
            num_map[n] = i
            
        for i, n in enumerate(nums):
            if target - n in num_map and i != num_map[target-n]:
                return [i, num_map[target-n]]