class Solution(object):
    def letterCombinations(self, digits:str)->List[str]:
        # 예외처리
        if not digits:
            return []
        
        # stack        
        dic = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        res = []
        stack = [(0, '')] # index: int
        while stack:
            i, p = stack.pop()
            if i == len(digits):
                res.append(p)
            else:
                words = dic[digits[i]]
                for word in words:
                    stack.append((i+1, p + word))
        return res
                    
            
    