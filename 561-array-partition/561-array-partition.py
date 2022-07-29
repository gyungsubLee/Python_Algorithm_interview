class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        pair = []
        sum = 0
        nums.sort()
        
        for n in nums:
            pair.append(n)
            if len(pair) == 2:
                sum += pair[0]
                pair = []
            
        return sum