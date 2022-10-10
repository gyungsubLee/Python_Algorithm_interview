​

# ✍️ 풀이1(DFS-재귀)

## 처음 풀이 -> 중복 되는 요소까지 구함.
```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(path, target):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return
            
            else:
                for c in candidates:
                    dfs(path+[c], target-c)
                
        res = []
        dfs([], target)
        return res
```

<br/>

> ### 👉 tast)
>input: candidates=[2,3,6,7], target=7<br/>
> -> output: [[2,2,3],[2,3,2],[3,2,2],[7]]

<br/>

종료 조건과 반복 되는 부분은 생각을 했으나 중복 요소가 나오는 부분을 생각 하지 못했다. 

<br/>

## ✍️ 해결

특정 값(target)을 구하는 경우 정렬 후 탐색을 하는 것이 효율적이다.
>해당 문제는 input 리스트가 이미 정렬이 되어있으므로 정렬을 따로 할 필요가 없음

아래 그림과 같이 작은 값 부터 순차적으로 탐색을 하여 중복된 요소가 나오는 불필요한 경우를 제거한다.

<img src="./이미지/설명1.png" width=60% />

<br/>

코드로는 아래와 같이 index 인자를 추가하여 재귀 처리하여 해결한다.

```python
def dfs(path, index, target):
    # 종료 조건
    if target < 0:
        return
    if target == 0:
        res.append(path)
        return
    
    # DFS-재귀
    for i in range(index, len(candidates)):
        dfs(path+[candidates[i]], i, target-candidates[i])
        
res = []
dfs([], 0, target)
return res
```

    