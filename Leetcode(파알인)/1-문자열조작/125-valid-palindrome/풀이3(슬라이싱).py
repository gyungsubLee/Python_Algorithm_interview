import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # 정규식 -> 문자 필터링
        s = re.sub('[^a-z0-9]', '', s)
        
        return print(s, s[::-1])

a = Solution()
a.isPalindrome('abc')