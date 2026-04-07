import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**7)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

T = int(input())

def dfs(y, x):
    graph[y][x] = 0

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= N or nx < 0 or nx >= M: 
            continue
        if graph[ny][nx] == 1:
            dfs(ny, nx)

    return 1

while T:
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    ret = 0

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                continue
            ret += dfs(i, j)

    print(ret)

    T -= 1