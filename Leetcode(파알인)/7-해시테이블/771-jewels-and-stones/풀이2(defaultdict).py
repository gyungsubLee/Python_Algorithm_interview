from collections import defaultdict
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = defaultdict(int)
        count = 0
        
        for char in stones:
            freqs[char] += 1
                
        # 보석(J)의 빈도 수 합산
        for char in jewels:
            if char in freqs:
                if char in freqs:
                    count += freqs[char]
        
        return count