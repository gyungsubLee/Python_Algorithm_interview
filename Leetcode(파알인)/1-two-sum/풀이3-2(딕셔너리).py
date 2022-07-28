class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        # for문 통합
        for i, n in enumerate(nums):
            if target-n in num_map:
                return [num_map[target-n], i]
            num_map[n]=i
        