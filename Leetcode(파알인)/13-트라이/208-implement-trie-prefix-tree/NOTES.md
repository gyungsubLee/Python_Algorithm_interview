​
# ✍️ 풀이1(dict)

> 시간복잡도 : O(n) [insert, search] 


<img src="https://user-images.githubusercontent.com/95308384/191414064-ef111f09-70bf-45c8-9d85-9bef825933db.png" width=60% />


 트라이 자료구조는 'apple'이라는 단어를 insert 시 위와 같이 트리를 구성하며


<img src="https://user-images.githubusercontent.com/95308384/191413979-bb5bc0ff-ef79-4c59-b099-e5ff3bd7e837.png" width=60% />


'appear' , 'appeal' 2개의 
단어를 추가 삽입 시 위와 같은 다진 트리 형태의 자료구조를 가진다.

<br/>


이전 이진탐색은 배열을 통해 구현했지만 트라이는 map(dictionary)을 통해 구현한다.

<br/>

## 🤔 이해하기 어려웠던 점

이해되지 않았던 부분은 아래의 코드인데, 아무래도 포인터를 통해 구현하기 때문에 연결리스트에서의 따로 변수를 통해 다음 노드의 주소 값을 저장하는 부분과 상이하여 멘붕이 왔었다.

```python
for c in word:                        
            if c not in cur.children:         
                cur.children[c] = TrieNode() 
            cur = cur.children[c]  
```

특히, 아래의 코드가 이해가 힘들었다.
```python
cur = cur.children[c]
```

<br/>

정리를 하자면 map에 대한 이해도(key : value 형태의 쌍을 이루는 데이터 구조임으로 key 값에 단어, value에 Node를 저장하는 형태는 것) 와
변수를 통해 메모리주소를 불어오는 것과 key를 통해 value의 메모리 주소를 불러오는 것을 같다는 것을 내 머리속에는 아에 따른 개념으로 받아들여서 생긴 오류였다.

결국에는 공부에 대한 깊이의 문제였다.

map도 자료구조이고 결국에는 데이터를 효율적으로 관리하기 위함이다.
즉, 데이터를 불러오고 저장한다는 사실은 변수와 다를 바가 없다.

문제의 본질이 뭔지 그 내부적으로 어떤 과정을 거치는지까지 생각을 하면서 공부를 해야 한다는 것을 깨닫게 해주는 귀중한 시간이었다.

한편으로썬, 비전공자로써 기본 cs 지식 부족에 대한 당연한 결과라고 생각한다. 따라서 cs공부 더 많이 하자...





