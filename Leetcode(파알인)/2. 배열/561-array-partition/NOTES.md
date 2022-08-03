문제를 이해하는데 조금 걸렸다. (min함수를 잘 몰랐음.)
해당 문제는 주어진 list의 n개를 2개 씩 짝을 지어 각 최솟값을 다 더하여 만들수 있는 수의 최댓값을 구하는 것이다. 
ex) [a, b, c, d]: min(a, b) + min(c, d)

<br/>

# ✍️ 풀이1(배열)
주어진 list를 정렬(```.sort()```) 후 배열(```[]```)에 2개의 요소를 넣어 최솟값(```min(배열)```)을 구하고 더하여 해를 구한다.

```python
pair = []
nums.sort()

for n in nums:
    pair.append(n)
    if len(pair) == 2:
        sum += pair[0]
        pair = []
```

<br/>


# ✍️ 풀이2(짝수)

아래와 같이 정렬 후 짝수의 index 만들 더하여 해를 구한다.

```python
sum = 0
nums.sort()

for i, n in enumerate(nums):
    if i % 2 == 0:
        sum += n
return sum
```

<br/>


# ✍️ 풀이3(슬라이싱)
파이썬 다운 방식으로 슬라이싱을 통해 한 줄로 간단히 표현가능

```python
sum(sorted(nums)[::2])
```
