# 시간복잡도: O(n)

class Solution:
    def fib(self, n: int) -> int:
        x, y = 0, 1
        for i in range(0, n):
            x, y = y, x+y
        
        return x