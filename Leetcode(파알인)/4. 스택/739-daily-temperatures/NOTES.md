# ✍️ 풀이1(브루트포스)
하나의 요소에 나머지 요소를 다 비교하여 counter를 세서 배열에 넣는 방법으로 설계를 했다.

O(n​²)의 시간복잡도를 가지며 시간초과로 실패하였다.

<br/>

# ✍️ 풀이2(Stack)
Array(```[]```)를 만들어 ```pop()```을 통해 stack의 방식으로 해결하는 풀이이다.

input의 길이만큼 0을 원소로 갖는 배열(answer) 과 stack 처리를 할 배열(stack)을 initialize한다.

```python
answer = [0]*len(T)
stack = []
```

<br/>

아래와 같이 for문을 통해 각 요소의 index를 stack에 저장하고 stack에 저장된 값과 현재 값을 비교하여 현재 값이 더 큰 경우 index의 차 만큼 answer에 업데이트 한다. 

```while문```을 통해 ```stack and cur > T[stack[-1]]```이 만족하는 경우 계속해서 update하도록 한다.

```python
for i, cur in enumerate(T):      
    while stack and cur > T[stack[-1]]:
        last = stack.pop()
        answer[last] = i - last
    stack.append(i)

return answer
```





