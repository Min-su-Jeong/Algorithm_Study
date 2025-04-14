import sys
from collections import deque
input = sys.stdin.readline

# Input
N = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(N)]

# Variables
res = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# Solution
def bfs(x, y, graph):
    q = deque()
    q.append((x, y))

    cnt = 1
    graph[x][y] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny]:
                graph[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1

    return cnt

# Main
res = [bfs(x, y, graph) for x in range(N) for y in range(N) if graph[x][y] == 1]
res.sort()

# Output
print(len(res))
print(*res, sep='\n')