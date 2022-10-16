class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, n in enumerate(nums):
            another_n = target - n
            
            if another_n in dic:
                return [i, dic[another_n]]
            
            if n not in dic:
                dic[n] = i
            dic[n] = i
        