from sys import stdin

#입력
T = int(stdin.readline())

#개수 카운트 저장할 배열, 사용할 데이터 배열
count = [0]*3
abc = [300,60,10]

#1의 자리가 0이 아니면 -1을 출력
if(T%10 != 0) :
    print(-1)
#1의 자리가 0이면 T를 큰 값부터 나누어 몫은 카운트에 저장하고 나머지는 T에 다시 저장
else :
    for i in range(3) :
        count[i] = T//abc[i]
        T -= count[i]*abc[i]

    #출력
    print(count[0], count[1], count[2])