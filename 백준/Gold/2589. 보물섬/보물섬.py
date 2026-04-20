import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

ret = 0
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N, M = map(int, input().split())
graph = [list(map(str, input())) for _ in range(N)]

def bfs(y, x):
    global ret

    visited = [[0] * M for _ in range(N)]
    visited[y][x] = 1
    q = deque()
    q.append((y, x))

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= M: continue
            if visited[ny][nx] or graph[ny][nx] == 'W': continue
            visited[ny][nx] = visited[y][x] + 1
            ret = max(ret, visited[y][x])
            q.append((ny, nx))
    
if __name__ == "__main__":
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 'L':
                bfs(i, j)

    print(ret)