# 그림을 통한 이해​ 

이해하기까지 좀 오래 걸렸다...<br/>
 yotube에서 설명한 내용을 통해 이해한 부분을 그림으로 만들었다.

## 👉 TeseCase1
<img src="이미지/1.png" width=60% />

<img src="이미지/2.png" width=60% />

<img src="이미지/3.png" width=60% />

<img src="이미지/4.png" width=60% />

<br/>

## 👉 TestCase2

<img src="이미지/5.png" width=60% />

<img src="이미지/6.png" width=60% />

<img src="이미지/7.png" width=60% />

<img src="이미지/8.png" width=60% />


----

Reference)<br/>
https://www.youtube.com/watch?v=EgI5nU9etnU

<br/>


# ✍️ 처음 작성한 풀이)

위의 이해를 바탕으로 직접 작성한 코드이다.

```python 
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visit = []
        
        for a, b in prerequisites:
            graph[a].append(b)
        
        def dfs(crs, pre):
            visit.append(crs)
            if len(pre) == 0:
                return 
            
            for n in pre:
                if n in visit:
                    return False
                dfs(n, graph[n])
                
            return True
        
        if not dfs(0, graph[0]): false
        
        return True
```

visit list를 만들어 방문한 노드를 기록하고 재귀로 노드를 탐색하여 방문한 노드 여부를 판단하여 순환구조를 확인하는 형태로 작성했다.  

해당 풀이로는 정답을 도출할 수 없었다...

<br/>

> 🤔 생각하지 못했던 부분은?

우선 순환이 아닌데 잘못 판단 될 수 있는 경우를 생각하지 못했다.

```testcase = [0, 1], [0, 2], [1, 2]``` 의 경우 형제 노드가 방문한 노드까지 visit에 기록되어 순환이 아닌데도 순환으로 오판되었다.

해당 노드의 탐색이 모든 완료된 경우 방문한 내역을 삭제 해야 되었다.  


<br/>

또한 ```visit=[]``` 으로 작성하여 중복 되는 값을 같는 경우 Error가 발생되었다.

-> ```set()```로 중복을 걸러주거나 ```[0 for _ in range(numCourses)]```로 방문 여부를 직접 지정하는 경우로 해결 되었다.



<br/>


# ✍️ 풀이1(DFS-재귀)

```python
if not dfs(crs): return False
```
위 코드에서 약간 멘붕이 왔다.

파이썬의 함수는 1급 객체 이다.
> ### ● 1급 객체의 특징
>1.  값으로써 변수에 할당 가능
>2. 함수의 인자 나 return 값으로 가능
>3. 제어문[조건문(if..), 반복문(while..)]에서 사용 가능 (고차함수)

따라서 위의 코드처럼 함수를 값으로써 비교할 수 있다.

재귀구조로 복잡한 함수도 결국 value를 return 하기 때문에 문제가 없다.

별거 아닌건데 머리가 이해하기를 거부했다...(왜그런지 모르겠음...)







