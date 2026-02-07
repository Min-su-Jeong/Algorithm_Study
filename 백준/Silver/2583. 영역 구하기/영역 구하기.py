import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 6)

M, N, K =map(int, input().split())
graph = [[0] * N for _ in range(M)]
visited = [[0] * N for _ in range(M)]

ret = []
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

def dfs(y, x):
    cnt = 1
    graph[y][x] = 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or nx < 0 or ny >= M or nx >= N: continue
        if graph[ny][nx] == 1: continue
        graph[ny][nx] = 1
        cnt += dfs(ny, nx)
    
    return cnt

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            ret.append(dfs(i, j))

ret.sort()

print(len(ret))
print(*ret)