class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_copy = sorted(nums)
        left, right = 0, len(nums)-1
        while not left == right:   # (left == rigth) = False인 경우
            if nums_copy[left] + nums_copy[right] < target:
                left += 1

            elif nums_copy[left] + nums_copy[right] > target:
                right -= 1

            elif nums_copy[left] != nums_copy[right]:
                return [nums.index(nums_copy[left]), nums.index(nums_copy[right])]
            
            else:
                return [nums.index(nums_copy[left]), nums.index(nums_copy[right] ,nums.index(nums_copy[left])+1]