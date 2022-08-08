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


### 1. dummy 노드(root)로 연결리스트(head) initialize 


<img src="../../../이미지/페어의 노드 스왑/1.png" width=60% />

<br/>

```python
root = prev = ListNode(0)
prev.next = head
```

<br/>

### 2. 페어 노드 스왑 (while문: 1회)

<img src="../../../이미지/페어의 노드 스왑/2.png" width=60% />

<br/>

```python
 while head and head.next:
    # b가 a(head)를 가리키도록 할당
    b = head.next
    head.next = b.next
    b.next = head

        # prev가 b를 가리키도록 할당
    prev.next = b
```

<br/>

### 3. 다음 페어 노드 스왑을 위한 노드 이동

이 부분을 잘 이해가 안 되었다. <br/>
노드가 스왑하여 head의 위치가 변경되는 것을 생각하지 못했다.<br/>
(별 것도 아니었는데... 3시간 동안 해맸음...)

<img src="../../../이미지/페어의 노드 스왑/3.png" width=60% />

<br/>


```python
head = head.next
prev = prev.next.next
```

<br/>

### 4. 다시 페어 노드 스왑 (while문: 2회)

<img src="../../../이미지/페어의 노드 스왑/4.png" width=60% />

<br/>

```python
 while head and head.next:
    # b가 a(head)를 가리키도록 할당
    b = head.next
    head.next = b.next
    b.next = head

        # prev가 b를 가리키도록 할당
    prev.next = b
```

### 5. 출력

```python
return root.next
```

<br/>
<br/>


# ✍️ 풀이3()​
​


```python
```

```python
```
