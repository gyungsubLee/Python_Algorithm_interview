
# ✍️ 풀이1​(재귀, 메모제이션)


![제목 없음](https://user-images.githubusercontent.com/95308384/193751769-1b26ee83-0d25-43ba-b02f-d3f6ccb60426.png)

<br/>


### 분할: 부호를 기준으로 left, right를 나눠 재귀 호출

```python
for i, c in enumerate(input):
    if c in "+-*":
        l = self.diffWaysToCompute(input[:i])
        r = self.diffWaysToCompute(input[i+1:])
 ```

### 정복

```python
 ret.extend(eval(str(x)+c+str(y)) for x in l for y in r)
 ```

 > eval(): 인자로  문자열 식을 받아 결과값을  return 함.  ex) eval("1+2") -> 3


### 조합

 ```python
ret.extend( ... )
m[input] = ret
 ```


<br/>

### 메모제이션

```{}```를 통한 메모제이션 -> 메모리 낭비 ↓

<br/>

```python
class Solution(object):
    def diffWaysToCompute(self, input):
        m = {}
        return self.dfs(input, m)
        
    def dfs(self, input, m):
        # 재귀 종료조건
        if input in m:
            return m[input]
        if input.isdigit():
            m[input] = int(input)
            return [int(input)]

        ret = []
        for i, c in enumerate(input):
            if c in "+-*":
                # 분할
                l = self.diffWaysToCompute(input[:i])
                r = self.diffWaysToCompute(input[i+1:])
                 # 정복
                ret.extend(eval(str(x)+c+str(y)) for x in l for y in r)
        # 조합
        m[input] = ret
        return ret
```

<br/>

# 풀이2(재귀)
책 풀이 위와 동일


```python
def diffWaysToCompute(self, input: str) -> List[int]:
    def compute(left, right, op):
        results = []
        for l in left:
            for r in right:
                results.append(eval(str(l) + op + str(r)))
        return results

    if input.isdigit():
        return [int(input)]

    results = []
    for index, value in enumerate(input):
        if value in "-+*":
            left = self.diffWaysToCompute(input[:index])
            right = self.diffWaysToCompute(input[index + 1:])

            results.extend(compute(left, right, value))
    return results
```


<br/>

----

Reference)<br/>
https://leetcode.com/problems/different-ways-to-add-parentheses/discuss/66419/Python-easy-to-understand-concise-solution-with-memorization<br/>
https://www.youtube.com/watch?v=binXv9-uT3A<br/>