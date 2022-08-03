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
아직 이해 X