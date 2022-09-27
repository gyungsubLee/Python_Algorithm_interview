
# 풀이1(이진검색 - 재귀, 투포인터)
for문 과 이진 탐색을 통한 O(nlogN) 연산으로 풀이하였다. 
이전 풀이에서 for문만 더 해진 경우로 쉽게 답을 풀이할 수 있었다.

```python
# 풀이1(이진검색-반복,투포인터)
# 시간복잡도: O(nlogN)
class Solution:
    # 이진 검색 - 재귀, 투포인터
    def binary_search(self, nums:List[int], target: int, left, right)->int:
        if left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                return self.binary_search(nums, target, mid+1, right)
            elif nums[mid] > target:
                return self.binary_search(nums, target, left, mid-1)
            else:
                return mid
        else: 
            return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 각 배열마다 탐색 진행
        for i in range(len(matrix)):
            nums = matrix[i]
            if self.binary_search(nums, target, 0, len(nums)-1) != -1:
                return True
        return False
```

<br/>

# 풀이2(투포인터)
책의 풀이다. 시간복잡도 ?, 투포인터인지 풀이이긴 한데... 잘 모르겠다.

풀이 자체는 직관적이라 이해하기는 쉽다. 위 풀이 보다는 더 빠른 연산으로 처리함.

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 예외처리
        if not matrix:
            return False
        
        # 첫 행의 맨 뒤
        row, col = 0, len(matrix[0])-1
        
        while row <= len(matrix)-1 and col >= 0:
            if target == matrix[row][col]:
                return True
            # 타겟이 작으면 왼쪽으로 이동
            elif target < matrix[row][col]:
                col -= 1
            # 타겟이 크면 아래로 이동
            elif target > matrix[row][col]:
                row += 1
        return False
```

<br>

# 풀이3(파이썬다운 방식)

```python
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    return any(target in row for row in matrix)
```

<br/>

# 정리
풀이1(for문 + Binary Search), 시간복잡도: O(nlogN)<br/>
풀이2(투포인터), 시간복잡도: ? <br/>
> 2의 4제곱 < 25 < 2의 5제곱
> 문제의 예시에서, 최악의 경우 18을 찾는 경우임으로, 8번의 연산으로 찾을 수 있다. 따라서 O(nlogN)보다 빠른 연산을 가짐.

풀이3(파이썬다운 방식), 시간복잡도: ?, 풀이2와 비슷한 연산 시간이라 책에 나옴. <br/>

책에서 해당 문제는 이전 검색으로 풀이가 어려워 다른 방법을 사용하여 풀이하였다고 나온다. <br/>
실제 코딩테스트에서도 이와 같이 예상과 달리 다른 방법으로 풀리는 경우가 있으므로, 
예상하는 방식대로 풀리지 않는다면 해당 방식에 너무 많은 시간을 허비하지 않도록 유의해야 한다고 한다.<br/>

근데 이진 검색을 사용하여 풀긴 함.
