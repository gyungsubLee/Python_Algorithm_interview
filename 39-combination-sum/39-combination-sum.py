class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        stack = [(0, target, [])]
        while stack:
            index, target, path = stack.pop()
            if target < 0:
                continue
            if target == 0:
                res.append(path)
                continue
            for i in range(index, len(candidates)):
                stack.append((i, target-candidates[i], path+[candidates[i]]))
            
        return res
        
    