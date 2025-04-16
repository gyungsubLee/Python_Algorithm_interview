# ✍️ 풀이1-1(역순-반복, LL-L)
연결리스트 -> 역순(반복)
```python
def reverseList(self, head: ListNode)->ListNode:
    node, prev = head, None
    while node:
        next, node.next = node.next, prev
        prev, node = node, next
    return prev
```

<br/>

연결리스트 -> 리스트

```python
def toList(self, node: ListNode) -> List:
    l: List = []
    while node:
        l.append(node.val)
        node = node.next    
    return l
```

<br/>

문자열 -> 연결리스트(역순)

```python
def toReversedLinkedList(self, result: str)->ListNode:
    prev: ListNode = None
    for r in result:
        node = ListNode(r)
        node.next = prev
        prev = node
    return node
```

<br/>

list -> str -> int -> 더하기 

```python
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    a = self.toList(self.reverseList(l1))
    b = self.toList(self.reverseList(l2))

    resultStr = int(''.join(str(e) for e in a)) + \
                int(''.join(str(e) for e in b))

    return self.toReversedLinkedList(str(resultStr))
```

<br/><br/>


# ✍️ 풀이1-2(역순-재귀, LL-L)


연결리스트 -> 역순(재귀)
```python
def reverseList(self, head: ListNode)->ListNode:
    def reverse(node: ListNode, prev: ListNode=None):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)
    return reverse(head)
```

<br/><br/>

# ✍️ 풀이2(전가산기)
2개의 변수를 통해 각 연결리스트 value의 합 과 자릿수를 할당하고 계산하여 풀이 (전가산기 유사)

<br/>

### 1. Initialize

```python
node=head=ListNode(0)
```

위와 같이 dummy 데이터를 만들어 뒤에 붙인 후

```python
return node.next
```
dummy 데이터 다음(.next), 실제 데이터 부분만 추출한다.

<br/>

### 2. 각 Node의 value 더하고 node 넘기기

```python
carry=0
while l1 or l2 or carry:
    sum=0
    # 두 입력값의 합 계산
    if l1:
        sum += l1.val
        l1 = l1.next
    if l2:
        sum += l2.val
        l2 = l2.next
```

<br/>

### 3. divmod()를 통해 자릿수(몫), 값(나머지) 계산

```python
carry, val = divmod(sum + carry, 10)
```

<br/>

### 4. Node의 value 넣고 넘기기

```python
head.next = ListNode(val)
head = head.next 
```


