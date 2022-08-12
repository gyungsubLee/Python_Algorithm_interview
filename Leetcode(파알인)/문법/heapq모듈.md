# ✍️ Heapq 모듈

```python
     1  ---> root
   /   \
  3     5
 / \   /
4   8 7
```

Heapq 모듈은 이진 트리(binary tree) 기반의  최소 힙(min haep) 자료구조를 제공한다.


<br/>

```python
# root: heap[0]
heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2]
```

최소 힙(min heap) 내의 모든 원소(k)는 항상 자식 원소들(2k+1, 2k+2) 보다 크기가 작거나 같도록 원소가 추가되고 삭제된다.

<br/>


## 👉 모듈 import 


```python
from heapq import heappush, heappop //, ... 다른 함수들
```

<br/>

## 👉 최소 힙 생성
```heapq``` 모듈에은 파이썬의 보통 리스트를 마치 최소 힙처럼 다룰 수 있도록 도와준다.
(리스트와 별개의 자료구조가 아니다.)


따라서 빈 리스트를 생성해놓은 다음 heapq 모듈의 함수를 호출할 때 마다 이 리스트를 인자로 넘겨주어 처리한다.
```python
heap = []
```

<br/>

## 👉 힙 원소 추가(create)
heapq 모듈의 ```heappush()``` 함수를 이용하여 힙에 원소를 추가한다.

>첫번째 인자: 원소를 추가할 리스트 <br/>
두번째 인자: 추가할 원소

```python
from heapq import heappush

heappush(heap, 4)
heappush(heap, 1)
heappush(heap, 7)
heappush(heap, 3)

print(heap)
>>> [1, 3, 7, 4]
```

<br/>

## 👉 힙 원소 삭제(Delete)

heapq 모듈의 ```heappop()``` 함수를 이용하여 힙에서 원소를 삭제한다. 

원소를 삭제할 리스트를 인자로 넘기면, 가장 작은 원소를 삭제 후에 그 값을 리턴한다.

```python
from heapq import heappop

print(heappop(heap))
>>> 1
print(heap)
>>> [3, 4, 7]

print(heappop(heap))
>>> 3
print(heap)
>>> [4, 7]
```

<br/>

## 👉 최소값 삭제하지 않고 얻기(Read)
힙에서 최소값을 삭제하지 않고 단순히 읽기만 하려면  첫번째 원소의 index(```[0]```)로 접근한다.  
(리스트로 구현되기 때문에 index로 접근할 수 있다.)

```python
print(heap[0])
>>> 4
```

>### 😣 주의사항
>인덱스 0에 가장 작은 원소가 있다고 해서, 인덱스 1에 두번째 작은 원소, 인덱스 2에 세번째 작은 원소가 있다는 보장은 없다.
>
>왜냐하면 힙은 heappop() 함수를 호출하여 원소를 삭제할 때마다 이진 트리의 재배치를 통해 매번 새로운 최소값을 인덱스 0에 위치시키기 때문이다.
>
>따라서 두번째로 작은 원소를 얻으려면 바로 ```heap[1]```으로 접근하면 안되고, 반드시 ```heappop()```을 통해 가장 작은 원소를 삭제 후에 ```heap[0]```를 통해 새로운 최소값에 접근해야 한다.


<br/>

## 👉 기존 리스트를 힙으로 변환
이미 원소가 들어있는 리스트 -> 힙(heap)

heapq 모듈의 ```heapify()``` 라는 함수 사용


```python
from heapq import heapify

heap = [4, 1, 7, 3, 8, 5]
heapify(heap)

print(heap)
>>> [1, 3, 5, 4, 8, 7]
```

```heapify()``` 에 리스트를 인자로 넘기면 내부의 원소들의 위에서 다룬 힙 구조에 맞게 재배치되며 최소값이 0번째 인덱스에 위치한다. <br/>
(O(n)의 시간 복잡도)

<br/>

> ### 😣 주의사항
> 인자로 넘긴 원본값(리스트)을 수정한다.
> 원본값을 보존해야하는 경우 반드시 복제 후 인자로 넘긴다.
>```python
>nums = [4, 1, 7, 3, 8, 5]
>
>heap = nums[:]
>heapify(heap)
>
>print(nums)
>>>>[4, 1, 7, 3, 8, 5]
>print(heap)
>>>>[1, 3, 5, 4, 8, 7]
>```


<br/>

## 👉[응용] 최대 힙
heapq 모듈은 최소 힙(min heap)만을 지원하기 때문에 최대 힙(max heap)은 ```튜플(tuple)```을 사용하여 구현한다. 
> (우선 순위, 값) 

```python
from heapq import heappush, heappop

nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
  heappush(heap, (-num, num))  # (우선 순위, 값)

while heap:
  print(heappop(heap)[1])  # index 1
```

```python
>>>
8 7 5 4 3 1
```



<br/>

## 👉[응용] n번째 최소값/최대값
최소 힙이나 최대 힙을 사용하면 ```n 번째로 작은 값```이나 ```n 번째로 큰 값``` 효과적으로 구할 수 있다. 

<br/>

## ✍️ n 번째 최솟값
### 🔵 1. for문: list -> heap
list -> heap<br/>
```heappop()``` 함수를 n 번 호출

```python
from heapq import heappush, heappop

def nth_smallest(nums, n):
    heap = []
    for num in nums:
        heappush(heap, num)

    nth_min = None
    for _ in range(n):
        nth_min = heappop(heap)

    return nth_min

print(nth_smallest([4, 1, 7, 3, 8, 5], 3))
>>> 4
```

<br/>


### 🔵 2 .```heapify()``` 함수 사용

```python
from heapq import heapify, heappop

def nth_smallest(nums, n):
    heapify(nums)

    nth_min = None
    for _ in range(n):
        nth_min = heappop(nums)

    return nth_min
```

<br/>

### 🔵 3 .```nsmallest()``` 함수 사용


```python
from heapq import nlargest

nlargest(3, [4, 1, 7, 3, 8, 5])
>>> [1, 3, 4]

nlargest(3, [4, 1, 7, 3, 8, 5])[-1]
>>> 4
```

<br/>

## ✍️ [응용] 힙 정렬

```python
from heapq import heappush, heappop

def heap_sort(nums):
  heap = []
  for num in nums:
    heappush(heap, num)

  sorted_nums = []
  while heap:
    sorted_nums.append(heappop(heap))
  return sorted_nums

print(heap_sort([4, 1, 7, 3, 8, 5]))
>>> [1, 3, 4, 5, 7, 8]
```








<br/>



---- 

Reference)<br/>
https://www.daleseo.com/python-heapq/