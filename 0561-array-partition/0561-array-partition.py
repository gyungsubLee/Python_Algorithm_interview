class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res, odd, even =0, 0, 1
        lenght = len(nums)
        
        # 짝수
        if lenght % 2 == 0:
            while odd < lenght:
                res += nums[odd]
                odd += 2
            return res
        
        # 홀수
        if lenght % 2 == 1:
            while even < lenght:
                res += nums[even]
                even += 2
            return res
            
