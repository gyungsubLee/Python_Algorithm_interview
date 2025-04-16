# ✍️ 풀이1(투포인트)

투포인트... 처음 접했을 때 멘붕이었다. 
뭔소리진도 모르겠고 이해도 안되고... 결국 디버깅을 3번하다가 책의 풀이를 이해를 했다.

## 🤔이해가 안 되었던 부분)
- 슬라이싱
- max() <- (특히 이놈, 이해하니 별게 아니었다...)<br/>
-> 따로 문법 폴더에 정리함.

우선 문제는 주어진 문자열에서 가장 긴 팰린드롬을 추출하는 것이다.
> 팰린드롬: 뒤집어도 같은 문자열

팰린드롬은 뒤집어도 같은 문자열이기 때문에 투포인터 방식에서는 처음 같은 문자를 찾고 양 옆으로 확장하여 확인하는 풀이다.

처음 같은 문자의 case는 2가지로 나뉜다.
>  1. 짝수의 경우  ex) 'aa'
>  2. 홀수의 경우  ex) 'aba'

따라서 짝수의 경우, 홀수의 경우 2가지를 양쪽 포인터(left, right)로 확인한다.

```투포인터``` 와 ```짝수, 홀수 확인``` 구현 코드는 아래와 같다.

```python
# 투포인터
def expand(left: int, right: int) -> str:
    # 양쪽 포인터가 주어진 문자열 범위 내에서 value 같은 경우 양쪽으로 확장
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left+1:right]

expand(i, i+1) # 짝수의 경우
expand(i, i+2) # 홀수의 경우
```

<br/>

```python
s[left+1:right]
```

그리고 위 슬라이싱 처리 부분에서도 참 애를 먹었다.

해당 코드는 확인한 투포인터(left, right)에서 결과값(팰린드롬)을 도출하는 로직으로 디버깅을 여러번 하면서 이해가 되었다.

해당 로직은 팬린드롬이 확인되지 않으면 
> 짝수의 경우: ''<br>
> 홀수의 경우: 1개의 문자

를 return 한다.

그 이유는 아래와 같다. 
>짝수의 경우: [i+1:i+1]  -> ""(공백) <br/>
>홀수의 경우: [i+1:i+2]  -> 1개 문자

<br/>
그리고 팬린드롬이 확인되어 확장하는 경우 

```python
s[left] != s[right]
``` 

인 양쪽으로 **한칸 더 확장**되는 경우에서 포인터 전진이 끝나기 때문에 
```left+1```을 하여 값을 return 처리한다.

<br/>

```python
result = max(result, expand(i, i+1), expand(i, i+2), key=len)
```

마지막으로 위 ```max()``` 로직을 이해하는데 참 힘들었다.(결론적으론 너무 간단한 부분이었음)

```max()```는 주어진 인자에서 최댓값을 return하는 함수로 key를 통해 옵션을 줄 수 있다.

그리고 파이썬도 함수를 1급 객체로써 값으로 써 함수의 인자값이 될 수 있다는 사실을 알았다.

따라서 위 로직은 result, expand(i, i+1), expand(i, i+2)이 셋의 value 중 길이가 가장 긴(key=len) 최댓값을 result에 할당하는 로직이다. 

<br/>

### ● 전체코드
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 팰린드롬 판별, 투포인트 확장
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        # 해당 사항 없을 시 리턴
        if len(s) < 2 or s == s[::-1]:
            return s
        
        result = ''
        # 슬라이딩 윈도우 우측으로 이동
        for i in range(len(s)-1):
            result = max(result, expand(i, i+1), expand(i, i+2), key=len)

        return result
```

<br/>
<br/>



>진짜 감개무량한 것 같다. 처음 알고리즘을 접하고 이 문제를 봤을 때 진짜 멘붕이었는데 이해를 하니 참 재밌는 것 같다.

<br/>


## 🤔 추가정리)
해당 문제는 다이나믹 프로그래밍으로 풀 수 있는 전형적인 문제라고 한다. 근데 아직 다이나믹 프로그래밍을 학습하지 않았다. 따라서 다이나믹 프로그래밍 학습 후 해당 방법으로 풀어보고 정리하자.