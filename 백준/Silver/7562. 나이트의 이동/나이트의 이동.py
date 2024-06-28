"""
1.전략
- BFS
- BFS 알고리즘을 사용하여 8방향으로 탐색

2.시간복잡도
- O(N^2) = 300 * 300 = 90,000 (Worst case)
"""
import sys; input = sys.stdin.readline
from collections import deque

def bfs():
        q = deque()

        q.append(now)
        visited[now[0]][now[1]]

        while q:
            x, y = q.popleft()

            if x == dest[0] and y == dest[1]:
                return 0

            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue

                if nx == dest[0] and ny == dest[1]:
                    visited[nx][ny] = True
                    return graph[x][y]+1

                if visited[nx][ny] == False:
                    q.append([nx,ny])
                    visited[nx][ny] = True
                    graph[nx][ny] = graph[x][y] + 1

# 입력 받기             
t = int(input()) 

# 필요한 변수 생성 및 초기화
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

for _ in range(t):
    # 입력 받기
    n = int(input())
    now = list(map(int, input().split()))
    dest = list(map(int, input().split()))   
    
    # 필요한 변수 생성 및 초기화 
    graph = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    
    # 함수 실행 및 결과 출력
    print(bfs())