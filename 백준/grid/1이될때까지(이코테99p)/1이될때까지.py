#풀이1)
n, m = map(int, input().split()) # n=25, m=5

print(n, m)

cnt = 0

while n > 1:
    if n % m == 0:
        n/=m
        print(n)
        cnt += 1
    # 처음에 break문으로 작성을 함. if문에 break를 하면
    # while문 자체가 종료되고 print로 바로 넘어감. 
    # -> else를 통하여 해결
    else:        
        n -= 1
        cnt += 1

print(cnt)

# 풀이2) - 책 풀이
n, k = map(int, input().split())
result = 0

# N이 K 이상이라면 K로 계속 나누기
while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k 
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)
    
#풀이3) - 책 풀이
# -1의 연산자체가 한번에 해결되어 case가 커질수록 효율적이다.
# 문제를 요지를 정확하게 파악하고 자잘한 연산을 한번에 처리하려는 생각을 하자 (집합의 여집합으로 문제를 해결하는 부분과 비슷한 듯?)
n, k = map(int, input().split())
result = 0

while True:
    # (N == K로 나누어떨어지는 수)가 될떄까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    # //의 몫만 취한 값에 k를 다시 곱하여 n에서 뺀 값은 -1의 연산의 연속처리 결과와 같다.
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k
#마지막으로 남은 수에 대하여 1씩 빼기
# 결국 1이 되기까지의 연산 획수를 구하는 것이므로 나누기의 연산이 끝난 뒤는 -1 연산만이 남아있다. 
#  따라서 남은 값(n)의 -1을 뺀 값이 -1 연산 처리 횟수가 되므로 그 값을 result에 더하면 -1의 연산이 한번에 해결된다. 
result += (n-1)
print(result)
