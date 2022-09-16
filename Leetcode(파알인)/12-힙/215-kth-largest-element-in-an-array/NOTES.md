
# 풀이1(maxHeap 구현)

> Time: 5861 ms (5.01%), Space: 30.1 MB (28.16%)
> -> 파이썬에서 직접 구현하는 건 굉장히 비효율적

힙 연산 정리의 이해를 바탕으로 직접 Max_Heap을 구현하여 풀었다.

굉장히 낮은 효율을 나왔지만 직접 구현했다는 것에 큰 의의를 둠.



<br/>

# 풀이2-1(heapq모듈)

heapq모듈은 최소 힙만 구현되어 있기 때문에 배열의 모든 요소들을 음수(```-```) 처리를 하여 최소 힙에 추가를 한다.

그리고 최소값을 k 번째까지 추출 후 양수 처리하여 결과값을 return 하면 쉽게 풀수 있다.

```python
heap = list()

for n in nums:
    heapq.heappush(heap, -n)

for _ in range(1, k): # k-1번째 까지 추출
    heap.heappop(heap)

return -heapq.heappop()
```

# 풀이2-2(heapify)
heapq모듈의 heapify()를 하여 바로 최소힙으로 변환 가능하다.

그리고 거꾸로(len(nums)-k) 최소값부터 추출하여 k번째를 return하게 처리한다.


# 풀이2-3(nlargest)
heap모듈은 nlargest()를 통해 특정 수 번째까지의 크기 순으로 나열한 list를 추출 가능하다.

nlargest()는 첫번째인자로 추출을 진행할 특정한 수를 받고, 두번째 인자로 추출을 진행할 list를 받는다. 

```heapq.nlargest(k, nums)[-1]``` -> k번째로 큰 수


# 풀이3 (정렬)
정렬을 시켜 index로 바로 조회하여 찾아낸다.

```sorted(nums, reverse=True)[k-1]```





