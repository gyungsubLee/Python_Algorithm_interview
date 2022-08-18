# ✍️ Counter (collections)
## 👉 counter 함수를 사용해 리스트의 개수세기

### collections.Counter(a) : a에서 요소들의 개수를 세어, 딕셔너리 형태로 반환 ->  ```{문자 : 개수}```


```python
import collections

b = [1,3,4,2,3,5,2,3,4,1,3,1]
print(collections.Counter(a))

>>>
Counter({3: 4, 1: 3, 2: 2, 4: 2, 5: 1})
```

<br/>
 
## 👉 counter  - 연산
counter 함수로 구한 딕셔너리의 값(value)끼리 ```+```, ```-```, ```&(and)```, ```|(or)``` 연산 가능

```python
import collections

b = [1,1,1,1,1,1]
a = [1,1,2,2,2,2]

print(collections.Counter(a) - collections.Counter(b))
>>>
Counter({2: 4})

print(collections.Counter(a) + collections.Counter(b))
>>>
Counter({1: 8, 2: 4})
```

<br/>

## 👉 most_common() 함수 - 최빈값 구하기
### collections.Counter(a).most_common(n)
-> a의 요소를 세어, 최빈값 n개를 ```[() ...]```형태로 반환 (리스트에 담긴 튜플 형태)

```python
import collections

a  = [1,1,1,2,3,2,3,245,9]

print(collections.Counter(a).most_common(3))
>>>
[(1, 3), (2, 2), (3, 2)]

print(collections.Counter(a).most_common(1)[0][0])
>>> 
1
```

<br/>

---

Reference)<br/>
https://infinitt.tistory.com/183

