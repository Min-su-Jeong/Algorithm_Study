import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
graph = [input().rstrip() for _ in range(N)]

walls = 0
virusOne = 0
virusAll = 0
vaccines = 0
s = 0
e = 0

for i in graph:
    for j in i:
        if j == '#': walls += 1
        if j in 'UDLR': virusOne += 1
        if j == 'A': virusAll += 1
        if j == 'V': vaccines += 1
        if j == 'S': s += 1
        if j == 'E': e += 1

if s != 1 or e != 1:
    print(-1)
else:
    if walls <= 1 and virusOne <= 1 and virusAll == 0 and vaccines == 0:
        print(1)
    elif virusAll == 0 and vaccines == 0:
        print(2)
    elif virusAll == 0:
        print(3)
    else:
        print(4)