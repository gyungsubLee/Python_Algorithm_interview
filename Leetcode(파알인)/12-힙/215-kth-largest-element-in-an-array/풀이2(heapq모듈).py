# 풀이1 - heapq모듈
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = list()
        for n in nums:
            heapq.heappush(heap, -n)
        for _ in range(1, k): # k-1번째 까지 추출
            heapq.heappop(heap)
        return -heapq.heappop(heap)
            

# 풀이2 - heapify
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(len(nums)-k):
            heapq.heappop(nums)
        return heapq.heappop(nums)


# 풀이3  - nlargest(1arg, 2arg)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
        