# ✍️ for 문

## 👉 for문의 기본 구조
```python
for 변수 in 리스트(or 튜플 or 문자열):
    수행할 문장1
    수행할 문장2 
      . . .
```

<br/>

### ● 리스트 예시
```python
test_list = ['one', 'two', 'three'] 
for i in test_list: 
       print(i)
>>> 
one 
two 
three
```

<br/>

### ● 튜플 예시
```python
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)
>>>
3
7
11
```

<br/>

### ● 문자열 예시
```python
a = 'abc'
for n in a:
    print(n)
>>>
a
b
c
```

## 👉 for문 -  continue, break 문
### ● continue
while문 과 같이 continue 사용 가능

for문을 수행 도중 ```continue문``` 을 만나면 아래의 로직을 건너뛰고 다음 case로 넘어간다. 

```python
data_list = [1, 2, 3, 4, 5, 6, 7]

for data in data_list:
    if data < 4:
        continue
    print(f"3보다 큰 수 : {data}")

>>>
3보다 큰 수 : 4
3보다 큰 수 : 5
3보다 큰 수 : 6
3보다 큰 수 : 7

```


### ● break
for문 수행 도중 break문을 만나는 경우 바로 for문 빠져나온다.


```python
data_list = [1, 2, 3, 4, 5, 6]

for data in data_list:
    if data > 3:
        break
    print(f"4 보다 작은 수 : {data}")

>>>
4 보다 작은 수 : 1
4 보다 작은 수 : 2
4 보다 작은 수 : 3
```

<br/>

----
reference)<br/>
https://notstop.co.kr/1204/<br/>
https://wikidocs.net/22