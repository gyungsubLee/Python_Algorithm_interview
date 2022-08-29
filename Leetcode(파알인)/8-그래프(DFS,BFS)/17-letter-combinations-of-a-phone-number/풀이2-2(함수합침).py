class Solution(object):
    def letterCombinations(self, digits:str)->List[str]:
        # 예외처리
        if not digits:
            return []
        
        # dfs - 재귀
        def dfs(index:int, path:str):
            if len(path) == len(digits):
                res.append(path)
                return
            words = dic[digits[index]]
            for word in words:
                dfs(index+1, path+word)
                
        dic = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        res = []
        dfs(0, '')
        return res
    