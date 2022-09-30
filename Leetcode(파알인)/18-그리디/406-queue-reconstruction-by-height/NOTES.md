```
Empty list:                []
[7,0] -> Add 7 at index 0: [[7,0]]
[7,1] -> Add 7 at index 1: [[7,0], [7,1]]
[6,1] -> Add 6 at index 1: [[7, 0], [6, 1], [7, 1]] 
[5,0] -> Add 5 at index 0: [[5, 0], [7, 0], [6, 1], [7, 1]] 
[5,2] -> Add 5 at index 2: [[5, 0], [7, 0], [5, 2], [6, 1], [7, 1]] 
[4,4] -> Add 4 at index 4: [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
```

풀이1,2 위 논리 구조와 동일

reference) <br/>
https://leetcode.com/problems/queue-reconstruction-by-height/discuss/673919/Python-3-simple-solution-with-explanation


<br/>

# 풀이1​(heapq)

```python
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))
        
        result = []
        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])
        return result
```


<br/>


# 풀이2(lambda)


```python
class Solution:
     def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        result = []
        for h, k in sorted(people, key=lambda x: (-x[0], x[1])):
            result.insert(k, [h, k])
        return result
```