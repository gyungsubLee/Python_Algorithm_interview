class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if strs == [""]:
            return [strs]
    
        ans = {}
        
        for i in strs:
            sorted_i = "".join(sorted(i))
            if sorted_i in ans:
                ans[sorted_i].append(i)
            else:
                ans[sorted_i] = [i]
                
        res = []
        for i in ans.values():
            res.append(i)
        return res
