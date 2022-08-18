class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        d = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        res=[]
        stack=[(0, "")] # index: int
        while stack:
            i, combo = stack.pop()
            if i == len(digits):
                res.append(combo)
            else:
                nextDigit =digits[i]
                children  = d[nextDigit]
                for child in children :
                    stack.append((i+1, combo+child))
        return res
        
        
            