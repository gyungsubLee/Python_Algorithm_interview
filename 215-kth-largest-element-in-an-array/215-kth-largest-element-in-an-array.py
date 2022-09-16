class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = list()
        for n in nums:
            heapq.heappush(heap, -n)
        for _ in range(1, k): # k-1번째 까지 추출
            heapq.heappop(heap)
        return -heapq.heappop(heap)
            
        
        
        