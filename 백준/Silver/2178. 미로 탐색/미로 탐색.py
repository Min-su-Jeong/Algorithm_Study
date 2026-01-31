import sys; input = lambda: sys.stdin.readline().rstrip()
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

def bfs(y, x):
    q = deque()
    q.append((y, x))

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if graph[ny][nx] != 1:
                continue

            graph[ny][nx] = graph[y][x] + 1
            q.append((ny, nx))

bfs(0, 0)

print(graph[N-1][M-1])