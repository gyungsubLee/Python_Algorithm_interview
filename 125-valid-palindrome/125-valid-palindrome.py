class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower(); # lower(): 복사해 소문자로 변환하여 반환
        ispal = re.sub('[^a-z0-9]', '', s)
        return ispal == ispal[::-1]