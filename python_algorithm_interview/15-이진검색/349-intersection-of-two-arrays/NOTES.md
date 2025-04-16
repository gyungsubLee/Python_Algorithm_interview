​
# 풀이1(브루트 포스)
가장 처음으로 푼 풀이이다.  for문을 2번 돌아 O(n²)의 연산으로 모든 경우를 확인하여 정답을 도출한다.

```python
# 브루트 포스
# 시간복잡도: O(n²)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst = []
        for n1 in nums1:
            for n2 in nums2:
                if n1 == n2 and n1 not in lst:
                    lst.append(n1)
        return lst
```

책에는 set 집합형으로 풀이하여 해당 풀이도 정리했다.

<br/>

# 풀이2(이진 검색)

이진 검색을 활용하여 시간복잡도를 ```O(nlogN)```으로 줄인 풀이다.

책에는 bisect모듈을 사용한 풀이만 정리 되어있어 이진 검색 문제에서의 구현을 참조하여 아래와 같이 ```재귀```로 ```Binary Search```로 구현하여 푼 풀이도 정리 했다. 


```python
# Binary Search: 재귀 구현
# 시간복잡도: O(nlogN)
class Solution:
    def binary_serch(self, nums: List[int], target:int, left:int, right:int) -> int:
        if left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                return self.binary_serch(nums, target, mid+1, right)
            elif nums[mid] > target:
                return self.binary_serch(nums, target, left, mid-1)
            else:
                return mid
        else:
            return -1
            
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: Set = set()
        nums2.sort()
        for n1 in nums1:
            # 이진 검색으로 일치 여부 판별
            i2 = self.binary_serch(nums2, n1, 0, len(nums2)-1)
            if len(nums2) > 0 and len(nums2) > i2 and n1  == nums2[i2]:
                result.add(n1)
        return result
```

<br/>

# 풀이3(투포인터)
인자로 받는 두 개의 Array를 정렬 후 투포인터로 차례로 비교하여 답을 도출하는 풀이다.

O(nlogN)으로 정렬 연산, O(n)으로 투포인터 비교 연산을 하여 ```O(nlogN)```으로 해결이 가능하다. 

```python
# 풀이3(투푀인터)  시간복잡도: O(nlogN)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: Set = set()
        # 정렬, 시간복잡도: O(nlogN)
        nums1.sort()
        nums2.sort()
        i = j = 0

        # 투포인터 우측으로 이동하여 일치여부 판단, 시간복잡도:O(2n)
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                result.add(nums1[i])
                i += 1
                j += 1
        return result 
```

<br/>


# 정리
브루트 포스: O(n²)
이진검색, 투포인터: O(nlogN)