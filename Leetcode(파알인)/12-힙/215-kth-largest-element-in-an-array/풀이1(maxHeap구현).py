class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # maxHeap에 요소 삽입 및 정렬
        def insert_maxHeap(n):
            heap.append(n)
            i = len(heap)-1
            parent = i//2
            while parent > 0:
                if heap[i] > heap[parent]:
                    heap[i], heap[parent] = heap[parent], heap[i]
                i = parent
                parent = i//2
        
        # 최댓값 추출 후 힙 재정렬
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
        
        # max_heap에서 최댓값 추출
        def extraction():
            extraced = heap[1]
            heap[1] = heap[len(heap)-1]
            heap.pop()
            rearrangement_maxHeap(1)
            return extraced
        
        # 예외처리
        if not nums or not k:
            return 0 

        # initialize
        heap = [None]
        result = ''

        # Array -> maxHeap
        for n in nums:
            insert_maxHeap(n)
        
        # 최대값(root) 추출 * k
        for _ in range(k):
            result = extraction()
        
        return result
            