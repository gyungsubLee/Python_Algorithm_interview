# ✍️ 파이썬에서 정렬(sort, sorted) 
[파알인 P.154 ~ 156]

sort: 원본값 수정
    -> 리스트명.sort()

sorted: 원본값 복사한 새로운 리스트 수정
    ->리스트명2 = sorted(리스트명)

## 👉 sorted()

```sorted()```: 입력값으로 받은 배열을 정렬하여 새로운 배열을 반환한다.

```python
>>> a = [2, 5, 1, 9, 7]
>>> sorted(a)
[1, 2, 5, 7, 9]
```

<br>

## 👉 문자열 정렬

```문자열(단어)```를 입력값으로 받을 시 아래와 같이 ```각 단어를 요소```로 만드는 새로운 배열을 반환한다.

```python
>>> b = 'zbdaf'
>>> sorted(b)
#단어 정렬 시 각 문자를 요소로 만드는 배열 반환
['a', 'b', 'd', 'f', 'z']  
```
<br>

## 👉 join() + sorted()

반환되는 배열을 ```join()``` 의 인자 값으로 넣어 문자열 반환

```python
>>> b = 'zbdaf'
>>> "".join(sorted(b))
# ''.join(리스트): 리스트에 있는 각 요소 합쳐서 하나의 문자열 반환
'abdfz'
```

<br/>

## 👉 sort()

```sort()``` : 제자리 정렬(in-place-sort), 입력을 출력으로 덮어씀 따라서 별도의 공간 필요 X

```python
>>> a = [2, 5, 1, 9, 7]
>>> a.sort()
print(a) // [1, 2, 5, 7, 9]
```
<br/>

## 👉 key = [함수, lambda]: 옵션
```key=옵션```, 옵션 정렬 가능

```python
>>> c = ['ccc', 'bb', 'a']
>>> sorted(c, key=len)
['a', 'bb', 'ccc']
```
위와 같이 옵션[ 길이(len) ...]을 추가해 정렬 가능하다. 

<br>


### ● 함수 

```key=함수``` 가능 (함수를 통해 옵션 여러개 지정 가능)

```python
a = ['cde', 'cfc', 'abc']

def fn(S):
    return s[0], s[-1]

print(sorted(a, key=fn)) // ['abc', 'cfc', 'cde']
```

### ● lambda

```lambda```를 사용한 축약

```python
>>> a = ['cde', 'cfc', 'abc']
>>> sorted(a, key=lambda s: (s[0], s[-1]))
['abc', 'cfc', 'cde']
```
