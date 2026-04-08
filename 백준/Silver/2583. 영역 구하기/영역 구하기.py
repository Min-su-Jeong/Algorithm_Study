import sys
sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())
graph = [[0 for _ in range(M)] for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
ret = []

def dfs(y, x):
    cnt = 1
    graph[y][x] = 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= N or nx < 0 or nx >= M: continue
        if graph[ny][nx] == 1: continue
        cnt += dfs(ny, nx)

    return cnt

if __name__ == "__main__":
    for _ in range(K):
        x1, y1, x2, y2 = map(int, input().split())
        for i in range(y1, y2):
            for j in range(x1, x2):
                graph[i][j] = 1

    for i in range(N):
        for j in range(M):
            if graph[i][j]: continue

            ret.append(dfs(i, j))

ret.sort()

print(len(ret))
print(*ret)