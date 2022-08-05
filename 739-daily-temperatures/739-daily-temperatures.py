class Solution:
    def dailyTemperatures(self, T):
        # next greater number
        wait = [0]*len(T)
        stack = []
        
        for i, x in enumerate(T):      
            while stack and x > T[stack[-1]]:
                j = stack.pop()
                wait[j] = i - j
            stack.append(i)
        
        return wait

            
        