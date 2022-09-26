class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst = []
        for n1 in nums1:
            for n2 in nums2:
                if n1 == n2 and n1 not in lst:
                    lst.append(n1)
        return lst