a = 1000 - int(input())
cnt = 0

b = [500, 100, 50, 10, 5, 1]

for c in b:
    cnt  += a//c
    a %= c

print(cnt)