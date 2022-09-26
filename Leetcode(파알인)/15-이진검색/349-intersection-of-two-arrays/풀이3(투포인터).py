# 풀이3(투푀인터)  시간복잡도: O(nlogN)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: Set = set()
        # 정렬, 시간복잡도: O(nlogN)
        nums1.sort()
        nums2.sort()
        i = j = 0

        # 투포인터 우측으로 이동하여 일치여부 판단, 시간복잡도:O(2n)
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                result.add(nums1[i])
                i += 1
                j += 1
        return result
        