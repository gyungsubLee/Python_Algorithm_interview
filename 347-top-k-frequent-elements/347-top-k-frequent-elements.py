import collections
from heapq import heappop, heappush

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        freqs_heap = []
        
        # 최대 힙 -> tuple(우선순위[-min_heap], 값 min_heap)
        for f in freqs:  
            heapq.heappush(freqs_heap, (-freqs[f], f))
            
        topk = list()
        # k번 만큼 추출, 
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])
        
        return topk