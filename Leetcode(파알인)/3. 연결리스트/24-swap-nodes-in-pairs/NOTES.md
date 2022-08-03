# ✍️ 풀이1(값 변경)

### 1. Initialize
```python
cur = head
```

### 2. 스왑, node 2번 건너뛰기
```python
while cur and cur.next:
    cur.val, cur.next.val = cur.next.val, cur.val
    cur = cur.next.next
```

### 3. 전체 출력
```python
return head
```
cur 변수와 헷갈렸다.

> 해당 로직에서 <br/>
>```cur```는 각 node에 접근하기 위해 initailize한 변수이고 <br/>
>```head``` 는 연결리스트 전체를 참조한 변수이다. 

-> 🤔 cur에 head를 참조하는 부분이 아직 정확하게 정리가 안되었음... 나중에 다시 정리
(역순연결리스에서 prev, curr 나 풀이2에서 dummy_node나 위에서의 cur=head나 뭔 차이가 있는지 정확하게 이해가 안됨.)




<br/>
<br/>



# ✍️ 풀이2(반복)

```python
```

​



```python
```



<br/>
<br/>


# ✍️ 풀이3()​
​


```python
```

```python
```
