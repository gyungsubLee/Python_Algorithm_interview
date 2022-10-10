class Solution:
    dp = collections.defaultdict(int)
    
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        if self.dp[n]:
            return self.dp[n]
        
        return self.fib(n-1) + self.fib(n-2) 