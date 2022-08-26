class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs=[]
        for char in s:
            if char.isalnum(): # isalnum(): 영문자, 숫자 여부 판단(영:True, 숫자:False)
                strs.append(char.lower()) # lower(): 소문자 변환

        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False


        return True
