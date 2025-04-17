import sys
from collections import deque
input = sys.stdin.readline

# Input
M, N = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(N)]

# Variables
q = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# Solution
def check(tomatoes):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if tomatoes[i][j] == 0:
                return -1
            else:
                cnt = max(cnt, tomatoes[i][j])
    
    return cnt - 1

def bfs(tomatoes):
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not tomatoes[nx][ny]:
                q.append((nx, ny))
                tomatoes[nx][ny] = tomatoes[x][y] + 1

    return check(tomatoes)

# Main
for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 1:
            q.append((i, j))

# Output
print(bfs(tomatoes))