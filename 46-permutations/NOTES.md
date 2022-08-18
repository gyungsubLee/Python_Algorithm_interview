# ✍️ 풀이1(DFS-재귀)


```python
def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
```

## TestCase1) nums = [1, 2, 3]

### ● 1) i=0<br/>
>dfs([2,3], [1], res)<br/>
>
>○ 1-1)i=0<br/>
dfs([3], [1, 2], res)<br/>
dfs([], [1,2,3], res)<br/>
-> res.append([1,2,3])
>
>○ 1-2)i=1<br/>
dfs([1], [1, 3], res)<br/>
dfs([], [1,3,2], res)<br/>
-> res.append([1,3,2])
>

<br/>

### ● 2) i=1<br/>
>dfs([1,3], [2], res)<br/>
>
>○ 2-1)i=0<br/>
dfs([3], [2,1], res)<br/>
dfs([], [2,1,3], res)<br/>
-> res.append([2,1,3])
>
>○ 2-1)i=1<br/>
dfs([1], [2,3], res)<br/>
dfs([], [2,3,1], res)<br/>
-> res.append([2,3,1])

<br/>

### ● 3) i=2<br/>
>dfs([1,2], [3], res)<br/>
>
>○ 3-1)i=0<br/>
dfs([2], [3,1], res)<br/>
dfs([], [3,1,2], res)<br/>
-> res.append([3,1,2])
>
>○ 3-1)i=2<br/>
dfs([1], [3,2], res)<br/>
dfs([], [3,2,1], res)<br/>
-> res.append([3,2,1])

<br/>

### ● 결과)
>res = ([1,2,3,], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]) 