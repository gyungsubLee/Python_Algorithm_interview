from collections import deque
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        ispal = re.sub('[^a-z0-9]', '', s)
        return ispal == ispal[::-1]
            