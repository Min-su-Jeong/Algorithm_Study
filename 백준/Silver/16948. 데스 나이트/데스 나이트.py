import sys
from collections import deque
input = sys.stdin.readline

# Input
N = int(input())
r1, c1, r2, c2 = map(int, input().split())

# Variables
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]
visited = [[0 for _ in range(N)] for _ in range(N)]

# Solution
def bfs(x, y):
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
            
                if nx == r2 and ny == c2:
                    return visited[nx][ny]
                
                q.append((nx, ny))
    
    return -1

# Output
print(bfs(r1, c1))