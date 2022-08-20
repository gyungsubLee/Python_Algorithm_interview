class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(path, index, target):
            # 종료 조건
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return
            
            # DFS-재귀
            for i in range(index, len(candidates)):
                dfs(path+[candidates[i]], i, target-candidates[i])
                
        res = []
        dfs([], 0, target)
        return res
    