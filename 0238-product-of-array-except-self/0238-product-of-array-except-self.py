class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        length = len(nums)
        
        p = 1
        for i in range(length):
            res.append(p)
            p = p * nums[i]
        
        p = 1
        for i in reversed(range(length)):
            res[i] = p * res[i]
            p = p * nums[i]
        
        return res
            
            