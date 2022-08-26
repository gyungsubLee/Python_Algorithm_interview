# 그리드 알고리즘 
# 핵심 아이디어: `반복되는 수열을 파악해라.`

#풀이1) - 내 풀이
n, m, k = map(int, input().split()) # n:배열크기, m: 더하는 횟수, k:최대 반복 횟수
a = list(map(int, input().split())) # a: 배열

a.sort(reverse=True) # 입력받은 리스트 역정렬
first = a[0] # 가장 큰 수
second = a[1] # 두 번째로 큰 수

result= 0

# m과 k값을 비교하여 case를 나눠 작성함.
while m > 0:
    if m > k:
        result += first * k
        m -= k
        result += second
        m -= 1
    elif m == k:
        result += first * k
        m -= k
    elif m < k:
        result += first * m
        m -= m

print(result)

# 풀이2) - 책풀이
# -> case 나눔 없이 한번에 작성하여 코드가 효육적인 듯 하다
# -> but while문 안에 for문을 한번 더 쓰기 때문에 시작 복잡도는 내가 푼 풀이보다 더 많이 걸리지 않을까 싶다...

n, m, k = map(int, input().split()) # n:배열크기, m: 더하는 횟수, k:최대 반복 횟수
a = list(map(int, input().split())) # a: 배열

a.sort()
first = a[n-1] # 가장 큰 수
second = a[n-2] # 두 번째로 큰 수

result = 0

while True:
    for i in range(k): # 가장 큰 수를 K번 더하기
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)



# 풀이3) - 책풀이
# 반복되는 수열의 개수를 파악하여 first와 second의 빈도수를 구하고 각각 곱하여 result값 도출한다. 
# -> 굉장히 재밌는 풀이임.
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

