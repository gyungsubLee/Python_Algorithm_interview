​## ✍️ 풀이1(리스트 컴프리헨션, max)

리스트 컴프리헨션 + 정규식
> ### ● 리스트 컴프리헨션
> 람다와 같이 축약 표현 

> ### ● 정규식
> ```\w``` : 문자(Word Character)<br/>
>```^``` : not  

```python
words = [word for word in re.sub('[^\w]', " ", paragraph).lower().split() if word not in banned]
```
<br/>

defaultdict(int) -> int 기본값 자동 부여, 키의 존재 유무를 확인할 필요없음.
```python
counts = collections.defaultdict(int)
```

<br/>

파이썬의 기본 타입은 argmax를 지원하지 않음. 따라서 max()에 key를 지정해 argmax 간접적으로 추출 
> ● argmax<br>
f(x)를 최댓값으로 만들기 위한 x 값 <br>
따라서 최대 value 값을 갖는 key 값
```python
for word in words:
    counts[word] += 1

return max(counts, key=counts.get)
```

## ✍️ 풀이2(Counter)

Counter 모듈을 사용하여 축약
```python
counts = collections.Counter(words)

return counts.most_common(1)[0][0]
```

counts.most_common(1)[0][0] 뭔 소린지 모르겠음... 추가 정리 필요