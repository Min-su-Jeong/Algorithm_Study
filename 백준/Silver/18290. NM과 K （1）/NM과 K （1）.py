"""
1.전략
- DFS
- 재귀함수를 통해 K개를 선택 가능한 조합 체크
- K개가 선택된 경우, 이전 조합에서의 최댓값과 비교하여 res에 갱신

2.시간복잡도
- O((N*M)^K) = (10*10)^4 = 100,000,000
  => 2초 이내 가능
"""
def dfs(selectNum, sumNum):
    global res
    
    # 선택된 개수가 K개가 되면 종료
    if selectNum == K:
        res = max(res, sumNum)
        return

    # NxM 배열 순회
    for i in range(N):
        for j in range(M):
            # [i, j] 번째 수를 방문하지 않은 경우
            if not visited[i][j]:
                visited[i][j] += 1
                
                # (i,j) 기준 좌표에서 상,하,좌,우 방문 여부 확인
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < N and 0 <= ny < M:
                        visited[nx][ny] += 1
                        
                # parameter: (선택 수 +1, (i,j)번째 수를 sumNum에 더한 값)
                dfs(selectNum+1, sumNum+graph[i][j])
                
                # 재귀함수가 모든 구역을 탐색한 후, 인접한 구역 해제
                visited[i][j] -= 1
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < N and 0 <= ny < M:
                        visited[nx][ny] -= 1

res = -40000 # 입력받는 최솟 값 : -10000 => K는 최대 4이므로 -10000*4=-40000=최솟 값          
N, M, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dfs(0, 0)

print(res)