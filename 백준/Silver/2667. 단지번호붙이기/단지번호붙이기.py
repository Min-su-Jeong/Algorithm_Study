import sys
from collections import deque
input = sys.stdin.readline

# bfs를 통한 해결
def bfs(x, y, graph):
    # 각 단지 내 집의 수를 위한 변수
    cnt = 1
    
    # 탐색중인 좌표를 0으로 변환 => 다시 방문하지 않도록 하기 위함
    graph[x][y] = 0 
    
    # 상, 하, 좌, 우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    # deque 사용
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 좌표 값이 범위를 벗어나는 경우
            if (nx < 0 or nx >= n) or (ny < 0 or ny >= n):
                continue
            
            # 좌표 값이 1(집이 있는 곳)인 경우
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0 # 탐색한 좌표를 0으로 변환
                q.append((nx, ny))
                cnt += 1
    
    return cnt
                
# 입력 받기(input)
n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
            
# bfs 수행(단지를 구별하며 각 단지별 집의 수를 리스트에 저장)
res = [bfs(i, j, graph) for i in range(n) for j in range(n) if graph[i][j] == 1]
res.sort()

# 결과 출력
print(len(res), *res, sep='\n')