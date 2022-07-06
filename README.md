# Algorithm-baekjoon
This is a auto push repository for Baekjoon Online Judge created with [BaekjoonHub](https://github.com/BaekjoonHub/BaekjoonHub).


### ● sort   vs   sorted
sort: 원본값 수정
    -> 리스트명.sort()

sorted: 원본값 복사한 새로운 리스트 수정
    ->리스트명2 = sorted(리스트명)


### ● lambda
    -> lambda 매개변수 : 표현식

#### ex)

ex1 = [[1, 2], [3, 4], [5, 6], [3, 6], [5,9]]

ex1.sort(key = lambda x : x[0], -x[1]) 
    -> [[1, 2], [3, 6], [3, 4], [5, 9], [5, 6]]

>x[0]: 첫번째 요소, 오름차순 정렬
>-x[1]: 두번쩨 요소, 내림차순 정렬
>  -> (-1)x[n]: n-1 요소, (내림)오름차순 정렬

![](./lambda.png)

Reference) https://wikidocs.net/64


### ● range()
 -> 반복이 가능한 숫자형 이터러블 객체를 반환해주는 함수이다.

1. 인수가 한 개일 때 - range(MAX)
    -> 0 <= x < MAX
         ex) .range(5) -> 0, 1, 2, 3, 4


2. 인수가 두 개일 때 - range(MIN, MAX)
   -> MIN <= x < MAX
        ex) .range(1, 5) -> 1, 2, 3, 4

3. 인수가 세 개일 때 - range(Min, Max, GAP) 
    -> Min <= x(gap=GAP) < Max
        ex) .range(0, 10, 2) -> 0, 2, 4, 6, 8