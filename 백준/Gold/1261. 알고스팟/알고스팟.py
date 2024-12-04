"""
1.전략
- BFS(Breath-First Search)
- 상하좌우 움직일 수 있는 BFS 구성 + 방문 여부 확인 + 벽을 부숴야 하는 경우 계산
- 벽을 부숴야 하는 경우: 이전 값+1, 리스트 뒤에 이동한 좌표 추가
- 벽이 없는 경우: 이전 값, 리스트 앞에 이동한 좌표 추가를 통해 우선적으로 움직일 수 있도록 함

2.시간 복잡도
- 시간 제한: 1초
- O(M*N) = 100 * 100 = 10,000
"""
import sys
from collections import deque
input = sys.stdin.readline

# Input
M, N = map(int, input().split())
miro = [list(map(int, input().rstrip())) for _ in range(N)]

# Variables
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[-1 for _ in range(M)] for _ in range(N)]

# Solution
def bfs(x, y):
    global visited

    q = deque()
    q.append((x, y))
    visited[0][0] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if visited[nx][ny] == -1:
                if miro[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y]
                    q.appendleft((nx, ny))

                else:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

# Main
bfs(0, 0)

# Output
print(visited[N-1][M-1])