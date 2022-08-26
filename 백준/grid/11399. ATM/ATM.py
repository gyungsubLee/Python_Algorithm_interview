n = int(input())
s = list(map(int, input().split()))
num =0
s.sort()
for i in range(n):
    num += int(s[(n-i)-1] * (i + 1))
print(num)