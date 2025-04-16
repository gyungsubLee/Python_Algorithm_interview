# 넘파이 모듈 사용 -> leetcode 실행 X
# 시간복잡도: O(logN)

class Solution:
    def fib(self, n: int) -> int:
        M = np.matrix([0,1], [1,1])
        vec = np.array([[0], [1]])
        
        return np.matmul(M**n, vec)[0]