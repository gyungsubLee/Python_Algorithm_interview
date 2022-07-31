# ✍️ enumerate()

### 👉 enumerate(list)
리스트의 ```index```와 ```value```를 ```tuple``` 형태로 반환한다.
-> ```(index, value)```

보통 for문 과 함께 사용하며 list와 index를 이용하여 코드를 작성할때 쓴다. 

```python
for entry in enumerate(['A', 'B', 'C']):
        print(entry)
>>>
(0, 'A')
(1, 'B')
(2, 'C')
```

<br>

### 👉 시작 인덱스 변경


```python
>>> for i, letter in enumerate(['A', 'B', 'C'], start=1):
...     print(i, letter)
...
1 A
2 B
3 C
```

```python
>>> for i, letter in enumerate(['A', 'B', 'C'], start=101):
...     print(i, letter)
...
101 A
102 B
103 C
```
<br>

---
Reference)<br/>
https://www.daleseo.com/python-enumerate/

