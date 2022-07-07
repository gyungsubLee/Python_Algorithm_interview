# 풀이3) - 책풀이
n, m, k = map(int, input().split()) # n:배열크기, m: 더하는 횟수, k:최대 반복 횟수
a = list(map(int, input().split())) # a: 배열

a.sort()
first = a[n-1] # 가장 큰 수
second = a[n-2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = (m // (k + 1)) * k + m % (k + 1)
print(count)

result = count*first + (m-count)*second

print(result)
















