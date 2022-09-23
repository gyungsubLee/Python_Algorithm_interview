class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        _lst = []
        for lst in points:
            _lst.append((lst, lst[0]**2 + lst[1]**2))
        
        _lst.sort(key=lambda x:x[1])
        
        result = []
        for i in range(k):
            result.append(_lst[i][0])
        
        return result
        
        
        
            