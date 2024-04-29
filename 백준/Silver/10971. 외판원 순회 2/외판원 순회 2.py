"""
1.전략
- DFS
- 도시를 순회하면서 방문 여부와 도시 비용을 체크
- 비용의 누적합을 구하며 가장 최소가 되는 비용을 res 값에 저장

2.시간복잡도
- O(N!) = 10! = 3,628,800 (Worst case)
  => 2초 이내 가능
"""
import sys; input = sys.stdin.readline

def dfs(depth: int, cost: int, cur: int):
    global graph, visited, res
    
    # N-1 : 모든 도시를 순회한 상태
    # graph[cur][0] : 마지막 지점에서 1로 돌아가는 경로가 존재
    if depth == N-1 and graph[cur][0]:
        res = min(res, cost+graph[cur][0])
        return
    
    for i in range(N):
        # 방문여부와 행렬의 성분이 0인지 확인
        if not visited[i] and graph[cur][i]:
            visited[i] = True
            dfs(depth+1, cost+graph[cur][i], i)
            visited[i] = False

# 입력받기
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# 변수 선언
visited = [False] * N
res = int(1e9)
visited[0] = True

# 합수 실행
dfs(0, 0, 0)

# 결과 출력
print(res)