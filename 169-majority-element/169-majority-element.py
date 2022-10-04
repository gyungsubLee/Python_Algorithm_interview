class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = collections.defaultdict(int)
        for n in nums:
            dic[n] += 1
        
        mid = len(nums) // 2
        for n in dic:
            if dic[n] > mid:
                return n