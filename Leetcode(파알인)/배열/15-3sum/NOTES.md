# ✍️ 풀이1(브루트포스)

```nums.sort()```
정렬을 통해 풀이 간소화 [정렬의 시간복잡도: O(nlogn)]


```python
for i in range(len(nums)-2):
        #중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, len(nums)-1):
            #중복된 값 건너뛰기
            if j > i + 1 and nums[j] == nums[j-1]:
                continue
            for k in range(j+1, len(nums)):
                #중복된 값 건너뛰기
                if k > j + 1 and nums[k] == nums[k -1]:
                    continue

                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])
```

위 코드와 같이 브루트포스로 O(n³)의 풀이가 가능하다. 
  -> 타입아웃으로 실패 

<br/>

# ✍️ 풀이2(투포인터)
투포인터를 통해 ```O(n²)```으로 시간복잡도를 줄일 수 있다.


```python
l, r = i+1, len(nums)-1
while l < r:
    s = nums[i] + nums[l] + nums[r]
    if s < 0:
        l += 1 
    elif s > 0:
        r -= 1
    else:
        res.append([nums[i], nums[l], nums[r]])
        # 중복된 값 건너뛰기
        while l < r and nums[l] == nums[l+1]:
            l += 1
        # 중복된 값 건너뛰기
        while l < r and nums[r] == nums[r-1]:
            r -= 1
        l += 1; r -= 1
```

else문의 로직에서 또한 중복된 값을 같는 포인터를 넘어가는 형식으로 필요없는 연산을 줄인다. 
