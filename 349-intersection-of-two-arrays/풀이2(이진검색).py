# Binary Search: 재귀 구현
# 시간복잡도: O(nlogN)
class Solution:
    def binary_serch(self, nums: List[int], target:int, left:int, right:int) -> int:
        if left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                return self.binary_serch(nums, target, mid+1, right)
            elif nums[mid] > target:
                return self.binary_serch(nums, target, left, mid-1)
            else:
                return mid
        else:
            return -1
            
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: Set = set()
        nums2.sort()
        for n1 in nums1:
            # 이진 검색으로 일치 여부 판별
            i2 = self.binary_serch(nums2, n1, 0, len(nums2)-1)
            if len(nums2) > 0 and len(nums2) > i2 and n1  == nums2[i2]:
                result.add(n1)
        return result

# bisect 모듈
import bisect
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: Set = set()
        nums2.sort()
        for n1 in nums1:
            # 이진 검색으로 일치 여부 판별
            i2 = bisect.bisect_left(nums2, n1)
            if len(nums2) > 0 and len(nums2) > i2 and n1  == nums2[i2]:
                result.add(n1)
        return result