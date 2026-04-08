import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
graph = [[-1] * M for _ in range(N)]

for i in range(N):
    for j, c in enumerate(list(map(str, input()))):
        if c == "c": graph[i][j] = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] != 0:
            continue

        while j+1 < M and graph[i][j+1] != 0:
            graph[i][j+1] = graph[i][j] + 1
            j += 1
        
for i in range(N):
    for j in range(M):
        print(graph[i][j], end=' ')
    print()