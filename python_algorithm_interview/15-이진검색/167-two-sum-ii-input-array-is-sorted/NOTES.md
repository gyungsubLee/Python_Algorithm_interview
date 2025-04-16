​
# 풀이1(투포인터)
이전 배열 파트의 두수의 합에서 정리했던 투포인터 풀이와 동일하다. 
이전 배열 파트의 문제는 입력 받는 배열이 정렬 되어 있지 않아 index를 구하는 것이 불가능 했지만(되긴 하는데 안 하는 게 더 나음),

해당 문제는 ```정렬된 배열을 받```기 때문에 쉽게 투포인터를 통해서 ```O(n)```으로 풀이가 가능하다.<br/>
(index를 구하는 것이 아니라면 정렬 되지 않는 배열을 받아도 상관없다.)

```python
# 풀이1(투포인터)
# 시간복잡도: O(n)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) -1
        while left < right:
            if numbers[left] + numbers[right] < target:
                left +=1 
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left+1, right+1]
```


<br/>

# 풀이2(이진 검색 - 반복, 투포인터)

투포인터 와 while문 반복을 통해 구하는 풀이이다.
enumerate로 index 와 value 값을 받고, 해당 value 값의 다음 index 범위부터 이진 검색으로 탐색을 하여 expected(target-value)를 구한다. for문으로 O(n), 이진 검색으로 O(logN), 따라서 ```O(nlogN)```의 연산으로 풀이된다.


```python
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            left, right = k + 1, len(numbers) - 1
            expected = target - v
            # 이진 검색으로 나머지 값 판별
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] < expected:
                    left = mid + 1
                elif numbers[mid] > expected:
                    right = mid - 1
                else:
                    return k + 1, mid + 1        
```

<br/>

# 풀이3(이진검색 - 재귀, 투포인터)
논리 구조는 동일하다. 책에 재귀를 통한 풀이가 없길래 구해봤다.

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 이진 검색 -> 재귀
        def binary_search(left, right):
            if left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] < expected:
                    return binary_search(mid+1, right)
                elif numbers[mid] > expected:
                    return binary_search(left, mid-1)
                else:
                    return mid
            else:
                return -1
                
        for k, v in enumerate(numbers):
            left, right = k+1, len(numbers)-1
            expected = target - v
            v = binary_search(k+1, len(numbers)-1)
            if v > 0:
                return k+1, v+1
```

<br/>

# 정리
투포인터: O(n), 이진검색:O(nlogn)

biset모듈을 사용한 풀이가 책에는 정리 되어있지만, 해당 풀이는 직관적이지 않아 배제하였다.
