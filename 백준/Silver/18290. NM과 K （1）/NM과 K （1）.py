"""
1.전략
- DFS
- 재귀함수를 통해 K개를 선택 가능한 조합 체크
- K개가 선택된 경우, 이전 조합에서의 최댓값과 비교하여 res에 갱신

2.시간복잡도
- O((N*M)^K) = (10*10)^4 = 100,000,000
  => 2초 이내 가능
"""
def dfs(cx, cy, selectNum, sumNum):
    global res
    
    # 선택된 개수가 K개가 되면 종료
    if selectNum == K:
        res = max(res, sumNum)
        return

    # NxM 배열 순회
    for x in range(cx, N):
        cy = 0 if x != cx else cy
        for y in range(cy, M):
            visitFlag = False
            
            # [x, y] 좌표에 해당하는 수를 방문했는지 여부 확인
            if visited[x][y]:
                continue
                
            # (x, y) 좌표 기준에서 상,하,좌,우 방문 여부 확인
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < N and 0 <= ny < M and visited[nx][ny]:
                    visitFlag = True # 하나라도 있으면 True
                        
            # 방문한 적이 없는 경우, 순회 시작
            if not visitFlag:
                visited[x][y] = True
                dfs(x, y, selectNum+1, sumNum+graph[x][y])
                visited[x][y] = False

                
res = -40000 # 입력받는 최솟 값 : -10000 => K는 최대 4이므로 -10000*4=-40000=최솟 값          
N, M, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dfs(0, 0, 0, 0)

print(res)