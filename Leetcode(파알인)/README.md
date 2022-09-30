# 👉 파이썬 알고리즘 인터뷰 정리본


<img src="../이미지/파알인-표지.jpg" width=60% />

<br>

구매 링크)
- [교보문고](http://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode=9791189909178&orderClick=LEa&Kc=)
- [알라딘](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=245495826)


- [파알인-github](https://github.com/onlybooks/algorithm-interview)

<br>

- [빅오, 시간복잡도](https://velog.io/@dltjq2323/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%98-%ED%9A%A8%EC%9C%A8%EC%84%B1%EC%8B%9C%EA%B0%84%EB%B3%B5%EC%9E%A1%EB%8F%84-%EA%B3%B5%EA%B0%84%EB%B3%B5%EC%9E%A1%EB%8F%84-%EB%B9%85%EC%98%A4)

<br>

# 자료구조
- [배열](https://velog.io/@dltjq2323/%EB%B0%B0%EC%97%B4)
- [연결리스트](https://velog.io/@dltjq2323/%EC%97%B0%EA%B2%B0%EB%A6%AC%EC%8A%A4%ED%8A%B8Linked-List)
- [스택](https://velog.io/@dltjq2323/%EC%8A%A4%ED%83%9DStack)
- [큐](https://velog.io/@dltjq2323/%ED%81%90Queue)
- [해시테이블](https://velog.io/@dltjq2323/%ED%95%B4%EC%8B%9C-%ED%85%8C%EC%9D%B4%EB%B8%94Hash-table)
- []()
- []()

<br><br>

# ✍️ 문제

<table>
  <tr>
    <td rowspan="6">문자열 조작</td>
    <td><a href="https://leetcode.com/problems/125-valid-palindrome/submissions/">유효한 팰린드롬</a></td>
    <td><a href="./1-문자열조작/125-valid-palindrome/풀이1(Array).py">풀이1(Array)</a>, 
    <a href="./1-문자열조작/125-valid-palindrome/풀이2(Deque).py">풀이2(Deque)</a>, 
    <a href="./1-문자열조작/125-valid-palindrome/풀이3(슬라이싱).py">풀이3(슬라이싱)</a></td>
    <td><a href="./1-문자열조작/125-valid-palindrome/NOTES.md">Notes</a><br/><a href="./문법/슬라이싱.md">슬라이싱</a></td>
  </tr>

  <tr>
    <td><a href="https://leetcode.com/problems/reverse-string/submissions/">문자열 뒤집기</a></td>
    <td><a href="./1-문자열조작/344-reverse-string/풀이1(투포인터).py">풀이1(투포인터)</a>, 
    <a href="./1-문자열조작/344-reverse-string/풀이2(내장함수).py">풀이2(내장함수)</a>, 
    <a href="./1-문자열조작/344-reverse-string/풀이3(슬라이싱).py">풀이3(슬라이싱)</a></td>
    <td><a href="./1-문자열조작/344-reverse-string/NOTES.md">Notes</a></td>
  </tr>

  <tr>
    <td><a href="https://leetcode.com/problems/reorder-data-in-log-files/">로그파일 재정렬</a></td>
    <td><a href="./1-문자열조작/937-reorder-data-in-log-files/풀이1(lambda).py">풀이1(lambda)</a>, 
    <a href="./1-문자열조작/937-reorder-data-in-log-files/풀이2.py">🤔 풀이2</a>
    <td><a href="./1-문자열조작/937-reorder-data-in-log-files/NOTES.md">Notes</a><br/><a href="./문법/lambda.md">lambda</a></td>
  </tr>


   <tr>
    <td><a href="https://leetcode.com/problems/most-common-word/">가장 흔한 단어</a></td>
    <td><a href="./1-문자열조작/819-most-common-word/풀이1(리스트컴프리헨션-max).py">풀이1(리스트컴프리헨션, max)</a>, 
    <a href="./1-문자열조작/819-most-common-word/풀이2(리스트컴프리헨션-Counter).py">풀이2(Couter)</a></td>
    <td><a href="./1-문자열조작/819-most-common-word/NOTES.md">Notes</a>
    <br><a href="./문법/Counter(most_common).md">Counter(most_common)</a></td>
  </tr>


   <tr>
    <td><a href="https://leetcode.com/problems/group-anagrams/submissions/">그룹 애너그램</a></td>
    <td><a href="./1-문자열조작/49-group-anagrams/풀이1(dict-정렬).py">풀이1(정렬)</a></td>
    <td>
      <a href="./1-문자열조작/49-group-anagrams/NOTES.md">Notes</a><br/>
      <a href="./문법/정렬(sorted,sort).md">정렬(sort, sorted)</a>
    </td>
  </tr>

  <tr>
      <td><a href="https://leetcode.com/problems/longest-palindromic-substring/submissions/">가장 긴 팰린드롬 부분 문자열</a></td>
      <td><a href="./1-문자열조작/5-longest-palindromic-substring/풀이1(투포인터).py">풀이1(투포인트)</a></td>
      <td><a href="./1-문자열조작/5-longest-palindromic-substring/NOTES.md">Notes</a><br/><a href="">유니코드, UTF-8</a></td>
  </tr>


  <tr>
      <td rowspan="6" href="https://velog.io/@dltjq2323/%EB%B0%B0%EC%97%B4">배열</td>
      <td><a href="https://leetcode.com/problems/two-sum/submissions/">두 수의 합</a></td>
      <td><a href="https://github.com/gyungsubLee/Algorithm-baekjoon/blob/main/Leetcode(%ED%8C%8C%EC%95%8C%EC%9D%B8)/1-two-sum/%ED%92%80%EC%9D%B41(%EB%B8%8C%EB%A3%A8%ED%8A%B8%ED%8F%AC%EC%8A%A4).py">풀이1(브루트포스)</a>, <a href="https://github.com/gyungsubLee/Algorithm-baekjoon/blob/main/Leetcode(%ED%8C%8C%EC%95%8C%EC%9D%B8)/1-two-sum/%ED%92%80%EC%9D%B42(in%ED%83%90%EC%83%89).py">풀이2(in탐색)</a>, <a href="https://github.com/gyungsubLee/Algorithm-baekjoon/blob/main/Leetcode(%ED%8C%8C%EC%95%8C%EC%9D%B8)/1-two-sum/%ED%92%80%EC%9D%B43-2(%EB%94%95%EC%85%94%EB%84%88%EB%A6%AC).py">풀이3(딕셔너리)</a>, <a href="https://github.com/gyungsubLee/Algorithm-with-python-/blob/main/Leetcode(%ED%8C%8C%EC%95%8C%EC%9D%B8)/1-two-sum/%ED%92%80%EC%9D%B44(%ED%88%AC%ED%8F%AC%EC%9D%B8%ED%84%B0).py">풀이4(투포인트)</a></td>
      <td><a href="https://github.com/gyungsubLee/Algorithm-baekjoon/blob/main/Leetcode(%ED%8C%8C%EC%95%8C%EC%9D%B8)/1-two-sum/NOTES.md">Notes</a></td>
  </tr>

  <tr>
      <td><a href="https://leetcode.com/problems/trapping-rain-water/">빗물 트래핑</a></td>
      <td>
        <a href="">풀이1-1(투포인터)</a>, 
        <a href="">풀이1-2(투포인터)</a>, 
        <a href="">🤔 풀이2(Stack)</a>
      </td>
      <td>
        <a href="">Notes</a>
        <br/><a href="">Notes</a>
      </td>
  </tr>

  <tr>
    <td><a href="https://leetcode.com/problems/3sum/"> 세 수의 합</a></td>
      <td>
        <a href="">풀이1(브루트포스)-X</a>, 
        <a href="">풀이2(투포인터)</a>
      </td>
      <td>
        <a href="">Notes</a>
        <br/><a href="">Notes</a>
      </td>
  </tr>

  <tr>
    <td><a href="https://leetcode.com/problems/array-partition/">
    배열 파티션1</a></td>
      <td>
        <a href="">풀이1(배열)</a>, 
        <a href="">풀이2(짝수합)</a>, 
        <a href="">풀이3(슬라이싱)</a>
      </td>
      <td>
        <a href="">Notes</a>
        <br/><a href="">Notes</a>
      </td>
  </tr>

  <tr>
    <td><a href="https://leetcode.com/problems/product-of-array-except-self/">자신을 제외한 배열의 곱</a></td>
      <td>
        <a href="">풀이1(left X right)</a>
      </td>
      <td>
        <a href="">Notes</a>
        <br/><a href="">Notes</a>
      </td>
  </tr>

  <tr>
    <td><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock/">주식을 사고팔기 가장 좋은 시점</a></td>
      <td>
        <a href="">풀이1(min,max)</a>
      </td>
      <td>
        <a href="">Notes</a>
      </td>
  </tr>



  <tr>
    <td rowspan="7" href="">연결리스트</td>
    <td><a href="https://leetcode.com/problems/palindrome-linked-list/submissions/">팰린드롬 연결리스트</a></td>
      <td>
        <a href="">풀이1(배열)</a>, 
        <a href="">풀이2(데큐)</a>, 
        <a href="">🤔 풀이3(런너)</a>
      </td>
      <td>
        <a href="">Notes</a>
      </td>
  </tr>
  
  <tr>
    <td><a href="https://leetcode.com/problems/merge-two-sorted-lists/"> 두 정렬 리스트 병합</a></td>
      <td>
        <a href="">풀이1(반복)</a>, 
        <a href="">🤔풀이2(재귀)</a>
      </td>
      <td>
        <a href="">Notes</a>
      </td>
  </tr>

  <tr>
    <td><a href="https://leetcode.com/problems/reverse-linked-list/">역순 연결리스트</a></td>
      <td>
        <a href="">풀이1(반복)</a>, 
        <a href="">🤔 풀이2(재귀)</a>
      </td>
      <td>
        <a href="">Notes</a>
      </td>
  </tr>

  <tr>
    <td><a href="https://leetcode.com/problems/add-two-numbers/">두 수의 덧셈</a></td>
      <td>
        <a href="">풀이1</a>, 
        <a href="">풀이2</a>, 
        <a href="">풀이3</a>
      </td>
      <td>
        <a href="">Notes</a>
        <br/><a href="">Notes</a>
      </td>
  </tr>

  <tr>
    <td><a href="https://leetcode.com/problems/swap-nodes-in-pairs/">페어의 노드 스왑</a></td>
      <td>
        <a href="">풀이1</a>, 
        <a href="">풀이2</a>, 
        <a href="">풀이3</a>
      </td>
      <td>
        <a href="">Notes</a>
        <br/><a href="">Notes</a>
      </td>
  </tr>

  <tr>
    <td><a href="https://leetcode.com/problems/odd-even-linked-list/">홀짝 연결리스트</a></td>
      <td>
        <a href="">풀이1</a>, 
        <a href="">풀이2</a>, 
        <a href="">풀이3</a>
      </td>
      <td>
        <a href="">Notes</a>
        <br/><a href="">Notes</a>
      </td>
  </tr>

  <tr>
    <td><a href="https://leetcode.com/problems/reverse-linked-list-ii/">역순 연결리스트II</a></td>
      <td>
        <a href="">풀이1</a>, 
        <a href="">풀이2</a>, 
        <a href="">풀이3</a>
      </td>
      <td>
        <a href="">Notes</a>
        <br/><a href="">Notes</a>
      </td>
  </tr>








  <tr>
    <td rowspan="3" href="">스택</td>
    <td><a href="https://leetcode.com/problems/valid-parentheses/">유효한 괄호</a></td>
      <td>
        <a href="">풀이1</a>, 
        <a href="">풀이2</a>, 
        <a href="">풀이3</a>
      </td>
      <td>
        <a href="">Notes</a>
      </td>
  </tr>

  <tr>
    <td><a href="https://leetcode.com/problems/remove-duplicate-letters/submissions/">중복문자제거</a></td>
      <td>
        <a href="">풀이1</a>, 
        <a href="">풀이2</a>, 
        <a href="">풀이3</a>
      </td>
      <td>
        <a href="">Notes</a>
      </td>
  </tr>

  <tr>
    <td><a href="https://leetcode.com/problems/daily-temperatures/">일일온도</a></td>
      <td>
        <a href="">풀이1</a>, 
        <a href="">풀이2</a>, 
        <a href="">풀이3</a>
      </td>
      <td>
        <a href="">Notes</a>
      </td>
  </tr>






  <tr>
    <td rowspan="3" href="">큐</td>
    <td><a href="https://leetcode.com/problems/implement-stack-using-queues/submissions/">큐를 이용한 스택 구현</a></td>
      <td>
        <a href="">풀이1(deque)</a>
      </td>
      <td>
        <a href="">Notes</a>
      </td>
  </tr>

  <tr>
    <td><a href="https://leetcode.com/problems/implement-queue-using-stacks/">스택을 이용한 큐 구현</a></td>
      <td>
        <a href="">풀이1(Array:2)</a>
      </td>
      <td>
        <a href="">Notes</a>
      </td>
  </tr>

  <tr>
    <td><a href="https://leetcode.com/problems/design-circular-queue/">원형 큐 디자인</a></td>
      <td>
        <a href="">풀이1(Array)</a>, 
        <a href="">풀이2(LinkedList)</a>
      </td>
      <td>
        <a href="">Notes</a>
      </td>
  </tr>

  
<tr>
    <td rowspan="2" href="">데크(deque)</td>
      <td>
        <a href="https://leetcode.com/problems/design-circular-deque/">원형 데크 디자인</a></td>
      <td>
        <a href="">풀이1</a>
      </td>
      <td>
        <a href="">Notes</a>
      </td>
  </tr>

  <tr>
    <td>
        <a href="https://leetcode.com/problems/merge-k-sorted-lists/">k개 정렬 리스트 병합</a></td>
      <td>
        <a href="">풀이1</a>
      </td>
      <td>
        <a href="">Notes</a>
      </td>
  </tr>



  <tr>
    <td rowspan="4" href="https://velog.io/@dltjq2323/%ED%95%B4%EC%8B%9C-%ED%85%8C%EC%9D%B4%EB%B8%94Hash-table">해시테이블</td>
      <td>
        <a href="https://leetcode.com/problems/design-hashmap/submissions/">해시맵 디자인</a></td>
      <td>
        <a href="">풀이1(연결리스트)</a>
      </td>
      <td>
        <a href="">Notes</a>
      </td>
  </tr>

  <tr>
    <td>
        <a href="https://leetcode.com/problems/jewels-and-stones/">보석과 돌</a></td>
      <td>
        <a href="">풀이1</a>
      </td>
      <td>
        <a href="">Notes</a>
      </td>
  </tr>

  <tr>
    <td>
        <a href="https://leetcode.com/problems/longest-substring-without-repeating-characters/">중복 문자 없는 가장 긴 부분 문자열</a></td>
      <td>
        <a href="">풀이1</a>
      </td>
      <td>
        <a href="">Notes</a>
      </td>
  </tr>

  <tr>
    <td>
        <a href="">상위 K 빈도 요소</a></td>
      <td>
        <a href="">풀이1</a>
      </td>
      <td>
        <a href="">Notes</a>
      </td>
  </tr>



  <tr>
    <td rowspan="8" href="">그래프(BFS, DFS)</td>
    <td>
        <a href="https://leetcode.com/problems/number-of-islands/submissions/">섬의 개수 </a></td>
      <td>
        <a href="">풀이1-1(DFS-재귀)</a>, 
        <a href="">풀이1-2(for문)</a>, 
        <a href="">풀이2(DFS-stack)</a>
      </td>
      <td>
        <a href="">Notes</a>
      </td>
  </tr>


  <tr>
    <td>
      <a href="https://leetcode.com/problems/letter-combinations-of-a-phone-number/">전화번호 문자 조합</a></td>
    <td>
      <a href="">풀이1(DFS-stack)</a>, 
        <a href="">풀이2-1(DFS-재귀)</a>, 
        <a href="">풀이2-2(함수합침)</a>
    </td>
    <td>
      <a href="">Notes</a>
    </td>
  </tr>


  <tr>
    <td>
      <a href="https://leetcode.com/problems/permutations/">순열</a></td>
    <td>
      <a href="">풀이1(DFS-재귀)</a>, 
      <a href="">풀이2(DFS-stack)</a>
    </td>
    <td>
      <a href="">Notes</a>
    </td>
  </tr>


  <tr>
    <td>
      <a href="https://leetcode.com/problems/combinations/submissions/">조합</a></td>
    <td>
      <a href="">풀이1-1(DFS-재귀)</a>, 
      <a href="">풀이1-2(DFS-재귀)</a>, 
      <a href="">풀이1-3(method-func)</a>, 
      <a href="">풀이2(DFS-Stack)</a>
    </td>
    <td>
      <a href="">Notes</a>
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://leetcode.com/problems/combination-sum/submissions/">조합의 합</a></td>
    <td>
      <a href="">풀이1(DFS-재귀)</a>, 
      <a href="">풀이1(DFS-Stack)</a>
    </td>
    <td>
      <a href="">Notes</a>
    </td>
  </tr>


  <tr>
    <td>
      <a href="https://leetcode.com/problems/subsets/">부분집합</a></td>
    <td>
      <a href="">풀이1(DFS-재귀)</a>, 
      <a href="">풀이1(DFS-Stack)</a>
    </td>
    <td>
      <a href="">Notes</a>
    </td>
  </tr>


  <tr>
    <td>
      <a href="https://leetcode.com/problems/reconstruct-itinerary/">🤔 일정 재구성</a></td>
    <td>
      <a href="">풀이1-1(DFS-재귀)</a>,
      <a href="">풀이1-2(최적화-reverse)</a>, 
      <a href="">풀이1(DFS-Stack)</a>
    </td>
    <td>
      <a href="">Notes</a>
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://leetcode.com/problems/course-schedule/">🤔 코스 스케줄</a></td>
    <td>
      <a href="">풀이1</a>
    </td>
    <td>
      <a href="">Notes</a>
    </td>
  </tr>





  <tr>
    <td rowspan="2" href="">최단 경로 문제</td>
    <td>
      <a href="https://leetcode.com/problems/network-delay-time/submissions/">네트워크 딜레이 타임</a></td>
    <td>
      <a href="">풀이1</a>
    </td>
    <td>
      <a href="">Notes</a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://leetcode.com/problems/cheapest-flights-within-k-stops/">K 경유지 내 가장 저렴한 항공권</a></td>
    <td>
      <a href="">풀이1</a>
    </td>
    <td>
      <a href="">Notes</a>
    </td>
  </tr>


  <tr>
    <td rowspan="8"><a href="">😗 이진 트리</a></td>
    <td>
      <a href="https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/">이진트리의 최대 깊이</a></td>
    <td>
      <a href="./10-이진트리/104-maximum-depth-of-binary-tree/풀이1(BFS).py">풀이1(BFS))</a>
    </td>
    <td>
      <a href="./10-이진트리/104-maximum-depth-of-binary-tree/NOTES.md">Notes</a>
    </td>
  </tr>



  <tr>
    <td>
      <a href="https://leetcode.com/problems/diameter-of-binary-tree/">이진트리의 직경</a></td>
    <td>
      <a href="">🤔풀이1(DFS)</a>
    </td>
    <td>
      <a href="">Notes</a>
    </td>
  </tr>


  <tr>
    <td>
      <a href="https://leetcode.com/problems/longest-univalue-path/">가장 긴 동일 값의 경로</a></td>
    <td>
      <a href="./10-이진트리/687-longest-univalue-path/풀이1(재귀).py">풀이1(DFS-재귀)</a>
    </td>
    <td>
      <a href="./10-이진트리/687-longest-univalue-path/NOTES.md">Notes</a>
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://leetcode.com/problems/invert-binary-tree/submissions/">이진트리 반전</a></td>
    <td>
      <a href="./10-이진트리/226-invert-binary-tree/풀이1(DFS-재귀).py">풀이1(DFS-재귀)</a>, 
      <a href="./10-이진트리/226-invert-binary-tree/풀이2(DFS-stack).py">풀이2(DFS-stack)</a>, 
      <a href="./10-이진트리/226-invert-binary-tree/풀이3(BFS-Queue).py">풀이3(BFS-Queue)</a>
    </td>
    <td>
      <a href="./10-이진트리/226-invert-binary-tree/NOTES.md">Notes</a>
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://leetcode.com/problems/merge-two-binary-trees/submissions/">두 이진트리 병합</a></td>
    <td>
      <a href="./10-이진트리/617-merge-two-binary-trees/풀이1(DFS-재귀).py">풀이1(DFS-재귀)</a>
    </td>
    <td>
      <a href="">Notes</a>
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://leetcode.com/problems/serialize-and-deserialize-binary-tree/submissions/">이진트리 직렬화&역직렬화</a></td>
    <td>
      <a href="./10-이진트리/297-serialize-and-deserialize-binary-tree/풀이1(BFS-queue).py">풀이1(BFS-queue)</a>
    </td>
    <td>
      <a href="">Notes</a>
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://leetcode.com/problems/balanced-binary-tree/">균형 이진트리</a></td>
    <td>
      <a href="./10-이진트리/110-balanced-binary-tree/풀이1(DFS-재귀).py">풀이1(DFS-재귀)</a>
    </td>
    <td>
      <a href="./10-이진트리/110-balanced-binary-tree/NOTES.md">Notes</a>
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://leetcode.com/problems/minimum-height-trees/submissions/">최노 높이 트리</a></td>
    <td>
      <a href="./10-이진트리/310-minimum-height-trees/풀이1(BFS).py">풀이1(BFS)</a>
    </td>
    <td>
      <a href="./10-이진트리/110-balanced-binary-tree/NOTES.md">Notes</a>
    </td>
  </tr>


  <tr>
    <td rowspan="4" href="">이진 탐색 트리</td>
    <td>
      <a href="https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/submissions/">정렬된 배열의 이진탐색트리 반환</a></td>
    <td>
      <a href="./11-이진탐색트리/108-convert-sorted-array-to-binary-search-tree/풀이1(재귀).py">풀이1(재귀)</a>
    </td>
    <td>
      <a href="./11-이진탐색트리/108-convert-sorted-array-to-binary-search-tree/NOTES.md">Notes</a>
    </td>
  </tr>


  <tr>
    <td>
      <a href="https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/">이진탐색트리를 더 큰 수 합계 트리로</a></td>
    <td>
      <a href="./11-이진탐색트리/1038-binary-search-tree-to-greater-sum-tree/풀이1(DFS-재귀).py">풀이1(DFS-재귀)</a>
    </td>
    <td>
      <a href="">Notes</a>
    </td>
  </tr>


  <tr>
    <td>
      <a href="https://leetcode.com/problems/range-sum-of-bst/">이진탐색트리 합의 범위</a></td>
    <td>
      <a href="./11-이진탐색트리/938-range-sum-of-bst/풀이1(DFS-재귀).py">풀이1(DFS-재귀)</a>, 
      <a href="./11-이진탐색트리/938-range-sum-of-bst/풀이2(DFS-Stack).py">풀이2(DFS-stack)</a>, 
      <a href="./11-이진탐색트리/938-range-sum-of-bst/풀이3(BFS-Queue).py">풀이3(BFS-Queue)</a>
    </td>
    <td>
      <a href="">Notes</a>
    </td>
  </tr>


  <tr>
    <td>
      <a href="https://leetcode.com/problems/minimum-distance-between-bst-nodes/">이진탐색트리 노드 간 최소거리</a></td>
    <td>
      <a href="./11-이진탐색트리/783-minimum-distance-between-bst-nodes/풀이1(재귀).py">🤔 풀이1(재귀)</a>, 
      <a href="./11-이진탐색트리/783-minimum-distance-between-bst-nodes/풀이2(Stack).py">🤔 풀이2(Stack)</a>
    </td>
    <td>
      <a href="">Notes</a>
    </td>
  </tr>


  <tr>
    <td rowspan="1" href="">트리 순회</td>
    <td>
      <a href="https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/submissions/">전위, 중위 순회 결과로 이진트리 구축</a></td>
    <td>
      <a href="./11-이진탐색트리/105-construct-binary-tree-from-preorder-and-inorder-traversal/풀이1(재귀).py">풀이1(재귀)</a>
    </td>
    <td>
      <a href="">Notes</a>
    </td>
  </tr>

  <tr>
    <td rowspan="1"><a href="https://velog.io/@dltjq2323/%ED%9E%99heap">힙(heap)</a></td>
    <td>
      <a href="https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/">배열의 K번째 큰 요소</a></td>
    <td>
      <a href="./12-힙/215-kth-largest-element-in-an-array/풀이1(maxHeap구현).py">풀이1(maxHeap구현)</a>, 
      <a href="./12-힙/215-kth-largest-element-in-an-array/풀이2(heapq모듈).py">풀이2(heapq모듈)</a>, 
      <a href="./12-힙/215-kth-largest-element-in-an-array/풀이3(정렬).py">풀이2(정렬)</a>
    </td>
    <td>
      <a href="./12-힙/215-kth-largest-element-in-an-array/NOTES.md">Notes</a>,
      <a href="./12-힙/힙연산.md">힙 연산</a>
    </td>
  </tr>


  <tr>
    <td rowspan="2"><a href="https://velog.io/@dltjq2323/트라이Trie#트라이trie">트라이</a></td>
    <td>
      <a href="https://leetcode.com/problems/implement-trie-prefix-tree/submissions/">트라이 구현</a></td>
    <td>
      <a href="./13-트라이/208-implement-trie-prefix-tree/풀이1(트라이-Map).py">풀이1(트라이-Map)</a>, 
      <a href="./13-트라이/208-implement-trie-prefix-tree/풀이2(트라이-defaultdict).py">풀이2(트라이-defaultdict)</a>
    </td>
    <td>
      <a href="./13-트라이/208-implement-trie-prefix-tree/NOTES.md">Notes</a>
    </td>
  </tr>


  <tr>
    <td>
      <a href="https://leetcode.com/problems/palindrome-pairs/">🤔 팰린드롬 페어</a></td>
    <td>
      <a href="./13-트라이/336-palindrome-pairs/풀이1(Trie).py">풀이1(Trie)</a>
    </td>
    <td>
      <a href="./13-트라이/336-palindrome-pairs/NOTES.md">Notes</a>
    </td>
  </tr>

  tr>
    <td rowspan="7"><a href="">정렬</a></td>
    <td>
      <a href="https://leetcode.com/problems/sort-list/">리스트 정렬</a></td>
    <td>
      <a href="./14-정렬/148-sort-list/풀이1(병합정렬-런너).py">풀이1(병합정렬-런너)</a>, 
      <a href="./14-정렬/148-sort-list/풀이2(sort).py">풀이2(sort)</a>
    </td>
    <td>
      <a href="./14-정렬/148-sort-list/NOTES.md">Notes</a>
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://leetcode.com/problems/merge-intervals/submissions/">구간 병합</a></td>
    <td>
      <a href="./14-정렬/56-merge-intervals/풀이1(lambda).py">풀이1(lambda)</a>
    </td>
    <td>
      <a href="./14-정렬/56-merge-intervals/NOTES.md">Notes</a>
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://leetcode.com/problems/insertion-sort-list/">삽입 정렬 리스트</a></td>
    <td>
      <a href="./14-정렬/147-insertion-sort-list/풀이1(삽입정렬).py">풀이1(삽입정렬)</a>, 
      <a href="./14-정렬/147-insertion-sort-list/풀이2(개선).py">풀이2(개선)</a>
    </td>
    <td>
      <a href="./14-정렬/147-insertion-sort-list/NOTES.md">Notes</a>
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://leetcode.com/problems/largest-number/submissions/">가장 큰 수</a></td>
    <td>
      <a href="./14-정렬/179-largest-number/풀이1(삽입정렬).py">🤔 풀이1(삽입정렬)</a>
    </td>
    <td>
      <a href="./14-정렬/179-largest-number/NOTES.md">Notes</a>
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://leetcode.com/problems/valid-anagram/submissions/">유효한 애너그램</a></td>
    <td>
      <a href="./14-정렬/242-valid-anagram/풀이1(sorted).py">풀이1(sorted)</a>, 
      <a href="./14-정렬/242-valid-anagram/풀이2(dict).py">풀이2(dict)</a>
    </td>
    <td>
      <a href="./14-정렬/242-valid-anagram/NOTES.md">Notes</a>
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://leetcode.com/problems/sort-colors/">색 정렬</a></td>
    <td>
      <a href="./14-정렬/75-sort-colors/풀이1(퀵정렬).py">풀이1(퀵정렬)</a>
    </td>
    <td>
      <a href=./14-정렬/75-sort-colors/NOTES.md">Notes</a>
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://leetcode.com/problems/k-closest-points-to-origin/submissions/">원점에 K번째로 가까운 점</a></td>
    <td>
      <a href="./14-정렬/973-k-closest-points-to-origin/풀이1(lambda).py">풀이1(lambda)</a>, 
      <a href="./14-정렬/973-k-closest-points-to-origin/풀이2(heapq).py">풀이2(heapq)</a>
    </td>
    <td>
      <a href="./14-정렬/973-k-closest-points-to-origin/NOTES.md">Notes</a>
    </td>
  </tr>


<tr>
    <td rowspan="5"><a href="">🤔 이진 검색</a></td>
    <td>
      <a href="https://leetcode.com/problems/binary-search/">이진 검색</a></td>
    <td>
      <a href="./15-이진검색/704-binary-search/풀이1(재귀, 투포인터).py">풀이1(재귀, 투포인터)</a>, 
      <a href="./15-이진검색/704-binary-search/풀이2(반복, 투포인터).py">풀이2(반복, 투포인터)</a>
    </td>
    <td>
      <a href="./15-이진검색/704-binary-search/NOTES.md">Notes</a>
    </td>
  </tr>


  <tr>
    <td>
      <a href="https://leetcode.com/problems/search-in-rotated-sorted-array/">🤔 회전 정렬된 배열 검색</a></td>
    <td>
      <a href="./15-이진검색/33-search-in-rotated-sorted-array/풀이1(피벗,이진검색).py">풀이1(피벗,이진검색)</a>, 
      <a href="./15-이진검색/33-search-in-rotated-sorted-array/풀이2(투포인터).py">풀이2(투포인터)</a>
    </td>
    <td>
      <a href="./15-이진검색/33-search-in-rotated-sorted-array/NOTES.md">Notes</a>
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://leetcode.com/problems/intersection-of-two-arrays/">두 배열의 교집합</a></td>
    <td>
      <a href="./15-이진검색/349-intersection-of-two-arrays/풀이1(브루트 포스).py">풀이1(브루트 포스)</a>, 
      <a href="./15-이진검색/349-intersection-of-two-arrays/풀이2(이진검색).py">풀이2(이진검색)</a>, 
      <a href="./15-이진검색/349-intersection-of-two-arrays/풀이3(투포인터).py">풀이3(투포인터)</a>
    </td>
    <td>
      <a href="./15-이진검색/349-intersection-of-two-arrays/NOTES.md">Notes</a>
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/">두 수의 합</a></td>
    <td>
      <a href="./15-이진검색/167-two-sum-ii-input-array-is-sorted/풀이1(투포인터).py">풀이1(투포인터)</a>, 
      <a href="./15-이진검색/167-two-sum-ii-input-array-is-sorted/풀이2(이진검색-반복, 투포인터).py">풀이2(이진검색-반복, 투포인터)</a>, 
      <a href="./15-이진검색/167-two-sum-ii-input-array-is-sorted/풀이3(이진검색-재귀, 투포인터).py">풀이3(이진검색-재귀, 투포인터)</a>
    </td>
    <td>
      <a href="./15-이진검색/167-two-sum-ii-input-array-is-sorted/NOTES.md">Notes</a>
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://leetcode.com/problems/search-a-2d-matrix-ii/">2D 행렬 검색 II</a></td>
    <td>
      <a href="./15-이진검색/240-search-a-2d-matrix-ii/풀이1(이진검색-재귀,투포인터).py">풀이1(이진검색-재귀,투포인터)</a>, 
      <a href="./15-이진검색/240-search-a-2d-matrix-ii/풀이2(투포인터).py">풀이2(투포인터)</a>
    </td>
    <td>
      <a href="./15-이진검색/240-search-a-2d-matrix-ii/NOTES.md">Notes</a>
    </td>
  </tr>



<tr>
    <td rowspan="2"><a href="">샘플</a></td>
    <td>
      <a href=""></a></td>
    <td>
      <a href="">풀이1</a>
    </td>
    <td>
      <a href="">Notes</a>
    </td>
  </tr>


  <tr>
    <td>
      <a href=""></a></td>
    <td>
      <a href="">풀이1</a>
    </td>
    <td>
      <a href="">Notes</a>
    </td>
  </tr>


  
<tr>
    <td rowspan="3"><a href="">슬라이딩 윈도우</a></td>
    <td>
      <a href="https://leetcode.com/problems/sliding-window-maximum/">🤔 최대 슬라이딩 윈도우</a></td>
    <td>
      <a href="./17-슬라이싱윈도우/239-sliding-window-maximum/풀이1(for, max).py">풀이1(for, max)</a>, 
      <a href="./17-슬라이싱윈도우/239-sliding-window-maximum/풀이2(deque).py">풀이2(deque)</a>
    </td>
    <td>
      <a href="./17-슬라이싱윈도우/239-sliding-window-maximum/NOTES.md">Notes</a>
    </td>
  </tr>



  <tr>
    <td>
      <a href="https://leetcode.com/problems/minimum-window-substring/">부분 문자열이 포함된 최소 윈도우</a></td>
    <td>
      <a href="./17-슬라이싱윈도우/76-minimum-window-substring/풀이1(투포인터, 슬라이딩윈도우).py">풀이1(투포인터, 슬라이딩윈도우)</a>, 
      <a href="./17-슬라이싱윈도우/76-minimum-window-substring/풀이2(counter).py">풀이2(counter)</a>
    </td>
    <td>
      <a href="./17-슬라이싱윈도우/76-minimum-window-substring/NOTES.md">Notes</a>
    </td>
  </tr>

  <tr>
    <td>
      <a href=""></a></td>
    <td>
      <a href="">풀이1</a>
    </td>
    <td>
      <a href="">Notes</a>
    </td>
  </tr>

  


<tr>
    <td rowspan="2"><a href="">샘플</a></td>
    <td>
      <a href=""></a></td>
    <td>
      <a href="">풀이1</a>
    </td>
    <td>
      <a href="">Notes</a>
    </td>
  </tr>


  <tr>
    <td>
      <a href=""></a></td>
    <td>
      <a href="">풀이1</a>
    </td>
    <td>
      <a href="">Notes</a>
    </td>
  </tr>

</table>

