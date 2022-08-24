class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(index, target, path):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return
            
            for i in range(index, len(candidates)):
                dfs(i, target-candidates[i], path+[candidates[i]])
                
        res = []
        dfs(0, target, [])
        return res
        
    