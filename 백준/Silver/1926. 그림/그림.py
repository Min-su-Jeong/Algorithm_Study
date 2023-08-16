import sys
from collections import deque

def bfs(x, y):
    area = 1
    graph[x][y] = 0
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
                area += 1
    return area

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

cnt, max_area = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cnt += 1
            max_area = max(bfs(i, j), max_area)

print(cnt)
print(max_area)