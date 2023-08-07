from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 0
    size = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny]:
                graph[nx][ny] = 0
                q.append((nx, ny))
                size += 1
                
    return size

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0 , -1, 1]

cnt, max_size = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            cnt += 1
            max_size = max(bfs(i, j), max_size)
        
print(cnt)
print(max_size)