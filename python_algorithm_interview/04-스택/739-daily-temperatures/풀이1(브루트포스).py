# 브루트포스 -> O(n²): 시간초과
class Solution:
    def dailyTemperatures(self, temperatures):
        l=[]
        c=0
        for i,t in enumerate(temperatures):
            for u in temperatures[i+1:]:
                c += 1
                if t < u:
                    l.append(c)
                    c=0
                    break
            if len(temperatures[:i+1]) != len(l):
                l.append(0)
                c=0

        return l


b=[55,38,53,81,61,93,97,32,43,78]
a = Solution()
a.dailyTemperatures(b)  