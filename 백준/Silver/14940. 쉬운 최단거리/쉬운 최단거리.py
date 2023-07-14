import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
visited = [[-1] * m for _ in range(n)]

# bsf 함수
def bfs(i, j):
    q = deque()
    q.append((i, j))
    
    visited[i][j] = 0
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if maps[nx][ny] == 0:
                    visited[nx][ny] = 0
                else:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

# bfs 탐색(시작지점 찾으면 탐색 시작)
for i in range(n):
    for j in range(m):
        if maps[i][j] == 2 and visited[i][j] == -1:
            bfs(i,j)

# 결과 출력을 위한 for문
for i in range(n):
    for j in range(m):
        if maps[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()