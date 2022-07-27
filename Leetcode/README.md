# 👉 파이썬 알고리즘 인터뷰 정리본


<img src="../이미지/파알인-표지.jpg" width=60% />

<br>

구매 링크)
- [교보문고](http://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode=9791189909178&orderClick=LEa&Kc=)
- [알라딘](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=245495826)


<br><br>

|chapter|주제|내용|
|:-----:|:--:|:--:|

- [빅오, 시간복잡도](https://velog.io/@dltjq2323/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%98-%ED%9A%A8%EC%9C%A8%EC%84%B1%EC%8B%9C%EA%B0%84%EB%B3%B5%EC%9E%A1%EB%8F%84-%EA%B3%B5%EA%B0%84%EB%B3%B5%EC%9E%A1%EB%8F%84-%EB%B9%85%EC%98%A4)

<br>

# 자료구조
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
    <td><a href="https://leetcode.com/problems/valid-palindrome/submissions/">유효한 팰린드롬</a></td>
    <td><a href="https://github.com/gyungsubLee/Algorithm-baekjoon/blob/main/Leetcode/125-valid-palindrome/%ED%92%80%EC%9D%B41-Array.py">풀이1(Array)</a>, <a href="https://github.com/gyungsubLee/Algorithm-baekjoon/blob/main/Leetcode/125-valid-palindrome/%ED%92%80%EC%9D%B42-Deque.py">풀이2(Deque)</a>, <a href="https://github.com/gyungsubLee/Algorithm-baekjoon/blob/main/Leetcode/125-valid-palindrome/%ED%92%80%EC%9D%B43-%EC%8A%AC%EB%9D%BC%EC%9D%B4%EC%8B%B1.py">풀이3(슬라이싱)</a></td>
    <td><a href="https://github.com/gyungsubLee/Algorithm-baekjoon/blob/main/Leetcode/125-valid-palindrome/NOTES.md">Notes</a></td>
  </tr>

  <tr>
    <td><a href="https://leetcode.com/problems/reverse-string/submissions/">문자열 뒤집기</a></td>
    <td><a href="https://github.com/gyungsubLee/Algorithm-baekjoon/blob/main/Leetcode/344-reverse-string/%ED%92%80%EC%9D%B41-%ED%88%AC%ED%8F%AC%EC%9D%B8%ED%84%B0.py">풀이1(투포인터)</a>, <a href="https://github.com/gyungsubLee/Algorithm-baekjoon/blob/main/Leetcode/344-reverse-string/%ED%92%80%EC%9D%B42-%EB%82%B4%EC%9E%A5%ED%95%A8%EC%88%98.py">풀이2(내장함수)</a>, <a href="https://github.com/gyungsubLee/Algorithm-baekjoon/blob/main/Leetcode/344-reverse-string/%ED%92%80%EC%9D%B43-%EC%8A%AC%EB%9D%BC%EC%9D%B4%EC%8B%B1.py">풀이3(슬라이싱)</a></td>
    <td><a href="https://github.com/gyungsubLee/Algorithm-baekjoon/blob/main/Leetcode/344-reverse-string/NOTES.md">Notes</a></td>
  </tr>

  <tr>
    <td><a href="https://leetcode.com/problems/reorder-data-in-log-files/">로그파일 재정렬</a></td>
    <td><a href="https://github.com/gyungsubLee/Algorithm-baekjoon/blob/main/Leetcode/937-reorder-data-in-log-files/%ED%92%80%EC%9D%B41-%EB%9E%8C%EB%8B%A4.py">풀이1(lambda)</a>
    <td><a href="https://github.com/gyungsubLee/Algorithm-baekjoon/blob/main/Leetcode/937-reorder-data-in-log-files/NOTES.md">Notes</a>, <a href="https://github.com/gyungsubLee/Algorithm-baekjoon/blob/main/Leetcode/125-valid-palindrome/%EB%9E%8C%EB%8B%A4%ED%91%9C%ED%98%84%EC%8B%9D.md">lambda</a></td>
  </tr>


   <tr>
    <td><a href="https://leetcode.com/problems/most-common-word/">가장 흔한 단어</a></td>
    <td><a href="https://github.com/gyungsubLee/Algorithm-baekjoon/blob/main/Leetcode/819-most-common-word/%ED%92%80%EC%9D%B41(%EB%A6%AC%EC%8A%A4%ED%8A%B8%EC%BB%B4%ED%94%84%EB%A6%AC%ED%97%A8%EC%85%98%2Cmax).py">풀이1(리스트컴프리헨션, max)</a>, <a href="https://github.com/gyungsubLee/Algorithm-baekjoon/blob/main/Leetcode/819-most-common-word/%ED%92%80%EC%9D%B42(%EB%A6%AC%EC%8A%A4%ED%8A%B8%EC%BB%B4%ED%94%84%EB%A6%AC%ED%97%A8%EC%85%98%2CCounter).py">풀이2(Couter)</a></td>
    <td><a href="https://github.com/gyungsubLee/Algorithm-baekjoon/blob/main/Leetcode/819-most-common-word/NOTES.md">Notes</a></td>
  </tr>


   <tr>
    <td><a href="https://leetcode.com/problems/group-anagrams/submissions/">그룹 애너그램</a></td>
    <td><a href="https://github.com/gyungsubLee/Algorithm-baekjoon/blob/main/Leetcode/49-group-anagrams/%ED%92%80%EC%9D%B41(dict-%EC%A0%95%EB%A0%AC).py">풀이1-정렬</a></td>
    <td><a href="https://github.com/gyungsubLee/Algorithm-baekjoon/blob/main/Leetcode/49-group-anagrams/NOTES.md">Notes</a>, <a href="https://github.com/gyungsubLee/Algorithm-baekjoon/blob/main/Leetcode/49-group-anagrams/%EC%A0%95%EB%A0%AC(sorted%2Csort).md">정렬(sort, sorted)</a></td>
  </tr>
  <tr>
      <td><a href="">가장 긴 팰린드롬 부분 문자열</a></td>
      <td><a href="">풀이1</a>, <a href="">풀이2</a>, <a href="">풀이3</a></td>
      <td><a href="">Notes</a></td>
  </tr>


  <tr>
      <td><a href=""></a></td>
      <td><a href="">풀이1</a>, <a href="">풀이2</a>, <a href="">풀이3</a></td>
      <td><a href="">Notes</a></td>
  </tr>

  <tr>
      <td><a href=""></a></td>
      <td><a href="">풀이1</a>, <a href="">풀이2</a>, <a href="">풀이3</a></td>
      <td><a href="">Notes</a></td>
  </tr>
</table>

