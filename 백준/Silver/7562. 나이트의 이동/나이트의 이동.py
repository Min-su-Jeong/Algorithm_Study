import sys
from collections import deque
input = sys.stdin.readline

# Input
N = int(input())

# Variables
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

# Solution
def bfs(start, end, board, l):
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = True

    while q:
        x, y = q.popleft()

        if x == end[0] and y == end[1]:
            return 0
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx < 0 or nx >= l) or (ny < 0 or ny >= l):
                continue
            
            if nx == end[0] and ny == end[1]:
                visited[nx][ny] = True
                return board[x][y] + 1
            
            if not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
                board[nx][ny] = board[x][y] + 1

# Main
for _ in range(N):
    l = int(input())
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))

    board = [[0 for _ in range(l)] for _ in range(l)]
    visited = [[False for _ in range(l)] for _ in range(l)]
    
    # Output
    res = bfs(start, end, board, l)
    print(res)