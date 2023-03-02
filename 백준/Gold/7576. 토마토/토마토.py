import sys
from collections import deque

def bfs():   
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 좌표 값 벗어나는 경우 제외 & 인접한 위치가 익지 않아야 함
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1 # 주변 토마토 익히기 & 횟수 세기
                q.append((nx, ny))

input = sys.stdin.readline
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
day = 0

# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0] 

# 익은 토마토의 위치 좌표 추가
q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j))

# bfs 수행
bfs()

# 답 찾아내기
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    day = max(day, max(i))
print(day -1)