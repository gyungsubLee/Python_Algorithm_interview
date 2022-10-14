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

위 코드와 같이 브루트포스로 모든 경우를 비교하여 ```O(n³)```의 풀이가 가능하다. 

하지만 결과는 ```타입 아웃```으로 정답을 도출하지 못했다.

<br/><br/>

# ✍️ 풀이2(```투포인터```)
```투포인터```를 통해 ```O(n²)```으로 시간복잡도를 줄여  아래와 같이 풀이 가능하다.


```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            # 중복된 겂 건너뛰기
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1 
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res
        
```

<br/>

해당 문제는 중복된 값 결과 값을 허용하지 않으므로

포인터 변경 시 ```이전 포인터의 value와 같은 경우```는 이미 비교가 끝낸 연산 처리이므로 아래와 같이 ```if문``` 과 ```while문```을 통해 ```건너뛰는 연산``` 처리를 해야된다.

그리하면 중복된 값 없이 정상적으로 결과를 도출 할 수 있다.


```python
# 중복된 겂 건너뛰기
if i>0 and nums[i] == nums[i-1]:
    continue
```


```python
while l < r and nums[l] == nums[l+1]:
    l += 1
# 중복된 값 건너뛰기
while l < r and nums[r] == nums[r-1]:
    r -= 1
```