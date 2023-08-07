import sys
from collections import deque

def bfs(x, y, val):
    safe[x][y] = 1
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                # 안전한 영역만 1로 변경
                if not safe[nx][ny] and graph[nx][ny] > val:
                    safe[nx][ny] = 1
                    q.append((nx, ny))
                    
input = sys.stdin.readline
n = int(input())
max_num = 0 # 최대 높이
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] > max_num:
            max_num = graph[i][j]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]



result = 0
for val in range(max_num):
    cnt = 0
    safe = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 안전한 영역의 개수 찾기
            if not safe[i][j] and graph[i][j] > val:
                cnt += 1
                bfs(i, j, val)
    result = max(cnt, result)
    
print(result)