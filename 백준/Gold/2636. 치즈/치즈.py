import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

def melt():
    visited = [[False] * M for _ in range(N)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    melted = []

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= M: continue
            if visited[ny][nx]: continue
            visited[ny][nx] = True
            if graph[ny][nx] == 1:
                melted.append((ny, nx))
            else:
                q.append((ny, nx))
    
    for y, x in melted:
        graph[y][x] = 0

    return len(melted)

if __name__ == "__main__":
    ret1, ret2 = 0, 0

    while True:
        melted = melt()
        if melted == 0:
            break
        
        ret1 += 1
        ret2 = melted
    
    print(ret1)
    print(ret2)