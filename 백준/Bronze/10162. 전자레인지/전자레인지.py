from sys import stdin
T = int(stdin.readline())
count = [0]*3
abc = [300,60,10]
if(T%10 != 0) :
    print(-1)
else :
    for i in range(3) :
        count[i] = T//abc[i]
        T -= count[i]*abc[i]
    print(count[0], count[1], count[2])
