import sys
input = lambda: sys.stdin.readline().strip()

N, M = map(int, input().split())

mpI = {}
mpS = {}
for i in range(1, N+1):
    s = input()
    mpI[i] = s
    mpS[s] = i

for _ in range(M):
    s = input()

    if s.isdigit():
        print(mpI[int(s)])
    else:
        print(mpS[s])