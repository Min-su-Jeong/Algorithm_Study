
import sys; input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**7)

T = int(input())

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

def dfs(y, x):
    visited[y][x] = True
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or nx < 0 or ny >= N or nx >= M: continue
        if graph[ny][nx] == 0 or visited[ny][nx]: continue

        dfs(ny, nx)
            
while T:
    M, N, K = map(int, input().split())

    ret = 0
    visited = [[0] * M for _ in range(N)]
    graph = [[0] * M for _ in range(N)]

    for i in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0 or visited[i][j]:
                continue
            
            dfs(i, j)
            ret += 1

    print(ret)
    
    T -= 1