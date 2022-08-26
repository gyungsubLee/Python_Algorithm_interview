n, m = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)

cnt = 0
for i in range(n):    
    cnt += m // coins[i]
    m %= coins[i]

print(cnt)