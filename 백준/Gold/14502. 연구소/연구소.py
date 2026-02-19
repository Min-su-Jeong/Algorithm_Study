import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

def bfs(y, x, visited):
    q = deque()
    q.append((y, x))

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= M: continue
            if visited[ny][nx] or graph[ny][nx] == 1: continue
            q.append((ny, nx))
            visited[ny][nx] = True

def solve():
    visited = [[False] * M for _ in range(N)]
    for vx, vy in virus:
        visited[vx][vy] = True
        bfs(vx, vy, visited)

    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0 and not visited[i][j]:
                cnt += 1

    return cnt

if __name__ == "__main__":        
    ret = 0
    wall, virus = [], []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                wall.append((i, j))
            if graph[i][j] == 2:
                virus.append((i, j))


    for i in range(len(wall)):
        for j in range(i):
            for k in range(j):
                graph[wall[i][0]][wall[i][1]] = 1
                graph[wall[j][0]][wall[j][1]] = 1
                graph[wall[k][0]][wall[k][1]] = 1
                ret = max(ret, solve())
                graph[wall[i][0]][wall[i][1]] = 0
                graph[wall[j][0]][wall[j][1]] = 0
                graph[wall[k][0]][wall[k][1]] = 0

    print(ret)