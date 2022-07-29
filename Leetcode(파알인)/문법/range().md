# ✍️ range(start, stop, step)

## 👉 range(stop) [인자: 1]
인자1개만 입력할 경우 start=0 으로 default 값으로 지정된다.

```python
>>> range(5) # start: 0, stop: 5-1
[0, 1, 2, 3, 4]
```

<br/>

## 👉 range(start, stop) [인자: 2]
```python
>>> range(1, 5) # start: 1 , stop: 5-1
[1, 2, 3, 4]
```

<br/>

## 👉 range(start, stop, step) [인자: 3]
step: 숫자의 간격 (음수 지정 가능)
```python
>>> range(0, 20, 2) # step: 2
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

>>> range(20, 0, -2) # step: -2
[20, 18, 16, 14, 12, 10, 8, 6, 4, 2]
```