class Solution:
    def binary_search(self, nums:List[int], target: int, left, right)->int:
        if left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                return self.binary_search(nums, target, mid+1, right)
            elif nums[mid] > target:
                return self.binary_search(nums, target, left, mid-1)
            else:
                return mid
        else: 
            return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            nums = matrix[i]
            if self.binary_search(nums, target, 0, len(nums)-1) != -1:
                return True
        return False
    
            