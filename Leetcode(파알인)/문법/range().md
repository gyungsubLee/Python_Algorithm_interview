# ✍️ range(start, stop, step)
> 반복이 가능한 숫자형 이터러블 객체를 반환해주는 함수이다.

## 👉 range(stop) [인자: 1]
인자1개만 입력할 경우: start=0(기본값), stop=5-1 **[0~4]**
-> 0 <= x < stop

```python
>>> range(5) # start: 0, stop: 5-1
[0, 1, 2, 3, 4]
```

<br/>

## 👉 range(start, stop) [인자: 2]
-> start <= x < stop

```python
>>> range(1, 5) # start: 1 , stop: 5-1  -> [1~4]
[1, 2, 3, 4]
```

<br/>

## 👉 range(start, stop, step) [인자: 3]
-> start <= x(step) < stop

step: 숫자의 간격 (음수 지정 가능)

```python
>>> range(0, 20, 2) # step: 2
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

>>> range(20, 0, -2) # step: -2
[20, 18, 16, 14, 12, 10, 8, 6, 4, 2]
```