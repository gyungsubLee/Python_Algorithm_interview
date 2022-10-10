## 풀이1(lambda)
```isdigit()``` 를 사용하여 숫자 필터링 (숫자:True, 문자:False)

```python
letters, digits = [], []
for log in logs:
    if log.split()[1].isdigit():
        digits.append(log)
    else:
        letters.append(log)
```

<br>

```lambda``` 를 사용,
1. 식별자([0])를 제외한 문자열([1:])을 key로 하여 정렬
2. 동일한 경우 식별자([0])를 key로 정렬

```python
letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
```

<br>

Array + Array = 순서대로 item을 더해서 새로운 Array 반환
>ex)<br>
> a = [1, 2, 3], b = [4, 5, 6]<br>
> a+b = [1, 2, 3, 4, 5, 6]<br>
> b+a = [4, 5, 6, 1, 2, 3]

```python
return letters + digits
```

<br/>

문제 자체가 좀 애매하다. 정렬의 순서를 알려주지 않아 헷갈렸다. 특히 숫자 문자 구별은 Input 값을 보고 [1]만 비교했지만 case가 더 많아지는 경우 나머지 for문으로 나머지 요소들도 구분하는 형식으로 수정해야 될 듯 하다. 