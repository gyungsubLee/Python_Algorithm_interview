# 그리드 알고리즘
# 아이디어: `각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰수 찾기`

'''
입력값
3 3
3 1 2
4 1 4
2 2 2

2 4
7 3 1 8
3 3 3 4
'''

# 퓰아1) - 내 풀이
n, m = map(int, input().split())
min_list = []

for _ in range(n):
    data = list(map(int, input().split()))
    min_list.append(min(data))

result = max(min_list)

print(result)