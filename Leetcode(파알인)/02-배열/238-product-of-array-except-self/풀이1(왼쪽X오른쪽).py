class Solution:
    def productExceptSelf(self, nums):
        list=[]
        p=1
        for i in range(len(nums)):
            list.append(p)
            p = p * nums[i]
        
        p=1
        for i in range(len(nums)-1, 0-1, -1):
            list[i] = list[i] * p
            p = p * nums[i]
            
        return list

b = [1, 2, 3, 4]
a = Solution()
a.productExceptSelf(b)
            