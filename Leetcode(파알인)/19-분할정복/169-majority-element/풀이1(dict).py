class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = collections.defaultdict(int)
        half = len(nums) // 2
        for n in nums:
            dic[n] += 1
            if dic[n] > half:
                return n
