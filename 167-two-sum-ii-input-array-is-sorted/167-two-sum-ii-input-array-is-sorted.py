class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
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
                
        for k, v in enumerate(numbers):
            left, right = k+1, len(numbers)-1
            expected = target - v
            v = binary_search(k+1, len(numbers)-1)
            if v > 0:
                return k+1, v+1
            
            
            
        
                
        