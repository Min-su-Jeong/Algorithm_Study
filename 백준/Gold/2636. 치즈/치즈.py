import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def melt():
    melted = []
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True

    q = deque()
    q.append((0, 0))
    
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= M or visited[ny][nx]: continue
            visited[ny][nx] = True
            if graph[ny][nx] == 1:
                melted.append((ny, nx))
            else:
                q.append((ny, nx))

    for y, x in melted:
        graph[y][x] = 0

    return len(melted)

if __name__ == "__main__":
    time, area = 0, 0

    while True:
        melted = melt()
        if melted == 0:
            break
        
        time += 1
        area = melted

    print(time)
    print(area)