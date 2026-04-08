import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

ret = 1
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def dfs(y, x):
    visited[y][x] = True

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= N or nx < 0 or nx >= N: continue
        if visited[ny][nx]: continue
        dfs(ny, nx)

    return 1

if __name__ == "__main__":
    for h in range(1, 101):
        visited = [[False] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if graph[i][j] <= h:
                    visited[i][j] = True

        cnt = 0
        for i in range(N):
            for j in range(N):
                if visited[i][j]: continue
                cnt += dfs(i, j)

        ret = max(ret, cnt)

print(ret)