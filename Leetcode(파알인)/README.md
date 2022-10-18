# 👉 파이썬 알고리즘 인터뷰 정리본

<br>

구매 링크 - [교보문고](http://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode=9791189909178&orderClick=LEa&Kc=), [알라딘](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=245495826)

[파알인-github](https://github.com/onlybooks/algorithm-interview)

<br>

<img src="https://user-images.githubusercontent.com/95308384/194082748-15cb2f0f-2cd0-47b4-8f28-164700b92ebe.png" width=60% />

<br>

# ✍️ 문법

| 제목                                                                  |
| --------------------------------------------------------------------- |
| [람다표현식](./문법/%EB%9E%8C%EB%8B%A4%ED%91%9C%ED%98%84%EC%8B%9D.md) |
| [슬라이싱](./문법/슬라이싱.md)                                        |
| [정렬(sorted,sort)](<./문법/정렬(sorted,sort).md>)                    |

<br>

# ✍️ 문제

<table>
  <tr>
    <td rowspan="6">문자열 조작</td>
    <td><a href="https://leetcode.com/problems/125-valid-palindrome/submissions/">유효한 팰린드롬</a></td>
    <td><a href="./01-문자열조작/125-valid-palindrome/풀이1(Array).py">풀이1(Array)</a>, 
    <a href="./01-문자열조작/125-valid-palindrome/풀이2(Deque).py">풀이2(Deque)</a>, 
    <a href="./01-문자열조작/125-valid-palindrome/풀이3(슬라이싱).py">풀이3(슬라이싱)</a></td>
    <td><a href="./01-문자열조작/125-valid-palindrome/NOTES.md">Notes</a></td>
  </tr>

  <tr>
    <td><a href="https://leetcode.com/problems/reverse-string/submissions/">문자열 뒤집기</a></td>
    <td><a href="./01-문자열조작/344-reverse-string/풀이1(투포인터).py">풀이1(투포인터)</a>, 
    <a href="./01-문자열조작/344-reverse-string/풀이2(내장함수).py">풀이2(내장함수)</a>, 
    <a href="./01-문자열조작/344-reverse-string/풀이3(슬라이싱).py">풀이3(슬라이싱)</a></td>
    <td><a href="./01-문자열조작/344-reverse-string/NOTES.md">Notes</a></td>
  </tr>

  <tr>
    <td><a href="https://leetcode.com/problems/reorder-data-in-log-files/">로그파일 재정렬</a></td>
    <td><a href="./01-문자열조작/937-reorder-data-in-log-files/풀이1(lambda).py">풀이1(lambda)</a>, 
    <a href="./01-문자열조작/937-reorder-data-in-log-files/풀이2.py">🤔 풀이2</a>
    <td><a href="./01-문자열조작/937-reorder-data-in-log-files/NOTES.md">Notes</a></td>
  </tr>

   <tr>
    <td><a href="https://leetcode.com/problems/most-common-word/">가장 흔한 단어</a></td>
    <td><a href="./01-문자열조작/819-most-common-word/풀이1(리스트컴프리헨션-max).py">풀이1(리스트컴프리헨션, max)</a>, 
    <a href="./01-문자열조작/819-most-common-word/풀이2(리스트컴프리헨션-Counter).py">풀이2(Couter)</a></td>
    <td><a href="./01-문자열조작/819-most-common-word/NOTES.md">Notes</a></td>
  </tr>

   <tr>
    <td><a href="https://leetcode.com/problems/group-anagrams/submissions/">그룹 애너그램</a></td>
    <td><a href="./01-문자열조작/49-group-anagrams/풀이1(dict-정렬).py">풀이1(정렬)</a></td>
    <td>
      <a href="./01-문자열조작/49-group-anagrams/NOTES.md">Notes</a><br/>
    </td>
  </tr>

  <tr>
      <td><a href="https://leetcode.com/problems/longest-palindromic-substring/submissions/">가장 긴 팰린드롬 부분 문자열</a></td>
      <td><a href="./01-문자열조작/5-longest-palindromic-substring/풀이1(투포인터).py">풀이1(투포인트)</a></td>
      <td><a href="./01-문자열조작/5-longest-palindromic-substring/NOTES.md">Notes</a></td>
  </tr>

  <tr>
      <td rowspan="6" ><a href="https://velog.io/@dltjq2323/%EB%B0%B0%EC%97%B4">배열</a></td>
      <td><a href="https://leetcode.com/problems/two-sum/submissions/">두 수의 합</a></td>
      <td>
      <a href="./02-배열/01-two-sum/풀이1(브루트포스).py">풀이1(브루트포스)</a>, 
      <a href="./02-배열/01-two-sum/풀이2(in탐색).py">풀이2(in탐색)</a>, 
      <a href="./02-배열/01-two-sum/풀이3-1(딕셔너리).py">풀이3-1(딕셔너리)</a>,
      <a href="./02-배열/01-two-sum/풀이3-2(딕셔너리).py">풀이3-2(딕셔너리)</a>, 
      <a href="./02-배열/01-two-sum/풀이4(투포인트).py">풀이4(투포인트)</a></td>
      <td><a href="./02-배열/01-two-sum/NOTES.md">Notes</a></td>
  </tr>
  <tr>
      <td><a href="https://leetcode.com/problems/trapping-rain-water/">빗물 트래핑</a></td>
      <td>
        <a href="./02-배열/42-trapping-rain-water/풀이1-1(투포인터).py">풀이1-1(투포인터)</a>, 
        <a href="./02-배열/42-trapping-rain-water/풀이1-2(투포인터).py">풀이1-2(투포인터)</a>, 
        <a href="./02-배열/42-trapping-rain-water/풀이2(stack).py">🤔 풀이2(stack)</a>
      </td>
      <td>
        <a href="./02-배열/42-trapping-rain-water/NOTES.md">Notes</a>
      </td>
  </tr>

  <tr>
    <td><a href="https://leetcode.com/problems/3sum/"> 세 수의 합</a></td>
      <td>
        <a href="./02-배열/15-3sum/풀이1(브루트포스).py">풀이1(브루트포스)X</a>, 
        <a href="./02-배열/15-3sum/풀이2(투포인터).py">풀이2(투포인터)</a>
      </td>
      <td>
        <a href="./02-배열/15-3sum/NOTES.md">Notes</a>
      </td>
  </tr>

  <tr>
    <td><a href="https://leetcode.com/problems/array-partition/">
    배열 파티션1</a></td>
      <td>
        <a href="./02-배열/561-array-partition/풀이1(배열).py">풀이1(배열)</a>, 
        <a href="./02-배열/561-array-partition/풀이2(짝수합).py">풀이2(짝수합)</a>, 
        <a href="./02-배열/561-array-partition/풀이3(슬라이싱).py">풀이3(슬라이싱)</a>
      </td>
      <td>
        <a href="./02-배열/561-array-partition/NOTES.md">Notes</a>
      </td>
  </tr>

  <tr>
    <td><a href="https://leetcode.com/problems/product-of-array-except-self/">자신을 제외한 배열의 곱</a></td>
      <td>
        <a href="./02-배열/238-product-of-array-except-self/풀이1(left X right).py">풀이1(left X right)</a>
      </td>
      <td>
        <a href="./02-배열/238-product-of-array-except-self/NOTES.md">Notes</a>
      </td>
  </tr>

  <tr>
    <td><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock/">주식을 사고팔기 가장 좋은 시점</a></td>
      <td>
        <a href="./02-배열/121-best-time-to-buy-and-sell-stock/풀이1(min,max).py">풀이1(min,max)</a>
      </td>
      <td>
        <a href="./02-배열/121-best-time-to-buy-and-sell-stock/NOTES.md">Notes</a>
      </td>
  </tr>

  <tr>
    <td rowspan="7"><a href="https://velog.io/@dltjq2323/%EC%97%B0%EA%B2%B0%EB%A6%AC%EC%8A%A4%ED%8A%B8Linked-List">😗 연결리스트</a></td>
    <td><a href="https://leetcode.com/problems/palindrome-linked-list/">팰린드롬 연결리스트</a></td>
      <td>
        <a href="./03-연결리스트/234-palindrome-linked-list/풀이1(Array).py">풀이1(Array)</a>, 
        <a href="./03-연결리스트/234-palindrome-linked-list/풀이2(Deque).py">풀이2(Deque)</a>,
        <a href="./03-연결리스트/234-palindrome-linked-list/풀이3(투포인터).py">풀이3(투포인터)</a>, 
        <a href="./03-연결리스트/234-palindrome-linked-list/풀이4-1(런너).py">🤔 풀이4-1(런너)</a>, 
        <a href="./03-연결리스트/234-palindrome-linked-list/풀이4-2(런너).py">🤔 풀이4-2(런너)</a>, 
      </td>
      <td>
        <a href="./03-연결리스트/234-palindrome-linked-list/NOTES.md">Notes</a>
      </td>
  </tr>
  
  <tr>
    <td><a href="https://leetcode.com/problems/merge-two-sorted-lists/"> 두 정렬 리스트 병합</a></td>
      <td>
        <a href="./03-연결리스트/21-merge-two-sorted-lists/풀이1(dummy).py">풀이1(dummy)</a>, 
        <a href="./03-연결리스트/21-merge-two-sorted-lists/풀이2(재귀).py">😗 풀이2(재귀)</a>
      </td>
      <td>
        <a href="./03-연결리스트/21-merge-two-sorted-lists/NOTES.md">Notes</a>
      </td>
  </tr>

  <tr>
    <td><a href="https://leetcode.com/problems/reverse-linked-list/">역순 연결리스트</a></td>
      <td>
        <a href="./03-연결리스트/206-reverse-linked-list/풀이1(반복).py">풀이1(반복)</a>, 
        <a href="./03-연결리스트/206-reverse-linked-list/풀이2(재귀).py">😗 풀이2(재귀)</a>
      </td>
      <td>
        <a href="./03-연결리스트/206-reverse-linked-list/NOTES.md">Notes</a>
      </td>
  </tr>

  <tr>
    <td><a href="https://leetcode.com/problems/add-two-numbers/">두 수의 덧셈</a></td>
      <td>
        <a href="./03-연결리스트/2-add-two-numbers/풀이1-1(역순-반복, LL-L).py">풀이1-1(역순-반복, LL-L)</a>, 
        <a href="./03-연결리스트/2-add-two-numbers/풀이1-2(역순-재귀, LL-L).py">풀이1-2(역순-재귀, LL-L)</a>, 
        <a href="./03-연결리스트/2-add-two-numbers/풀이2(전가산기).py">🤔 풀이2(전가산기)</a>
      </td>
      <td>
        <a href="./03-연결리스트/2-add-two-numbers/NOTES.md">Notes</a>
      </td>
  </tr>

  <tr>
    <td><a href="https://leetcode.com/problems/swap-nodes-in-pairs/">페어의 노드 스왑</a></td>
      <td>
        <a href="./03-연결리스트/24-swap-nodes-in-pairs/풀이1(값만변경).py">풀이1(값만변경</a>, 
        <a href="./03-연결리스트/24-swap-nodes-in-pairs/풀이2(반복).py">풀이2(반복)</a>, 
        <a href="./03-연결리스트/24-swap-nodes-in-pairs/풀이3(재귀).py">풀이3(재귀)</a>
      </td>
      <td>
        <a href="./03-연결리스트/24-swap-nodes-in-pairs/NOTES.md">Notes</a>
      </td>
  </tr>

  <tr>
    <td><a href="https://leetcode.com/problems/odd-even-linked-list/">홀짝 연결리스트</a></td>
      <td>
        <a href="./03-연결리스트/328-odd-even-linked-list/풀이1(반복)">풀이1(반복)</a>
      </td>
      <td>
        <a href="./03-연결리스트/328-odd-even-linked-list/NOTES.md">Notes</a>
      </td>
  </tr>

  <tr>
    <td><a href="https://leetcode.com/problems/reverse-linked-list-ii/">역순 연결리스트II</a></td>
      <td>
        <a href="./03-연결리스트/92-reverse-linked-list-ii/풀이1(LL-L,투포인터).py">풀이1(LL-L,투포인터)</a>, 
        <a href="./03-연결리스트/92-reverse-linked-list-ii/풀이2(LL,reverse).py">😗 풀이2(LL,reverse)</a>
      </td>
      <td>
        <a href="./03-연결리스트/92-reverse-linked-list-ii/NOTES.md">Notes</a>
      </td>
  </tr>

  <tr>
    <td rowspan="3"><a href="https://velog.io/@dltjq2323/%EC%8A%A4%ED%83%9DStack">스택</a></td>
    <td><a href="https://leetcode.com/problems/valid-parentheses/">유효한 괄호</a></td>
      <td>
        <a href="./04-스택/20-valid-parentheses/풀이1(map,list).py">풀이1(map,list)</a>, 
        <a href="./04-스택/20-valid-parentheses/풀이2(replace).py">풀이2(replace)</a>
      </td>
      <td>
        <a href="./04-스택/20-valid-parentheses/NOTES.md">Notes</a>
      </td>
  </tr>

  <tr>
    <td><a href="https://leetcode.com/problems/remove-duplicate-letters/">중복문자제거</a></td>
      <td>
        <a href="./04-스택/316-remove-duplicate-letters/풀이1(재귀).py">풀이1(재귀)</a>, 
        <a href="./04-스택/316-remove-duplicate-letters/풀이2(stack).py">풀이2(stack)</a>
      </td>
      <td>
        <a href="./04-스택/316-remove-duplicate-letters/NOTES.md">Notes</a>
      </td>
  </tr>

  <tr>
    <td><a href="https://leetcode.com/problems/daily-temperatures/">일일온도</a></td>
      <td>
        <a href="./04-스택/739-daily-temperatures/풀이1(브루트포스).py">풀이1(브루트포스)-시간초과</a>, 
        <a href="./04-스택/739-daily-temperatures/풀이2(Stack).py">풀이2(Stack)</a>
      </td>
      <td>
        <a href="./04-스택/739-daily-temperatures/NOTES.md">Notes</a>
      </td>
  </tr>

  <tr>
    <td rowspan="3"><a href="https://velog.io/@dltjq2323/%ED%81%90Queue">😗 큐</a></td>
    <td><a href="https://leetcode.com/problems/implement-stack-using-queues/">😗 큐를 이용한 스택 구현</a></td>
      <td>
        <a href="./05-큐/225-implement-stack-using-queues/풀이1(deque).py">풀이1(deque)</a>
      </td>
      <td>
        <a href="./05-큐/225-implement-stack-using-queues/NOTES.md">Notes</a>
      </td>
  </tr>

  <tr>
    <td><a href="https://leetcode.com/problems/implement-queue-using-stacks/">😗 스택을 이용한 큐 구현</a></td>
      <td>
        <a href="./05-큐/232-implement-queue-using-stacks/풀이1(stack).py">풀이1(stack)</a>
      </td>`
      <td>
        <a href="./05-큐/232-implement-queue-using-stacks/NOTES.md">Notes</a>
      </td>
  </tr>

  <tr>
    <td><a href="https://leetcode.com/problems/design-circular-queue/">😗 원형 큐 디자인</a></td>
      <td>
        <a href="./05-큐/622-design-circular-queue/풀이1-1(Array).py">풀이1-1(Array)</a>, 
        <a href="./05-큐/622-design-circular-queue/풀이1-2(Array).py">풀이1-2(Array)</a>, 
        <a href="./05-큐/622-design-circular-queue/풀이2(LinkedList).py">풀이2(LinkedList)</a>
      </td>
      <td>
        <a href="./05-큐/622-design-circular-queue/NOTES.md">Notes</a>
      </td>
  </tr>

<tr>
    <td rowspan="2"><a href="https://velog.io/@dltjq2323/Deque%EB%8D%B0%ED%81%90">데크(deque)</a></td>
      <td>
        <a href="https://leetcode.com/problems/design-circular-deque/">원형 데크 디자인</a></td>
      <td>
        <a href="./06-데크/641-design-circular-deque/풀이1(이중연결리스트).py">풀이1(이중연결리스트)</a>
      </td>
      <td>
        <a href="./06-데크/641-design-circular-deque/NOTES.md">Notes</a>
      </td>
  </tr>

  <tr>
    <td>
        <a href="https://leetcode.com/problems/merge-k-sorted-lists/">k개 정렬 리스트 병합</a></td>
      <td>
        <a href="./06-데크/23-merge-k-sorted-lists/풀이1(우선순위큐).py">풀이1(우선순위큐)</a>, 
        <a href="./06-데크/23-merge-k-sorted-lists/풀이2(mergesort).py">풀이2(mergesort)</a>
      </td>
      <td>
        <a href="./06-데크/23-merge-k-sorted-lists/NOTES.md">Notes</a>
      </td>
  </tr>

  <tr>
    <td rowspan="4"><a href="https://velog.io/@dltjq2323/%ED%95%B4%EC%8B%9C-%ED%85%8C%EC%9D%B4%EB%B8%94Hash-table" >해시테이블</a></td>
      <td>
        <a href="https://leetcode.com/problems/design-hashmap/">해시맵 디자인</a></td>
      <td>
        <a href="./07-해시테이블/706-design-hashmap/풀이1(연결리스트).py">풀이1(연결리스트)</a>
      </td>
      <td>
        <a href="./07-해시테이블/706-design-hashmap/NOTES.md">Notes</a>
      </td>
  </tr>
  <tr>
    <td>
        <a href="https://leetcode.com/problems/jewels-and-stones/">보석과 돌</a></td>
      <td>
        <a href="./07-해시테이블/771-jewels-and-stones/풀이1({}).py">풀이1({})</a>, 
        <a href="./07-해시테이블/771-jewels-and-stones/풀이2(defaultdict).py">풀이2(defaultdict)</a>, 
        <a href="./07-해시테이블/771-jewels-and-stones/풀이3(set).py">풀이3(set)</a>, 
        <a href="./07-해시테이블/771-jewels-and-stones/풀이4(sum).py">풀이4(sum)</a>
      </td>
      <td>
        <a href="./07-해시테이블/771-jewels-and-stones/NOTES.md">Notes</a>
      </td>
  </tr>
  <tr>
    <td>
        <a href="https://leetcode.com/problems/longest-substring-without-repeating-characters/">중복 문자 없는 가장 긴 부분 문자열</a></td>
      <td>
        <a href="./07-해시테이블/3-longest-substring-without-repeating-characters/풀이1(슬라이싱윈도우).py">풀이1(슬라이싱 윈도우)</a>
      </td>
      <td>
        <a href="./07-해시테이블/3-longest-substring-without-repeating-characters/NOTES.md">Notes</a>
      </td>
  </tr>

  <tr>
    <td>
        <a href="https://leetcode.com/problems/top-k-frequent-elements/">상위 K 빈도 요소</a></td>
      <td>
        <a href="./07-해시테이블/347-top-k-frequent-elements/풀이1(counter, heapq).py">풀이1(counter, heapq)</a>, 
        <a href="./07-해시테이블/347-top-k-frequent-elements/풀이2(zip, counter-most_common).py">풀이2(zip, counter-most_common)</a>
      </td>
      <td>
        <a href="./07-해시테이블/347-top-k-frequent-elements/NOTES.md">Notes</a>
      </td>
  </tr>

  <tr>
    <td rowspan="8"><a href="https://velog.io/@dltjq2323/%EA%B7%B8%EB%9E%98%ED%94%84-%EC%88%9C%ED%9A%8CDFS-BFS"">그래프(BFS, DFS)</a></td>
    <td>
        <a href="https://leetcode.com/problems/number-of-islands/">섬의 개수 </a></td>
      <td>
        <a href="./08-그래프(DFS,BFS)/200-number-of-islands/풀이1-1(DFS-재귀).py">풀이1-1(DFS-재귀)</a>, 
        <a href="./08-그래프(DFS,BFS)/200-number-of-islands/풀이1-2(for문).py">풀이1-2(for문)</a>, 
        <a href="./08-그래프(DFS,BFS)/200-number-of-islands/풀이1-3(함수합침).py">풀이1-3(함수합침)</a>, 
        <a href="./08-그래프(DFS,BFS)/200-number-of-islands/풀이2(Stack).py">풀이2(DFS-stack)</a>
      </td>
      <td>
        <a href="./08-그래프(DFS,BFS)/200-number-of-islands/NOTES.md">Notes</a>
      </td>
  </tr>
  <tr>
    <td>
      <a href="https://leetcode.com/problems/letter-combinations-of-a-phone-number/">전화번호 문자 조합</a></td>
    <td>
      <a href="./08-그래프(DFS,BFS)/17-letter-combinations-of-a-phone-number/풀이1(DFS-stack).py">풀이1(DFS-stack)</a>, 
        <a href="./08-그래프(DFS,BFS)/17-letter-combinations-of-a-phone-number/풀이2-1(DFS-재귀).py">풀이2-1(DFS-재귀)</a>, 
        <a href="./08-그래프(DFS,BFS)/17-letter-combinations-of-a-phone-number/풀이2-2(함수합침).py">풀이2-2(함수합침)</a>
    </td>
    <td>
      <a href="./08-그래프(DFS,BFS)/17-letter-combinations-of-a-phone-number/NOTES.md">Notes</a>
    </td>
  </tr>
  
  <tr>
    <td>
      <a href="https://leetcode.com/problems/permutations/">순열</a></td>
    <td>
      <a href="./08-그래프(DFS,BFS)/46-permutations/풀이1-1(DFS-재귀).py">풀이1(DFS-재귀)</a>, 
      <a href="./08-그래프(DFS,BFS)/46-permutations/풀이1-2(method-func).py">풀이1-2(method-func)</a>, 
      <a href="./08-그래프(DFS,BFS)/46-permutations/풀이2(DFS-stack).py">풀이2(DFS-stack)</a>
    </td>
    <td>
      <a href="./08-그래프(DFS,BFS)/46-permutations/NOTES.md">Notes</a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://leetcode.com/problems/combinations/">조합</a></td>
    <td>
      <a href="./08-그래프(DFS,BFS)/77-combinations/풀이1(DFS-재귀).py">풀이1(DFS-재귀)</a>, 
      <a href="./08-그래프(DFS,BFS)/77-combinations/풀이2(DFS-Stack).py">풀이2(DFS-Stack)</a>
    </td>
    <td>
      <a href="./08-그래프(DFS,BFS)/77-combinations/NOTES.md">Notes</a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://leetcode.com/problems/combination-sum/">조합의 합</a></td>
    <td>
      <a href="./08-그래프(DFS,BFS)/39-combination-sum/풀이1(DFS-재귀).py">풀이1(DFS-재귀)</a>, 
      <a href="./08-그래프(DFS,BFS)/39-combination-sum/풀이2(DFS-Stack).py">풀이2(DFS-Stack)</a>
    </td>
    <td>
      <a href="./08-그래프(DFS,BFS)/39-combination-sum/NOTES.md">Notes</a>
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://leetcode.com/problems/subsets/">부분집합</a></td>
    <td>
      <a href="./08-그래프(DFS,BFS)/78-subsets/풀이1(DFS-재귀).py">풀이1(DFS-재귀)</a>, 
      <a href="./08-그래프(DFS,BFS)/78-subsets/풀이2(DFS-Stack).py">풀이2(DFS-Stack)</a>
    </td>
    <td>
      <a href="./08-그래프(DFS,BFS)/78-subsets/NOTES.md">Notes</a>
    </td>
  </tr>
  
  <tr>
    <td>
      <a href="https://leetcode.com/problems/reconstruct-itinerary/">🤔 일정 재구성</a></td>
    <td>
      <a href="./08-그래프(DFS,BFS)/332-reconstruct-itinerary/풀이1-1(DFS-재귀.py">풀이1-1(DFS-재귀)</a>,  
      <a href="./08-그래프(DFS,BFS)/332-reconstruct-itinerary/풀이1-2(최적화-reverse).py">풀이1-2(최적화-reverse, 슬라이싱)</a>,  
      <a href="./08-그래프(DFS,BFS)/332-reconstruct-itinerary/풀이2(DFS-Stack).py">풀이2(DFS-Stack)</a>
    </td>
    <td>
      <a href="./08-그래프(DFS,BFS)/332-reconstruct-itinerary/NOTES.md">Notes</a>
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://leetcode.com/problems/course-schedule/">🤔 코스 스케줄</a></td>
    <td>
      <a href="./08-그래프(DFS,BFS)/207-course-schedule/풀이1(DFS-재귀)[youtube].py">풀이1(DFS-재귀)[youtube]</a>, 
      <a href="./08-그래프(DFS,BFS)/207-course-schedule/풀이2(DFS-재귀)[leetcode].py">풀이2(DFS-재귀)[leetcode]</a>, 
      <a href="./08-그래프(DFS,BFS)/207-course-schedule/풀이3(DFS-재귀)[파알인].py">풀이3(DFS-재귀)[파알인]</a>
    </td>
    <td>
      <a href="./08-그래프(DFS,BFS)/207-course-schedule/NOTES.md">Notes</a>
    </td>
  </tr>

  <tr>
    <td rowspan="2" href="">최단 경로 문제</td>
    <td>
      <a href="https://leetcode.com/problems/network-delay-time/">네트워크 딜레이 타임</a></td>
    <td>
      <a href="./09-촤단경로[다익스트라]/743-network-delay-time/풀이1(다익스트라[heap]).py">풀이1(다익스트라[heap])</a>, 
      <a href="./09-촤단경로[다익스트라]/743-network-delay-time/풀이2(다익스트라[Queue]).py">풀이2(다익스트라[Queue])</a>
    </td>
    <td>
      <a href=./09-촤단경로[다익스트라]/743-network-delay-time/NOTES.md">Notes</a>
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://leetcode.com/problems/cheapest-flights-within-k-stops/">K 경유지 내 가장 저렴한 항공권</a></td>
    <td>
      <a href="./09-촤단경로[다익스트라]/787-cheapest-flights-within-k-stops/풀이1-1(다익스트라[heaq]).py">풀이1-1(다익스트라[heaq])</a>, 
      <a href="./09-촤단경로[다익스트라]/787-cheapest-flights-within-k-stops/풀이1-2X(time-over).py">풀이1-2X(time-over)</a>, 
      <a href="./09-촤단경로[다익스트라]/787-cheapest-flights-within-k-stops/풀이2(Ballman ford).py">풀이2(Ballman ford)</a>, 
    </td>
    <td>
      <a href="./09-촤단경로[다익스트라]/787-cheapest-flights-within-k-stops/NOTES.md">Notes</a>
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
      <a href="https://leetcode.com/problems/diameter-of-binary-tree/">이진트리의 직경 - 정리 전</a></td>
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

  <tr>
    <td rowspan="7"><a href="">🤔 정렬</a></td>
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
    <td rowspan="3"><a href="">🤔 슬라이딩 윈도우</a></td>
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
      <a href="https://leetcode.com/problems/minimum-window-substring/">🤔 부분 문자열이 포함된 최소 윈도우</a></td>
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
      <a href="https://leetcode.com/problems/longest-repeating-character-replacement">가장 긴 반복 문자 대체</a></td>
    <td>
      <a href="./17-슬라이싱윈도우/424-longest-repeating-character-replacement/풀이1(투포인터,슬라이딩윈도우,counter).py">풀이1(투포인터,슬라이딩윈도우,counter)</a>
    </td>
    <td>
      <a href="./17-슬라이싱윈도우/424-longest-repeating-character-replacement/NOTES.md">Notes</a>
    </td>
  </tr>

   <tr>
    <td rowspan="5"><a href="https://velog.io/@dltjq2323/%EA%B7%B8%EB%A6%AC%EB%94%94Greedy-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98">그리디 알고리즘</a></td>
    <td>
      <a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/">주식을 사고팔기 가장 좋은 시점II</a></td>
    <td>
      <a href="./18-그리디/122-best-time-to-buy-and-sell-stock-ii/풀이1(for).py">풀이1(for)</a>, 
      <a href="./18-그리디/122-best-time-to-buy-and-sell-stock-ii/풀이2(한줄).py">풀이2(한줄)</a>
    </td>
    <td>
      <a href="./18-그리디/122-best-time-to-buy-and-sell-stock-ii/NOTES.md">Notes</a>
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://leetcode.com/problems/queue-reconstruction-by-height/">키에 따른 대기열 재구성</a></td>
    <td>
      <a href="./18-그리디/406-queue-reconstruction-by-height/풀이1(heapq).py">풀이1(heapq)</a>, 
      <a href="./18-그리디/406-queue-reconstruction-by-height/풀이2(lambda).py">풀이2(lambda)</a>
    </td>
    <td>
      <a href="./18-그리디/406-queue-reconstruction-by-height/NOTES.md">Notes</a>
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://leetcode.com/problems/task-scheduler/">🤔 태스크 스케줄러</a></td>
    <td>
      <a href="./18-그리디/621-task-scheduler/풀이1(우선순위큐).py">풀이1(우선순위큐)</a>
    </td>
    <td>
      <a href="./18-그리디/621-task-scheduler/NOTES.md">Notes</a>
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://leetcode.com/problems/gas-station/">주유소</a></td>
    <td>
      <a href="./18-그리디/134-gas-station/풀이1(for).py">풀이1(for)</a>, 
      <a href="./18-그리디/134-gas-station/풀이2(for).py">풀이2(for)</a>
    </td>
    <td>
      <a href="./18-그리디/134-gas-station/NOTES.md">Notes</a>
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://leetcode.com/problems/assign-cookies">🤔 쿠키 부여</a></td>
    <td>
      <a href="./18-그리디/455-assign-cookies/풀이1(그리디).py">풀이1(그리디)</a>, 
      <a href="./18-그리디/455-assign-cookies/풀이2(이진검색).py">풀이2(이진검색)</a>
    </td>
    <td>
      <a href="./18-그리디/455-assign-cookies/NOTES.md">Notes</a>
    </td>
  </tr>

<tr>
    <td rowspan="2"><a href="https://velog.io/@dltjq2323/%EB%B6%84%ED%95%A0-%EC%A0%95%EB%B3%B5%EB%B3%91%ED%95%A9-%EC%A0%95%EB%A0%AC">분할 정복</a></td>
    <td>
      <a href="https://leetcode.com/problems/majority-element">과반수 엘리먼트</a></td>
    <td>
      <a href="./19-분할정복/169-majority-element/풀이1(dict).py">풀이1(dict)</a>, 
      <a href="./19-분할정복/169-majority-element/풀이2(병합정렬-재귀).py">🤔 풀이2(병합정렬-재귀)</a>, 
      <a href="./19-분할정복/169-majority-element/풀이3(sorted).py">풀이3(sorted)</a>
    </td>
    <td>
      <a href="./19-분할정복/169-majority-element/NOTES.md">Notes</a>
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://leetcode.com/problems/different-ways-to-add-parentheses/">🤔 괄호를 삽입하는 여러가지 방법</a></td>
    <td>
      <a href="./19-분할정복/241-different-ways-to-add-parentheses/풀이1(재귀, 메모제이션).py">풀이1(재귀, 메모제이션)</a>, 
      <a href="./19-분할정복/241-different-ways-to-add-parentheses/풀이2(재귀).py">풀이2(재귀)</a>
    </td>
    <td>
      <a href="./19-분할정복/241-different-ways-to-add-parentheses/NOTES.md">Notes</a>
    </td>
  </tr>

  <tr>
    <td rowspan="4"><a href="https://velog.io/@dltjq2323/%EB%8B%A4%EC%9D%B4%EB%82%98%EB%AF%B9-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8DDynamic-programming">다이나믹 프로그래밍</a></td>
    <td>
      <a href="https://leetcode.com/problems/fibonacci-number/">피보나치 수</a></td>
    <td>
      <a href="./20-다이나믹프로그래밍/509-fibonacci-number/풀이1(브루트포스).py">풀이1(브루트포스)</a>, 
      <a href="./20-다이나믹프로그래밍/509-fibonacci-number/풀이2(메모제이션).py">풀이2(메모제이션)</a>, 
      <a href="./20-다이나믹프로그래밍/509-fibonacci-number/풀이3(반복, 상향식).py">풀이3(반복, 상향식)</a>, 
      <a href="./20-다이나믹프로그래밍/509-fibonacci-number/풀이4(두변수).py">풀이4(두변수)</a>, 
      <a href="./20-다이나믹프로그래밍/509-fibonacci-number/풀이5(넘파이).py">풀이5(넘파이)</a>
    </td>
    <td>
      <a href="./20-다이나믹프로그래밍/509-fibonacci-number/NOTES.md">Notes</a>
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://leetcode.com/problems/maximum-subarray/">최대 서브 배열</a></td>
    <td>
      <a href="./20-다이나믹프로그래밍/53-maximum-subarray/풀이1(메모제이션).py">풀이1(메모제이션)</a>, 
      <a href="./20-다이나믹프로그래밍/53-maximum-subarray/풀이2(카데인 알고리즘).py">풀이2(카데인 알고리즘)</a>
    </td>
    <td>
      <a href="./20-다이나믹프로그래밍/53-maximum-subarray/NOTES.md">Notes</a>
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://leetcode.com/problems/climbing-stairs/">계단 오르기</a></td>
    <td>
      <a href="./20-다이나믹프로그래밍/70-climbing-stairs/풀이1(브루트포스).py">풀이1(브루트포스)</a>, 
      <a href="./20-다이나믹프로그래밍/70-climbing-stairs/풀이2(메모제이션).py">풀이2(메모제이션)</a>
    </td>
    <td>
      <a href="./20-다이나믹프로그래밍/70-climbing-stairs/NOTES.md">Notes</a>
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://leetcode.com/problems/house-robber">🤔 집 도둑</a></td>
    <td>
      <a href="./20-다이나믹프로그래밍/198-house-robber/풀이1(브루트포스).py">풀이1(브루트포스)</a>, 
      <a href="./20-다이나믹프로그래밍/198-house-robber/풀이2(타블레이션).py">풀이(타블레이션[상향식])</a>, 
      <a href="./20-다이나믹프로그래밍/198-house-robber/풀이3(dp).py">풀이3(dp)</a>
    </td>
    <td>
      <a href="./20-다이나믹프로그래밍/198-house-robber/NOTES.md">Notes</a>
    </td>
  </tr>

<tr>
    <td rowspan="7"><a href="">카카오 공채(2017)</a></td>
    <td>
      <a href="https://school.programmers.co.kr/learn/courses/30/lessons/17681">비밀지도</a>
    </td>
    <td>
      <a href="./21-카카오(17)/1.비밀지도/풀이1.py">풀이1</a>
    </td>
    <td>
      <a href="">Notes</a>
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://school.programmers.co.kr/learn/courses/30/lessons/17682">다트 게임</a></td>
    <td>
      <a href="./21-카카오(17)/2.다트게임/풀이1.py">풀이1</a>
    </td>
    <td>
      <a href="">Notes</a>
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://school.programmers.co.kr/learn/courses/30/lessons/17680">캐시</a></td>
    <td>
      <a href="./21-카카오(17)/3.캐시/풀이1.py">풀이1</a>
    </td>
    <td>
      <a href="">Notes</a>
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://programmers.co.kr/learn/courses/30/lessons/17678">셔틀버스</a></td>
    <td>
      <a href="./21-카카오(17)/4.셔틀버스/풀이1.py">풀이1</a>
    </td>
    <td>
      <a href="">Notes</a>
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://programmers.co.kr/learn/courses/30/lessons/17677">뉴스 클러스터링</a></td>
    <td>
      <a href="./21-카카오(17)/5.뉴스_클러스터링/풀이1.py">풀이1</a>
    </td>
    <td>
      <a href="">Notes</a>
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://programmers.co.kr/learn/courses/30/lessons/17679">프렌즈4블록</a></td>
    <td>
      <a href="./21-카카오(17)/6.프렌즈4블록/풀이1.py">풀이1</a>
    </td>
    <td>
      <a href="">Notes</a>
    </td>
  </tr>

  <tr>
    <td>
      <a href="https://programmers.co.kr/learn/courses/30/lessons/17676">추석 트래픽</a></td>
    <td>
      <a href="./21-카카오(17)/7.추석_트래픽/풀이1.py">풀이1</a>
    </td>
    <td>
      <a href="">Notes</a>
    </td>
  </tr>

</table>

<br/><br/>

## 정리해야할 내용

### velog 정리: `최단경로(다익스트라, 벨만포드)`, `이진탐색트리, 트리 순회`, `정렬`, `이진검색`, `슬라이딩 윈도우`, 그리디(추가정리 필요)

<br/>

### 이해 안되는 문제: 다시 복습 시, 작성하기

### Notes: 이것도 복습하면서 정리

### `비트 조작`... 이놈은 아직 이해 불가다... 공부하면서 이해가 될때 추가 정리하자.

<br/>

이해한 내용도 따로 정리하지 않으면 reset된다.
쉬워서 그냥 넘어간 문제도 나중을 위해 Notes에 정리하자.

<br/>

추가 정리)<br/>
다 정리 후 `javascript` 풀이도 정리
