import sys
n = int(sys.stdin.readline())
ropes = []
for _ in range(n):
    ropes.append(int(sys.stdin.readline()))
ropes.sort(reverse=True)

result=[]
for i in range(n):
    result.append((i+1)*ropes[i])
print(max(result))
