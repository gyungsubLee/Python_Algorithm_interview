class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 이진 검색 -> 재귀
        def binary_search(left, right):
            if left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] < expected:
                    return binary_search(mid+1, right)
                elif numbers[mid] > expected:
                    return binary_search(left, mid-1)
                else:
                    return mid
            else:
                return -1
                
        for i, v in enumerate(numbers):
            expected = target - v
            j = binary_search(i+1, len(numbers)-1)
            if j > 0:
                return i+1, j+1
        