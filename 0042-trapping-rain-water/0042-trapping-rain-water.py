class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        volume, left, right = 0, 0, len(height)-1
        maxLeft, maxRight = height[left], height[right] # 초기화
        
        while left < right:
            maxLeft, maxRight = max(height[left], maxLeft), max(height[right], maxRight)
            
            if maxLeft <= maxRight:
                volume += maxLeft - height[left]
                left += 1
                
            else:
                volume += maxRight - height[right]
                right -= 1
        
        return volume