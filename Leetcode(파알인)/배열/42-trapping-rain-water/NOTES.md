
# ✍️ 풀이1(투포인터)
투포인터(left, right)로 max()를 통해 최댓값을 갱신하며 volume을 구한다.
```python
left, right = 0, len(height) - 1
left_max, right_max = height[left], height[right]

while left < right:
    left_max, right_max = max(height[left], left_max), max(height[right], right_max)
```

left_max 와 right_max 를 비교하여 포인터가 가장 큰 값(높이)에 도착했을 때 더이상 진행되지 않게 처리한다. 

```python
while left < right:
     ...
    
    if left_max <= right_max:
        volume += left_max - height[left]
        left += 1
        
    else:
        volume += right_max - height[right]
        right -= 1
```

<br/>

# ✍️ 풀이2(Stack)

아직 이해 X
