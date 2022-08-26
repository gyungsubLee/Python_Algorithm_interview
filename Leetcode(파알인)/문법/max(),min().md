# ✍️ max(),min() = 최댓값, 최솟값

## 1. min(), max()

```python
# min()
numbers = [5, 4, 1, 2, 3]
>>> min(numbers)
1

>>> min(5, 4, 1, 2, 3)
1
```

```python
# max()
numbers = [5, 4, 1, 2, 3]
>>> max(numbers)
5

>>> max(5, 4, 1, 2, 3)
5
```
<br/>

## 2. 문자열 리스트 min, max
문자열은 ```ASCII``` 값을 비교하여 최대, 최소를 구힌다.

```python
fruits = ['watermelon', 'kiwi', 'blueberry', 'apple']

>>> min(fruits)
apple

>>> max(fruits)
watermelon
```

<br/> 

## 3. min, max(iterable, key)
비교하는 기준(함수, lambda)을 key로 설정 가능하다.

<br/>

예1) Dictionary
```python
square = {2: 4, 3: 9, -1: 1, -2: 4}

>>> min(square)
-2

>>> min(square, key = lambda k: square[k])
-1
```

<br/>

예2) 길이(len)
```python
fruits = ['watermelon', 'kiwi', 'blueberry', 'apple']

>>> min(fruits, key = lambda s: len(s))
>>> min(fruits, key=len)
kiwi

>>> max(fruits, key = lambda s: len(s))
>>> max(fruits, key=len)
watermelon
```