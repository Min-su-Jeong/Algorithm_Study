"""
1.전략
- DFS 
- 5개의 테트로미노 중 T자 테트로미노를 dfs로 어떻게 구현할지에 대해 고민
- 기본 2개의 블럭을 연결한 상태로 5개의 테트로미노를 만들 수 있도록 함
- DFS 순회를 통해 res에 최댓값 갱신

2.시간복잡도
O(N*M*4) = 497 * 497 * 4 = 988,036
=> 2초 내 가능
"""
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def dfs(x:int, y:int, depth:int, total:int):
    global res
    
    # 예외처리
    if res >= total + max_pos*(4-depth):
        return
    
    # 테트로미노가 완성된 경우
    if depth == 4:
        res = max(res,total)
        return
    # 테트로미노가 미완성인 경우
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
                # 테트로미노 블럭이 2개가 연결된 경우
                # 기본 2개가 붙어있고 그 상태에서 모양을 만들어가는 방식
                if depth == 2:
                    visited[nx][ny] = True
                    # 두번째 블록에서 한번 더 돌아야 하기 때문에 x,y 좌표 필요
                    dfs(x, y, depth+1, total+graph[nx][ny]) 
                    visited[nx][ny] = False
                    
                visited[nx][ny] = True
                dfs(nx, ny, depth+1, total+graph[nx][ny])
                visited[nx][ny] = False

                
res = 0
max_pos = max(map(max,graph)) 
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 1, graph[i][j])
        visited[i][j] = 0
        
print(res)