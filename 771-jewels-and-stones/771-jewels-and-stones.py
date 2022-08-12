from collections import Counter

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
    	return sum(Counter(S)[i] for i in J)