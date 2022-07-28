class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        while not left == rigth: # (left == rigth) = False인 경우
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            return [left, right]
            
        return print("해당하는 요소가 없다.")
        
