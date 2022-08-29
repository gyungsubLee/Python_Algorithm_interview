연결리스트로 구성된 펠린드롬을 판별하는 문제

# ✍️ 풀이1(배열)
자료형 = 배열([])<br>
시간복잡도: O(n²) [ pop(0): O(n) * while: O(n) ]<br/>
공간복잡도: ?


우선 연결리스트로 구성된 데이터를 차례대로 배열에 넣는다.

```python
q:list = []

# 예외처리
if not head:
    return False

while head:
    q.append(head.val)
    head = head.next
```

<br/>

```pop()``` 를 통해 처음과 끝 값(value)를 비교하여 판별한다.

```python
while len(q) > 1:
            if q.pop(0) != q.pop():
                return False
        return True
```

```pop(0)``` 는 ```O(n)의 시간복잡도```를 갖는다. 따라서 전체 로직은 ```O(n²)```의 시간복잡도를 갖는다. 


자료형을 ```deque```로 변경하거나 ```투포인트```를 사용하여 ```O(n)``` 
으로 시간복잡도를 낮출 수 있다.


<br/><br/>

# ✍️ 풀이2(Deque)
자료형 = deque<br/>
시간복잡도: O(n) [ while: O(n) ]<br/>
공간복잡도: O(n²) ?

```python
from collections import deque

q:Deque = deque()
```

<br/>

pop(0): [O(n)] -> ```popleft()``` : [```O(1)```]
```python
while len(q) > 1:
    if q.popleft() != q.pop():
        return False
return True
```

[🤔 eque란?](https://velog.io/@dltjq2323/Deque%EB%8D%B0%ED%81%90)


<br/><br/>

# ✍️ 풀이3(투포인터)
투포인터: l, r = 0, len(q)-1 <br/>
시간복잡도: O(n) [ while: O(n) ]<br/>
공간복잡도: O(n)

```python
l, r = 0, len(nums)-1
while l <= r:
    if nums[l] != nums[r]:
        return False
    l += 1
    r -= 1
return True
```

<br/><br/>

# ✍️ 풀이4(런너-fast, slow)

이해가 안된다... 나중에 정리
