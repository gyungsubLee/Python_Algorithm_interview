from collections import deque
class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = re.sub('[^a-zA-Z0-9]', '', s).lower()
        return a == a[::-1]
        
            