"""
1.전략
- DFS 
- 5개의 테트로미노 중 T자형 테트로미노를 어떻게 구현할지에 대해 고민
- dfs 구현 + 가지치기(로직 구현)
- 나머지 블럭이 모두 최댓값이어도 현재 결과값보다 작으면 return

2.시간복잡도
- 시간 제한: 2초
- O(N*M) = 500 * 500 * 4 = 1,000,000
"""
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range (N)]
visited = [[0] * M for _ in range (N)]

max_pos = max(map(max, graph))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(depth:int, total:int, arr:list):
    global ans
    
    # 가지치기
    if ans >= total + (4-depth) * max_pos:
        return
    
    # 종료 조건
    if depth == 4:
        ans = max(total, ans)
        return
    
    # 순회 시작
    for cx, cy in arr:
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0<=nx<N and 0<=ny<M and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                dfs(depth+1, total+graph[nx][ny], arr+[(nx, ny)])
                visited[nx][ny] = 0
    
ans = 0
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(1, graph[i][j], [(i, j)])
        
print(ans)