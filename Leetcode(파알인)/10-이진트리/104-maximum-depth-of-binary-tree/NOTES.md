​
# ✍️ 풀이1(BFS)
> BFS: 큐 구현

deque를 통한 q 구현
```python
q = collections.deque([root])
```

BFS, 각 계층마다 탐색, Node 존재 시 depth+=1, 다음 노드 q에 추가
```python
while q:
        depth += 1
        for _ in range(len(q)):
            cur_node = q.popleft()
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)
```

<br/>

## TastCase1

```
-input
    root = {val=3, 
                left={
                    val=9, left=None, right=None
                },
                right={
                    val=20,
                    left={
                        val=15, left=None, right=None
                    },
                    right={
                        val=7, left=None, right=None
                    }
                }
            }
```

### 1️⃣ while 1:
```
-output
depth = 1
q =  [
        {
            val=9, left=None, right=None
        },
        {
            val=20,
            left={
                val=15, left=None, right=None
            },
            right={
                val=7, left=None, right=None
            }
        }
    ]
```

### 2️⃣ while 2:

```
-output
depth = 2
q =  [  
        {
            val=15, left=None, right=None
        },
        {
            val=7, left=None, right=None
        }
    ]
```

### 2️⃣ while 3:
```
-output
depth = 3
```