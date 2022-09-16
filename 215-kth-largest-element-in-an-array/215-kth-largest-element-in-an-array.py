class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def insert_maxheap(n):
            maxHeap.append(n)
            i = len(maxHeap)-1
            parent = i//2
            while parent > 0:
                if maxHeap[i] > maxHeap[parent]:
                    maxHeap[parent], maxHeap[i] = maxHeap[i], maxHeap[parent]
                i = parent
                parent = i//2
         
        def extraction_maxHeap(idx):
            left = idx * 2
            right = idx * 2 + 1
            smallest = idx
            if left <= len(maxHeap) -1 and maxHeap[left] > maxHeap[smallest]:
                smallest = left
            if right <= len(maxHeap) -1 and maxHeap[right] > maxHeap[smallest]:
                smallest = right
            if smallest != idx:
                maxHeap[idx], maxHeap[smallest] = maxHeap[smallest], maxHeap[idx]
                extraction_maxHeap(smallest)
        
        def extraction():
            extracted = maxHeap[1]
            maxHeap[1] = maxHeap[len(maxHeap)-1]
            maxHeap.pop()
            extraction_maxHeap(1)
            return extracted
        
        if not nums or not k:
            return 0
        
        maxHeap = [None]
        for _ in range(len(nums)):
            insert_maxheap(nums.pop())
        result=''
        for _ in range(k):
            result = extraction()
        return result
            
        
        
        