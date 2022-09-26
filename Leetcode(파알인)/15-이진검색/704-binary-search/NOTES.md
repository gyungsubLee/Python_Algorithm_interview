​
# 처음 풀이)

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(nums):
            mid = len(nums) // 2
            if nums[mid] > target:
                return binary_search(nums[:mid])
            elif nums[mid] < target:
                return binary_search(nums[mid+1:])
            else:
                return mid
        return binary_search(nums)  
```

재귀를 사용하여 위와 같이 Birany search를 구현했다.

해당하는 풀이로는 답을 도출할 수 없었는데, 해당 문제는 target의 index 값을 구하는 것으로 
위와 같이 nums를  절반으로 좁혀서 넘겨주어 원본 list의 index는 당연히 구할 수 없는 것이었다. 결국 문제를 정확하게 인지하지 못해 생긴 오류였다.


<br/>

# 두번째 풀이)
따라서 index의 값을 구하기 위해 투포인터로 index를 좁혀들어가는 방식으로 아래와 같이 풀이를 하였다.

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            if left <= right:
                mid = (left+right) //2
                if nums[mid] < target:
                    return binary_search(mid+1, right)
                elif nums[mid] > target:
                    return binary_search(left, mid-1)
                else:
                    return mid
        return binary_search(0, len(nums)-1)
```

위 풀이는 test_case는 통과 하였으나, 제출 시 wrong answer가 나왔다. 
이유를 봤더니 target이 없을 때의 예외 case를 처리하지 않았다. 


따라서 아래와 같이 예외 case를 처리하여 정답을 도출할 수 있었다.

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            if left <= right:
                mid = (left+right) //2
                if nums[mid] < target:
                    return binary_search(mid+1, right)
                elif nums[mid] > target:
                    return binary_search(left, mid-1)
                else:
                    return mid
            else:
                return -1
        return binary_search(0, len(nums)-1)
```

<br/>

# 풀이2 (반복, 투포인터)

재귀 대신 while문을 통한 반복 풀이이다.

target의 index(mid)를 구했을 시 해당 값을 return 처리하여 구하며 target 값이 없을 시 while 문이 끝나고 '-1'을 return  하여 예외처리 한다.


```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid # retunr 시 함수를 종료하기 때문에 while도 바로 종료된다.
        return -1
```

해당 풀이도 재귀와 비슷하기 때문에 딱히 어렵지는 않다.

<br/>

# 풀이3 (bisect모듈)
파이썬에는 이진검색 모듈인 bisect가 존재한다. 

아래와 같이 간단하게 풀이 가능하다.

```python
def search(self, nums: List[int], target: int) -> int:
    index = bisect.bisect_left(nums, target)

    if index < len(nums) and nums[index] == target:
        return index
    else:
        retun -1
```

<br/>

# 풀이4(index)
이진 검색을 사용하지 않는 index 풀이

```python
def search(self, nums: List[int], target: int) -> int:
    try:
        return nums.index(target)
    except ValueError:
        return -1
```


<br/>

# 정리
책을 보면 코딩테스트 시 ```재귀```나 ```반복```으로 직접 이진 검색 풀이를 하는 편이 코드 리뷰 시 더 좋은 평가를 받는다고 나와 있다.

개인적으로도 ```재귀```나 ```반복``` 풀이가 더 직관적이고 쉬운 것 같으니 ```재귀```나 ```반복```으로 풀어야 겠다.

