# 브루트 포스
# 시간복잡도: O(n²)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst = []
        for n1 in nums1:
            for n2 in nums2:
                if n1 == n2 and n1 not in lst:
                    lst.append(n1)
        return lst



# array -> set
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: Set = set() # Set 자료형: 중복 자동 제거
        for n1 in nums1:
            for n2 in nums2:
                if n1 == n2 and n1 not in lst:
                    result.add(n1)
        return result
