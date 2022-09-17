class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # initialize
        
        
        def insert_maxHeap(n):
            heap.append(n)
            i = len(heap)-1
            parent = i//2
            while parent > 0:
                if heap[i] > heap[parent]:
                    heap[i], heap[parent] = heap[parent], heap[i]
                i = parent
                parent = i//2
        
        def rearrangement_maxHeap(idx):
            left = idx*2
            right = idx*2 + 1
            largest = idx
            
            if left <= len(heap)-1 and heap[largest] < heap[left]:
                largest = left
            if right <= len(heap)-1 and heap[largest] < heap[right]:
                largest = right
            if largest != idx:
                heap[idx], heap[largest] = heap[largest], heap[idx]
                rearrangement_maxHeap(largest)
            
        def extraction():
            extraced = heap[1]
            heap[1] = heap[len(heap)-1]
            heap.pop()
            rearrangement_maxHeap(1)
            return extraced
        
        
        if not nums or not k:
            return 0 
        
        heap = [None]
        # Array -> maxHeap
        for n in nums:
            insert_maxHeap(n)
        
        result = ''
        for _ in range(k):
            result = extraction()
        
        return result
            