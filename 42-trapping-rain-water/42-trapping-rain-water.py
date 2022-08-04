class Solution:
    def trap(self, height):
        water=[]
        left=0
        for h in height:
            left = max(left, h)
            water.append(left)
        
        right=0
        for i in range(len(height)-1, 0-1, -1):
            right = max(right, height[i])
            water[i] = min(right, water[i]) - height[i]
        
        return sum(water)
            
        