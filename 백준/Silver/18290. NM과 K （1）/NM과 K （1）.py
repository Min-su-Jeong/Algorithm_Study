"""
1.전략
- 백트래킹(Back Tracking)
- DFS + 가지치기
- N X M 크기만큼 2차원 반복문 생성
- 현재/인접 위치 방문 여부 확인 -> 모두 해당되지 않을 때 현재 위치 방문 표시

2.시간 복잡도
- 시간 제한: 2초
- O((N*M)^K) = (10 * 10) ^ 4 = 100,000,000
"""
import sys
input = sys.stdin.readline

# Input
N, M, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# Variables
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visited = [[False for _ in range(M)] for _ in range(N)]
res = -sys.maxsize

# Solution
def backTracking(cx, cy, cost, depth):
    global res

    # 가지치기
    if depth == K:
        res = max(res, cost)
        return

    # 조건
    for x in range(cx, N):
        # 같은 행 중복 선택 방지
        for y in range(cy if x == cx else 0, M):
            # 현재 위치 방문여부 확인
            if visited[x][y]:
                continue
            
            # 인접 위치 방문여부 확인
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and visited[nx][ny]:
                    break
            
            # 인접 위치 방문하지 않은 경우 방문 표시 및 순회
            else:
                visited[x][y] = True
                backTracking(x, y, cost+graph[x][y], depth+1)
                visited[x][y] = False

# Main
backTracking(0, 0, 0, 0)

# Output
print(res)