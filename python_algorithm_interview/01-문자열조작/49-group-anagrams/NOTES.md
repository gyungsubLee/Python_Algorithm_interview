## 풀이1(정렬)

> ### 🤔 애너그램<br>
> 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것<br>
> 즉, 문장 구성 요소가 동일

### 애너그램을 판단하는 가장 간단한 방법은 ```정렬하여 비교```하는 것이다. 

<br>

존재하지 않는 key를 삽입하는 경우 KeyError가 발생<br>
따라서 default 값을 생성 해주는 ```defaultdict()```로 선언<br>
 -> 키 존재 여부 체크 X, 비교 구문 생략 

```python
anagrams = collections.defaultdict(list)
```

<br/>

정렬한 값을 key로 딕셔너리에 추가

```python
for word in strs:
    anagrams[''.join(sorted(word))].append(word)
    # ''.join(sorted(word)  
    # ex) 'ate' -> 'aet', 'tea' -> 'aet' ...
```

<br/>

```values()``` 를 통해 value 값만 추출<br>
```list()``` 를 통해 입력값을 list로 생성
```python
return list(anagrams.values())
```